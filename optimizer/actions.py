import os

def execute_action(action):
    """Perform optimization actions based on user input."""
    if action == "clear_logs":
        log_path = "/var/log"
        print(f"Clearing logs in {log_path}...")
        for file in os.listdir(log_path):
            file_path = os.path.join(log_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("Logs cleared.")
    else:
        print(f"Unknown action: {action}")
