import psutil

def get_suggestions():
    """Provide rule-based optimization suggestions."""
    suggestions = []
    if psutil.cpu_percent(interval=1) > 80:
        suggestions.append("Close resource-intensive applications.")
    if psutil.virtual_memory().percent > 90:
        suggestions.append("Free up memory by closing unused applications.")
    if psutil.disk_usage('/').percent > 90:
        suggestions.append("Clear large or unnecessary files to free up disk space.")
    return suggestions
