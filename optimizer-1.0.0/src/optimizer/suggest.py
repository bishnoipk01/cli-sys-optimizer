import psutil

def get_suggestions():
    """Provide system optimization suggestions."""
    suggestions = []

    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 80:
        suggestions.append(f"High CPU usage detected ({cpu_usage}%). Consider closing unnecessary applications.")

    # Memory usage
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > 75:
        suggestions.append(f"High memory usage detected ({memory_usage}%). Consider freeing up memory or adding more RAM.")

    # Disk usage
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > 85:
        suggestions.append(f"High disk usage detected ({disk_usage}%). Consider cleaning up files or adding more storage.")

    # Startup programs
    suggestions.append("Review and disable unnecessary startup programs to speed up boot time.")

    # Swap usage
    swap = psutil.swap_memory()
    if swap.percent > 50:
        suggestions.append(f"High swap usage detected ({swap.percent}%). Consider reducing memory load.")

    # Network activity
    net_io = psutil.net_io_counters()
    if net_io.bytes_recv / 1e6 > 500 or net_io.bytes_sent / 1e6 > 500:
        suggestions.append("High network activity detected. Check for bandwidth-heavy applications.")

    return suggestions
