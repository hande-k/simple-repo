# file2.py
from file1 import User

class Subscription:
    def __init__(self, name: str):
        self.name = name
        self.users = []

    def add_user(self, user: User) -> str:
        self.users.append(user)
        return f"{user.name} has subscribed to {self.name}."

    def list_users(self):
        return [user.name for user in self.users]

if __name__ == "__main__":
    print("Subscription class defined")
