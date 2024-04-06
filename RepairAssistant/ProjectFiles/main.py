import shutil
import os

from user_admin import UserAdministration
from fail_methods import FailureMethods
from fail_logs import RepairLog


def repair_assistant():
    """
    Key Features:
    1. User Administration - Requires login to access
    2. Failure Logging - Logs failures performed by technicians in a dictionary
    3. Repair Instructions - Searches failure code in dictionary of proper repairs to return work instructions

    Additional functionality:
        - Allows user to print all logs currently on file
        - Allows user to query repairs done to specific servers
        - Further user administration, allowing creation of new users and the changing of passwords
    """
    user_admin_instance = UserAdministration()
    fail_logs_instance = RepairLog()
    fail_methods_instance = FailureMethods(fail_logs_instance)
    user = user_admin_instance.identify_user()
    cont_program = True

    while cont_program:
        server, failure = fail_methods_instance.input_failure()
        if server is None and failure is None:
            # Either logs have been displayed or cleared, or an invalid command was entered
            pass
        elif failure == "query":
            matching_logs = fail_logs_instance.query_logs_by_server_sn(server)
            if matching_logs:
                print("Matching logs found: ")
                for user, logs in matching_logs.items():
                    print(f"User: {user}")
                    for log in logs:
                        print(log)
            else:
                print("No matching Server SN Found")
        else:
            repair_info = fail_methods_instance.fail_search(failure, user, server)
        cont_program = more_help()
        os.system('cls')


def more_help():
    """
    Asks the user if they would like to continue running the program
    """
    question = input("Would you like to continue with more repairs? (Y/N): ")
    print_dashed_line()
    return question.upper() == "Y"


def print_dashed_line():
    # Get the size of the terminal window
    columns, _ = shutil.get_terminal_size(fallback=(80, 20))

    # Print a line of dashes as wide as the terminal
    print('-' * columns)


# Runs the program
repair_assistant()
