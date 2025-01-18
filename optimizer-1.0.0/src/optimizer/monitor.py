import psutil

def display_resources():
    """Monitor system resources in real-time."""
    print("Monitoring system resources:")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
    print(f"Network I/O: {psutil.net_io_counters().bytes_sent / 1e6:.2f} MB sent, "
          f"{psutil.net_io_counters().bytes_recv / 1e6:.2f} MB received")
