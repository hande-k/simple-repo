# file1.py
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def greet(self) -> str:
        return f"Hello, my name is {self.name}. You can reach me at {self.email}."

    def subscribe(self, subscription):
        return subscription.add_user(self)

if __name__ == "__main__":
    print("User class defined")
