import datetime


def print_header():
    print("--------------------------")
    print("       BIRTHDAY APP")
    print("--------------------------")


def get_birthday_from_user():
    print("When were you born?")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_day_between_dates(original_date, target_date):
    this_year = datetime.date(
        year=target_date.year, month=original_date.month, day=original_date.day
    )
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print(f"You had your birthday {-days} days ago this year")
    elif days > 0:
        print(f"Your birthday is in {days} days.")
    else:
        print(f"Happy Birthday!!!")


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_day_between_dates(bday, today)
    print_birthday_information(number_of_days)


main()
