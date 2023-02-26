from datetime import datetime


def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False

date = input()
if is_valid_date(date):
    print("Valid")
else:
    print("Invalid")
