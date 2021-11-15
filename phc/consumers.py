import json

from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync



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
        # text_data_json = json.loads(text_data)
        # message = text_data_json["message"]
        # self.send(text_data = json.dumps({
        #     'message': message
        # }))
        group = self.scope["url_route"]["kwargs"].get("group")
        async_to_sync(self.channel_layer.group_send)(group, {"type":"message.send", "message":message})


    def message_send(self, event):
        # json_event = json.loads(event)
        text = event["message"]["text"]
        json_text = json.loads(text)
        username = json_text["username"]
        print(username)
        content = json_text["content"]
        print(content)
        json_message = {"username":username, "content":content}
        self.send(json.dumps(json_message))