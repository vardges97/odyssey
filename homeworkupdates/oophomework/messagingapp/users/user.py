from typing import List
from messages.message import Message
from convos.conversaition import Conversation


class User:
    def __init__(self,name:str,contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.conversations : List[Conversation] = []

    def create_conversation(self,user:'User'):
        conversation = Conversation([self,user])
        self.conversations.append(conversation)
        user.conversations.append(conversation)
        return conversation

    def send_message(self,message:'Message',conversation='Conversation'):
        if conversation in self.conversations:
            conversation.add_message(message)
        else:
            print('you are not in this conversation')

    def recieve_message(self,message:"Message") -> None:
        print(f"new message for: {self.name}")
        message.display_content()

    def manage_setting(self):
        print(f"managing settings for{self.name}")

    def get_conversation(self)-> List['Conversation']:
        return self.conversations