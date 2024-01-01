from fail_logs import RepairLog

RepairLog = RepairLog()


class FailureMethods:
    def __init__(self, repair_log):
        self.failure_dict = {
            "field diag": "Process - SEL Cleared, PC, and Reseated Trays - OTH-OT",
            "ssd nd": "Process - SEL Cleared, PC, and Reseated Trays - SSD-ND"
        }
        self.repair_log = repair_log

    def input_failure(self):
        """
        Takes the server SN and failure code as inputs.
        """
        server = input("What is the server SN: ('logs' to view logs, 'clear' to clear logs) ")
        if server.lower() == "logs":
            print(self.repair_log.repair_log)
            return None, None
        elif server.lower() == "clear":
            self.repair_log.clear_logs()
            return None, None
        else:
            failure = input("What is the failure code: ('query' to query logs for server SN) ")
            return server, failure

    def fail_search(self, failure, user, server):
        """
        Searches the dictionary of failures and prints repair information for the technician.
        """
        if failure in self.failure_dict:
            repair_info = self.failure_dict[failure]
            print("Here is the repair information: ")
            print("--------------------------------------------------------------------")
            print(repair_info)
            print("--------------------------------------------------------------------")
            if server == "":
                print("No Server Information - Repair Logged Unsuccessfully")
            else:
                repair_confirmation = input("Repair Complete: (Y/N) ")
                if repair_confirmation.upper() == "Y":
                    if server is not None:
                        self.repair_log.log_failure(user, failure, repair_info, server)
                        print("Repair Logged Successfully")
                else:
                    print("Repair status not logged: No repair confirmation received.")
            return repair_info
        else:
            print("No info found for this failure code.")
            return None
