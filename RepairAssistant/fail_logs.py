import os


class RepairLog:
    def __init__(self):
        """
        Initializes a new instance of RepairLog.
        """
        self.repair_log = {}

    def log_failure(self, user, failure, repair_info, server):
        """
        Logs the failure, repair information, and server SN into the repair log.

        Args:
            user (str): The user logging the failure.
            failure (str): Description of the failure.
            repair_info (str): Information about the repair.
            server (str): Server Serial Number.
        """
        if repair_info and server is not None:
            # Create a new repair entry
            repair_entry = {
                "Server SN": server,
                "Failure": failure,
                "Repair Info": repair_info
            }

            # Check if the user already has repair logs
            if user in self.repair_log:
                # Add the new repair entry to the existing list for this user
                self.repair_log[user].append(repair_entry)
            else:
                # Create a new list for this user with the repair entry
                self.repair_log[user] = [repair_entry]

    def clear_logs(self):
        """
        Clears the repair log and prints a confirmation message.
        """
        self.repair_log.clear()
        print("Logs have been successfully cleared.")

    def query_logs_by_server_sn(self, server):
        """
        Queries the logs for entries related to a specific server SN.

        Returns:
            dict: A dictionary of log entries matching the specified server SN.
        """
        matching_logs = {}

        # Iterate through each user's logs
        for user, user_logs in self.repair_log.items():
            # Iterate through each log entry for the user
            for log in user_logs:
                if log.get("Server SN") == server:
                    # Add the matching log entry to the matching_logs dictionary
                    if user not in matching_logs:
                        matching_logs[user] = []
                    matching_logs[user].append(log)
        # Check if matching logs were found
        if matching_logs:
            return matching_logs
