import pandas as pd
import matplotlib.pyplot as plt
from chat_class import User, Chat
from logger import ChatLogger

u1 = User("Alice")
u2 = User("Bob")

chat = Chat("Alice-Bob", [u1, u2])
logger = ChatLogger()

while True:
    print("\n1. Send Message")
    print("2. Show Stats")
    print("3. Pandas Analysis")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sender = u1 if input("Sender (1-Alice / 2-Bob): ") == "1" else u2
        msg = input("Enter message: ")
        chat.add_message(sender, msg, logger)

    elif choice == "2":
        print(chat.get_stats())

    elif choice == "3":
        df = pd.read_csv(
            "chat_log.txt",
            sep="|",
            header=None,
            names=["time", "chat", "user", "message"]
        )
        print(df["user"].value_counts())
        df["user"].value_counts().plot(kind="bar")
        plt.show()

    elif choice == "4":
        break
