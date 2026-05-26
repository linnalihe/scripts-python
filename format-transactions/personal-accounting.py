from datetime import datetime

def format_dates(line):
    # Get the current year
    year = datetime.now().year
    

    if not line.strip():
        return ''
    try:
        # Parse the MM/DD format
        month, day = map(int, line.split('/'))
        # Create a new date string in YYYY-MM-DD format
        # new_date = datetime(current_year, month, day).strftime('%Y-%m-%d')
        
        new_date = datetime(year, month, day).strftime('%Y-%m-%d')

    except ValueError:
        # Handle invalid date formats
        print(f"Invalid date format: {line}")
        return ''

    return new_date

def format_amount(amount):
    # Remove the comma from the amount
    return amount.replace(',', '').replace('$', '')


def format_row(line):
    # strip the whitespace at beginning and end of line
    stripped_line = line.strip()
    
    if not stripped_line:
        return ''
    # get the string before the first whitespace
    date = format_dates(line.split()[0])
    # get the string after the first whitespace until the last whitespace
    description = ' '.join(line.split()[1:-1])
    # get the string after the last whitespace
    amount = format_amount(line.split()[-1])

    return f"{date};{description};{amount}"


# Example usage
if __name__ == "__main__":
    dates_to_format = """
06/17 Jun 09 Deposit Activity 3,227.08 
06/07 Deposit Internet - Transfer from 591970001 CK 3,000.00
06/30 Withdrawal Transferring - mortgage for 2025-07 -3,000.00
06/30 Credit Interest 33.83
    """

    for line in dates_to_format.split('\n'):
        print(format_row(line))

    # rewrite the above line to print in reverse order
    