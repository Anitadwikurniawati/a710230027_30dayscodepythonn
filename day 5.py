from abc import ABC, abstractmethod

class MessageMethod(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass

class EmailSender(MessageMethod):
    def send(self, message, recipient):
        print(f"Sending email to {recipient}: {message}")

class SMSSender(MessageMethod):
    def send(self, message, recipient):
        print(f"Sending SMS to {recipient}: {message}")

class MessageSender:
    def __init__(self, method: MessageMethod):
        self.method = method

    def send_message(self, message, recipient):
        self.method.send(message, recipient)

email_sender = EmailSender()
sms_sender = SMSSender()

message_sender = MessageSender(email_sender)
message_sender.send_message('Hello, World!', 'user@example.com')

message_sender = MessageSender(sms_sender)
message_sender.send_message('Hello, World!', '123-456-7890')
