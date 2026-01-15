def format_number(num):
    """Format numbers with commas"""
    return f"{num:,}"

def calculate_percentage(part, whole):
    """Calculate percentage"""
    return (part / whole) * 100 if whole != 0 else 0
