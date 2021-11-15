import json

from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from phc import basic_hash_chain
from phc import sm2
# send_hash_chain = basic_hash_chain.Hash_Chain()
# basic_hash_chain.init_hash_chain(send_hash_chain)
#
# recv_hash_chain = basic_hash_chain.Hash_Chain()
# basic_hash_chain.init_hash_chain(recv_hash_chain)

global hash_chain_p
hash_chain_p = {}

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):

        self.accept()
        group = self.scope["url_route"]["kwargs"].get("group")
        async_to_sync(self.channel_layer.group_add)(group,self.channel_name)

    def websocket_disconnect(self, message):
        group = self.scope["url_route"]["kwargs"].get("group")
        async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)
        print('断开连接')
        raise StopConsumer()

    def websocket_receive(self, message):

        group = self.scope["url_route"]["kwargs"].get("group")
        async_to_sync(self.channel_layer.group_send)(group, {"type":"message.send", "message":message})


    def message_send(self, event):
        # json_event = json.loads(event)
        text = event["message"]["text"]
        json_text = json.loads(text)
        username = json_text["username"]
        content = json_text["content"]
        sig_opt = json_text["sig_opt"]

        global hash_chain_p

        final_node = ""
        if hash_chain_p.__contains__(username) == False :
            hash_chain = basic_hash_chain.Hash_Chain()
            basic_hash_chain.init_hash_chain(hash_chain)
            basic_hash_chain.basic_hash_chain_construction(content, hash_chain)
            hash_chain_p[username] = hash_chain
            final_node = hash_chain.get_final_hash_chain_node()

        else:
            hash_chain = hash_chain_p[username]
            basic_hash_chain.basic_hash_chain_construction(content, hash_chain)
            hash_chain_p[username] = hash_chain
            final_node = hash_chain.get_final_hash_chain_node()

        signature_txt = ""
        if sig_opt == "4":
            signature_txt = sm2.sm2_encrypt(content)
        json_message = {"username":username, "content":content, "final_node": final_node, "signature_txt":signature_txt}
        self.send(json.dumps(json_message))