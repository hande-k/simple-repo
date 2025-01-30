# file3.py
from file1 import User
from file2 import Subscription

class SubscriptionManager:
    def __init__(self):
        self.subscriptions = {}

    def create_subscription(self, name: str):
        if name not in self.subscriptions:
            self.subscriptions[name] = Subscription(name)
            return f"Subscription '{name}' created."
        return f"Subscription '{name}' already exists."

    def add_user_to_subscription(self, user: User, subscription_name: str) -> str:
        if subscription_name in self.subscriptions:
            return self.subscriptions[subscription_name].add_user(user)
        return f"Subscription '{subscription_name}' does not exist."

if __name__ == "__main__":
    manager = SubscriptionManager()
    manager.create_subscription("Python Monthly")
    user = User(name="Alice", email="alice@example.com")
    print(manager.add_user_to_subscription(user, "Python Monthly"))
