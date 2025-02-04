import os
import json
import getpass

class Authentication:
    @staticmethod
    def load_users(file_path):
        # Loaded user data from the specified file
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return {}

    @staticmethod
    def save_users(file_path, users):
        # Saved user data to the specified file
        with open(file_path, 'w') as file:
            json.dump(users, file)

    @staticmethod
    def register(file_path, user_type):
        users = Authentication.load_users(file_path)
        while True:
            username = input("Enter a new username: ")
            if username in users:
                print("Username already exists. Please try again.")
            else:
                break
        password = getpass.getpass("Enter a new password: ")
        users[username] = {'password': password, 'type': user_type}
        Authentication.save_users(file_path, users)
        print("Registration successful.")

    @staticmethod
    def login(file_path):
        users = Authentication.load_users(file_path)
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        if username in users and users[username]['password'] == password:
            print("Login successful.")
            return users[username]['type']
        else:
            print("Invalid username or password. Please try again.")
            return None

    @staticmethod
    def authenticate(file_path):
        while True:
            # Displayed the authentication menu to the user
            print("\n" + "="*120)
            print("Welcome to Sampath Food City Sales Data System".center(120))
            print("="*120)
            print("1. Register as Admin")
            print("2. Register as Regular User")
            print("3. Login")
            print("0. Exit")
            print("="*120)
            choice = input("Select an option: ")
            if choice == '1':
                Authentication.register(file_path, 'admin')
            elif choice == '2':
                Authentication.register(file_path, 'regular')
            elif choice == '3':
                user_type = Authentication.login(file_path)
                if user_type:
                    return user_type
            elif choice == '0':
                print("Exiting the program.")
                return None
            else:
                print("Invalid option. Please try again.")
