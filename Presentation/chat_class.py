from datetime import datetime

class User:
    def __init__(self, username):
        self.username = username


class Message:
    def __init__(self, text, sender):
        self.text = text
        self.sender = sender
        self.timestamp = datetime.now()

    def __str__(self):
        time_format = lambda t: t.strftime("%H:%M:%S")
        return f"{self.sender.username}: {self.text} ({time_format(self.timestamp)})"


class Chat:
    def __init__(self, name, users):
        self.name = name
        self.users = users
        self.messages = []

    def add_message(self, sender, text, logger):
        msg = Message(text, sender)
        self.messages.append(msg)
        print(msg)
        logger.log_message(self.name, msg)

    def get_stats(self):
        stats = {}
        for m in self.messages:
            stats[m.sender.username] = stats.get(m.sender.username, 0) + 1
        return stats
