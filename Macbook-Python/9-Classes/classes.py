
class User:
    def __init__(self, first_name, last_name, age, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username

    def describe_user(self):
        
        print(f"User Profile:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

# Example usage
user1 = User("John", "Doe", 30, "john.doe@example.com", "johndoe")
user1.describe_user()
user1.greet_user()