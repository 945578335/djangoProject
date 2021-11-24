import json
import time

from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from phc import hash_chain_progress
from phc import sm2
from phc import models
from django.db.models import Max

salt = "453245b037ea9220b49395e65954411ad156bcc1dddf712863f2c8ecfcb22dc4"
share_key = "3245b037ea9220b49395e65954411ad156bcc1dddf712863f2c8ecfcb22dc445"
# send_hash_chain = basic_hash_chain.Hash_Chain()
# basic_hash_chain.init_hash_chain(send_hash_chain)
#
# recv_hash_chain = basic_hash_chain.Hash_Chain()
# basic_hash_chain.init_hash_chain(recv_hash_chain)

global hash_chain_p
hash_chain_p = {}

global sig_sign
sig_sign = True
global interval_num
interval_num = 10
global sig_method
sig_method = "0"

global msg_content_flag
msg_content_flag = ""

global user_num
user_num = 0

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):

        self.accept()
        global user_num
        user_num = user_num + 1
        group = self.scope["url_route"]["kwargs"].get("group")
        async_to_sync(self.channel_layer.group_add)(group, self.channel_name)

    def websocket_disconnect(self, message):
        group = self.scope["url_route"]["kwargs"].get("group")
        async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)
        print('断开连接')
        global user_num
        user_num = user_num - 1
        raise StopConsumer()

    def websocket_receive(self, message):

        text = message["text"]
        json_text = json.loads(text)
        username_ip = json_text["sip"]
        dip = json_text["dip"]
        content = json_text["content"]
        sig_opt = json_text["sig_opt"]
        con_opt = json_text["con_opt"]

        global msg_content_flag
        if msg_content_flag == content:
            return
        else:
            msg_content_flag = content

        global hash_chain_p

        if not hash_chain_p.__contains__(username_ip):

            try:
                db = models.HashChain.objects.filter(sip=username_ip, dip=dip).aggregate(Max('seq'))
                seq_max = db['seq__max']
                chaindb = models.HashChain.objects.filter(sip=username_ip, dip=dip, seq=seq_max)

                hashnode = {}
                try:
                    hashnode["sip"] = chaindb[0].sip
                    hashnode["dip"] = chaindb[0].dip
                    hashnode["chainhash"] = chaindb[0].chainhash
                    hashnode["pkthash"] = chaindb[0].msghash
                    hashnode["seq"] = chaindb[0].seq
                except:
                    hashnode = hash_chain_progress.init_hash_chain(username_ip, dip)
                # print(hashnode)
            except models.HashChain.DoesNotExist:
                hashnode = hash_chain_progress.init_hash_chain(username_ip, dip)

            hash_chain_p[username_ip] = hashnode
        else:
            hashnode = hash_chain_p[username_ip]

        if con_opt == "1":
            hashnode = hash_chain_progress.basic_hash_chain_construction(content, hashnode)
        elif con_opt == "2":
            hashnode = hash_chain_progress.pk_hash_chain_construction(content, hashnode)
        elif con_opt == "3":
            hashnode = hash_chain_progress.salt_hash_chain_construction(content, hashnode)
        elif con_opt == "4":
            hashnode = hash_chain_progress.basic_hash_chain_construction(content, hashnode)

        hash_chain_p[username_ip] = hashnode
        final_node = hashnode["chainhash"]
        final_seq = hashnode["seq"]
        pkt_hash = hashnode["pkthash"]

        signature_txt = ""
        global sig_sign
        global sig_method
        global interval_num

        action = "报文哈希链验证成功"
        if sig_method == "2" and sig_opt != "2":
            sig_sign = True
        else:
            if sig_opt == "1":
                if sig_method == sig_opt:
                    sig_sign = False
                else:
                    sig_method = sig_opt
            elif sig_opt == "2":
                sig_sign = False
                sig_method = sig_opt
            elif sig_opt == "3":
                interval_num = interval_num - 1
                if interval_num == 0:
                    sig_sign = True
                    interval_num = 10
                else:
                    sig_sign = False
                sig_method = sig_opt
            elif sig_opt == "4":
                sig_sign = True
                sig_method = sig_opt

        if sig_sign == True:
            signature_txt = sm2.sm2_encrypt(content)
            action = "链式签名验证成功"

        global user_num
        if user_num > 2:
            json_message = {"username_ip": username_ip, "content": "", "final_node": "",
                            "signature_txt": "", "seq_s": "", "action_s": "",
                            "msghash_s": "",
                            "chainhash_s": ""}
            group = self.scope["url_route"]["kwargs"].get("group")
            async_to_sync(self.channel_layer.group_send)(group, {"type": "message.send", "message": json_message})
            time.sleep(1)
        else:

            if con_opt == "1":
                models.HashChain.objects.create(sip=username_ip, dip=dip, seq=final_seq, contype=con_opt,
                                                signtype=sig_opt, content=content, msghash=pkt_hash, chainhash=final_node,
                                                action=action)
            elif con_opt == "2":
                models.HashChain.objects.create(sip=username_ip, dip=dip, seq=final_seq, contype=con_opt,
                                                signtype=sig_opt, content=content, msghash=pkt_hash,
                                                chainhash=final_node, sharekey=share_key, action=action)
            elif con_opt == "3":
                models.HashChain.objects.create(sip=username_ip, dip=dip, seq=final_seq, contype=con_opt,
                                                signtype=sig_opt, content=content, msghash=pkt_hash,
                                                chainhash=final_node, salt=salt, action=action)
            elif con_opt == "4":
                models.HashChain.objects.create(sip=username_ip, dip=dip, seq=final_seq, contype=con_opt,
                                                signtype=sig_opt, content=content, msghash=pkt_hash, chainhash=final_node,
                                                action=action)
            else:
                models.HashChain.objects.create(sip=username_ip, dip=dip, seq=final_seq, contype=con_opt,
                                                signtype=sig_opt, content=content, msghash=pkt_hash, chainhash=final_node,
                                                action=action)

            json_message = {"username_ip": username_ip, "content": content, "final_node": final_node,
                            "signature_txt": signature_txt, "seq_s": final_seq, "action_s": action, "msghash_s": pkt_hash,
                            "chainhash_s": final_node}



            group = self.scope["url_route"]["kwargs"].get("group")
            async_to_sync(self.channel_layer.group_send)(group, {"type": "message.send", "message": json_message})
            time.sleep(1)

    def message_send(self, event):
        # json_event = json.loads(event)
        message = event["message"]

        self.send(json.dumps(message))
