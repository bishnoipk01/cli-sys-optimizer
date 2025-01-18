import psutil

def list_processes():
    """List all running processes."""
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")

def kill_process(name):
    """Kill a process by name."""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == name:
            try:
                proc.terminate()
                print(f"Terminated: {name}")
                return
            except Exception as e:
                print(f"Failed to terminate {name}: {e}")
                return
    print(f"Process {name} not found.")
