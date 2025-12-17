def message_sent(func):
    def wrapper(*args):
        func(*args)
        print("[MESSAGE SENT]")
    return wrapper


class ChatLogger:
    def __init__(self, file_name="chat_log.txt"):
        self.file_name = file_name

    @message_sent
    def log_message(self, chat_name, message):
        with open(self.file_name, "a") as f:
            f.write(
                f"{message.timestamp}|{chat_name}|{message.sender.username}|{message.text}\n"
            )
