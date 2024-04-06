import os
import sys


class UserAdministration:
    def __init__(self):
        self.user_dict = {
            "kcantrell": "Pass",  # Plain text password for demonstration
        }

    def identify_user(self):
        """
        Asks the user for their credentials before using the application.
        """
        username_attempts = 0  # Counter for username attempts

        while username_attempts < 3:
            user = input("Please provide your username: ")

            if user in self.user_dict:
                attempt_count = 0  # Counter for password attempts

                while attempt_count < 3:
                    password = input("Please input your password: ")

                    if self.verify_password(password, user):
                        self.clear_screen()
                        print("Login Successful!")
                        return user

                    attempt_count += 1
                    if attempt_count < 3:
                        print(f"Incorrect Password. You have {3 - attempt_count} attempts left.")
                    else:
                        self.clear_screen()
                        print("Incorrect Password")

                if attempt_count >= 3:
                    if self.request_password_change():
                        self.change_password(user)
                        return self.identify_user()  # Restart function after password change
                    else:
                        self.clear_screen()
                        print("Login Unsuccessful")
                        sys.exit()

            else:
                username_attempts += 1
                if username_attempts < 3:
                    print(f"Username not found. You have {3 - username_attempts} attempts left.")
                else:
                    self.clear_screen()
                    print("Username not found")
                    if self.request_user_creation():
                        self.add_user()
                        return self.identify_user()  # Recursive call to restart the function
                    else:
                        print("Exiting the application.")
                        sys.exit()

        return None  # Return None if the loop exits without successful login

    def verify_password(self, password, user):
        """
        Verifies the provided password against the stored password.

        Args:
            password (str): The password provided by the user.
            user (str): The username of the user.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        return password == self.user_dict[user]

    def change_password(self, user):
        """
        Allows the user to change their password by altering the user_dict.
        """
        new_pw = input("What is your new password: ")
        self.user_dict[user] = new_pw
        print("Your password has been changed.")

    def add_user(self):
        """
        Allows for the creation of a new user.
        """
        new_user = input("Create your username: ")
        new_user_pw = input("Create your password: ")
        self.user_dict[new_user] = new_user_pw
        print("Your account has been created.")

    @staticmethod
    def clear_screen():
        """Clears the terminal screen."""
        # For Windows
        if os.name == 'nt':
            os.system('cls')
        # For Unix/Linux/Mac
        else:
            os.system('clear')

    @staticmethod
    def request_password_change():
        change_request = input("Would you like to change your password? (Y/N) ")
        return change_request.upper() == "Y"

    @staticmethod
    def request_user_creation():
        creation_request = input("Would you like to create a new user? (Y/N) ")
        return creation_request.upper() == "Y"
