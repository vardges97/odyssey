from typing import List
from typing import TYPE_CHECKING


if TYPE_CHECKING:
   from users.user import User
   from messages.message import Message

class Conversation:
    def __init__(self,participants: List['User']):
        self.participants: List[User] = participants
        self.message_history: List[Message] = []

    def add_message(self,message:"Message"):
        self.message_history.append(message)
        for participant in self.participants:
            if participant != message.sender:
                participant.recieve_message(message)

    def add_user(self,user:"User"):
        self.participants.append(user)

    def get_message(self):
        return self.message_history