import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont  # Import to customize font
from user_admin import UserAdministration
from fail_logs import RepairLog
from fail_methods import FailureMethods


class RepairApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Repair Assistant")
        self.root.configure(bg="#333333")  # Dark background color

        # Customizing font
        self.customFont = tkfont.Font(family="Helvetica", size=10)

        # Dark theme colors
        self.bg_color = "#333333"
        self.fg_color = "#ffffff"
        self.entry_bg = "#555555"
        self.entry_fg = "#ffffff"
        self.button_bg = "#555555"
        self.button_fg = "#ffffff"
        self.text_bg = "#555555"
        self.text_fg = "#ffffff"

        self.user_admin_instance = UserAdministration()
        self.fail_logs_instance = RepairLog()
        self.fail_methods_instance = FailureMethods(repair_log=self.fail_logs_instance)

        # Define additional attributes
        self.change_password_window = None
        self.change_username_entry = None
        self.old_password_entry = None
        self.new_password_entry = None
        self.login_frame = None
        self.create_user_window = None
        self.username_entry = None
        self.active_user = None
        self.new_user_entry = None
        self.password_entry = None
        self.new_user_password_entry = None
        self.server_sn_entry = None
        self.failure_code_entry = None
        self.display_area = None

        # Create and place widgets for login
        self.create_login_widgets()


    def create_login_widgets(self):
        # Creating a frame to contain all login widgets with dark background
        self.login_frame = tk.Frame(self.root, bg=self.bg_color)
        self.login_frame.pack(pady=10)  # Added padding for better spacing

        # Creating labels, entry boxes, and buttons for login with dark theme adjustments
        tk.Label(self.login_frame, text="Username:", bg=self.bg_color, fg=self.fg_color, font=self.customFont).pack(pady=5)
        self.username_entry = tk.Entry(self.login_frame, bg=self.entry_bg, fg=self.entry_fg, insertbackground=self.fg_color)  # Cursor color
        self.username_entry.pack(pady=5)

        tk.Label(self.login_frame, text="Password:", bg=self.bg_color, fg=self.fg_color, font=self.customFont).pack(pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*", bg=self.entry_bg, fg=self.entry_fg, insertbackground=self.fg_color)
        self.password_entry.pack(pady=5)

        tk.Button(self.login_frame, text="Login", command=self.login, bg=self.button_bg, fg=self.button_fg).pack(pady=5)
        tk.Button(self.login_frame, text="Change Password", command=self.show_change_password_window, bg=self.button_bg, fg=self.button_fg).pack(pady=5)
        tk.Button(self.login_frame, text="Create New User", command=self.show_create_user_window, bg=self.button_bg, fg=self.button_fg).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_admin_instance.verify_password(password, username):
            messagebox.showinfo("Login Info", "Login Successful")
            # Store the current user as an instance
            self.active_user = username
            # Destroy the widgets safely
            self.login_frame.destroy()
            # Now create the main window
            self.create_main_window()
        else:
            messagebox.showerror("Login Info", "Invalid Username or Password")
        return username

    def show_change_password_window(self):
        self.change_password_window = tk.Toplevel(self.root)
        self.change_password_window.title("Change Password")

        tk.Label(self.change_password_window, text="Username:").pack()
        self.change_username_entry = tk.Entry(self.change_password_window)
        self.change_username_entry.pack()

        tk.Label(self.change_password_window, text="Old Password:").pack()
        self.old_password_entry = tk.Entry(self.change_password_window, show="*")
        self.old_password_entry.pack()

        tk.Label(self.change_password_window, text="New Password:").pack()
        self.new_password_entry = tk.Entry(self.change_password_window, show="*")
        self.new_password_entry.pack()
        tk.Button(self.change_password_window, text="Change Password", command=self.change_password).pack()

    def show_create_user_window(self):
        self.create_user_window = tk.Toplevel(self.root)
        self.create_user_window.title("Create New User")
        self.create_user_window.configure(bg=self.bg_color)

        tk.Label(self.create_user_window, text="Username:", bg=self.bg_color, fg=self.fg_color, font=self.customFont).pack(pady=5)
        self.new_user_entry = tk.Entry(self.create_user_window, bg=self.entry_bg, fg=self.entry_fg, insertbackground=self.fg_color)
        self.new_user_entry.pack(pady=5)

        tk.Label(self.create_user_window, text="Password:", bg=self.bg_color, fg=self.fg_color, font=self.customFont).pack(pady=5)
        self.new_user_password_entry = tk.Entry(self.create_user_window, show="*", bg=self.entry_bg, fg=self.entry_fg, insertbackground=self.fg_color)
        self.new_user_password_entry.pack(pady=5)

        tk.Button(self.create_user_window, text="Create User", command=self.create_new_user, bg=self.button_bg, fg=self.button_fg).pack(pady=5)

    def create_main_window(self):
        """
        This method sets up the main application window
        """

        # Load the logo
        self.logo_image = tk.PhotoImage(file="/home/kelz/ProfessionalPortfolio/RepairAssistant/quanta_logo.png")
        # Display Logo
        self.logo_label = tk.Label(self.root, image=self.logo_image, bg=self.bg_color)
        self.logo_label.pack(pady=2, padx=2) 

        tk.Label(self.root, text="Server SN:", bg=self.bg_color, fg=self.fg_color, font=self.customFont).pack(pady=5)
        self.server_sn_entry = tk.Entry(self.root, bg=self.entry_bg, fg=self.entry_fg, insertbackground=self.fg_color)
        self.server_sn_entry.pack(pady=5)

        tk.Label(self.root, text="Failure Code:", bg=self.bg_color, fg=self.fg_color, font=self.customFont).pack(pady=5)
        self.failure_code_entry = tk.Entry(self.root, bg=self.entry_bg, fg=self.entry_fg, insertbackground=self.fg_color)
        self.failure_code_entry.pack(pady=5)

        tk.Button(self.root, text="Repair Info", command=self.retrieve_info, bg=self.button_bg, fg=self.button_fg).pack(pady=5)
        tk.Button(self.root, text="Clear Logs", command=self.clear_logs, bg=self.button_bg, fg=self.button_fg).pack(pady=5)
        tk.Button(self.root, text="View Logs", command=self.view_logs, bg=self.button_bg, fg=self.button_fg).pack(pady=5)
        tk.Button(self.root, text="Query Logs by Server SN", command=self.query_logs, bg=self.button_bg, fg=self.button_fg).pack(pady=5)

        # Adjusting the Text widget for the dark theme
        self.display_area = tk.Text(self.root, height=30, width=60, bg=self.text_bg, fg=self.text_fg)
        self.display_area.pack(pady=5)

    def retrieve_info(self):
        # Get inputs
        server = self.server_sn_entry.get()
        failure = self.failure_code_entry.get()
        user = self.active_user

        # Use the FailureMethods class to retrieve the repair information
        repair_info = self.fail_methods_instance.get_repair_info(failure)
        if repair_info:
            self.display_area.insert(tk.END, f"Repair info for {server}: {repair_info}\n")
            # Now ask for repair confirmation and log the repair if confirmed
            if self.fail_logs_instance.log_failure(user, failure, repair_info, server):
                self.display_area.insert(tk.END, "Repair Logged Successfully\n")
            else:
                self.display_area.insert(tk.END, "Repair Log Unsuccessful\n")
        else:
            self.display_area.insert(tk.END, "No repair info found for the given failure code.\n")

    def clear_logs(self):
        # Clear the logs using the RepairLog class
        self.fail_logs_instance.clear_logs()
        self.display_area.insert(tk.END, "Logs have been cleared.\n")

    def view_logs(self):
        # Display the current logs
        logs = self.fail_logs_instance.repair_log
        self.display_area.insert(tk.END, f"Current Logs: {logs}\n")

    def query_logs(self):
        # Query the logs by server SN
        server = self.server_sn_entry.get()
        matching_logs = self.fail_logs_instance.query_logs_by_server_sn(server)
        if matching_logs:
            self.display_area.insert(tk.END, f"Matching logs for {server}: {matching_logs}\n")
        else:
            self.display_area.insert(tk.END, "No matching logs found for the given Server SN.\n")


def main():
    root = tk.Tk()
    root.geometry('800x600')
    app = RepairApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
