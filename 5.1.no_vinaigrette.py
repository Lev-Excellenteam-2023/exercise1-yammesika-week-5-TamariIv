import datetime
import random


def no_vinaigrette():       # from 5.1
    date1 = input("Enter the first date in format YYYY-MM-DD:")
    date2 = input("Enter the second date in format YYYY-MM-DD:")
    date1 = datetime.strptime(date1, '%Y-%m-%d').date()
    date2 = datetime.strptime(date2, '%Y-%m-%d').date()
    if date1 > date2:
        date1, date2 = date2, date1
    diff = date2 - date1

    rand_days = random.randrange(diff.days)
    rand_date = date1 + datetime.timedelta(days=rand_days)
    print(rand_date)
    if rand_date.weekday() == 0:
        print("I have no vinaigrette!")


if __name__ == '__main__':
    no_vinaigrette()
