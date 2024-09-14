from users.user import User
from messages.message import TextMessage, MultimediaMessage


def main():
    bob = User("bob", "bob@example.com")
    rob = User("rob", "rob@example.com")

    conversation = bob.create_conversation(bob)

    text_message = TextMessage(sender=bob, conversation=conversation, content="Hello Bob")
    bob.send_message(text_message, conversation)

    multimedia_message = MultimediaMessage(sender=rob, conversation=conversation, file_path="/images/photo.jpg", media_type="Image")
    rob.send_message(multimedia_message, conversation)

    print("\n--- Conversation History ---")
    for message in conversation.get_message():
        message.display_content()

if __name__ == "__main__":
    main()