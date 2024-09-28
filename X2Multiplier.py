from time import sleep
from os import system, name
from sys import set_int_max_str_digits
set_int_max_str_digits(0)
try:
    cents = 1
    dollars = cents / 100
    dollars = round(dollars)
    hours = 0
    days = hours / 24
    days = round(days, 1)
    weeks = days / 7
    weeks = round(weeks, 2)
    print(f"${dollars} after {hours} hours.")
    sleep(1)
except Exception as e:
    print("Error:", e)
while True:
    try:
        system('cls' if name == 'nt' else 'clear')
        hours += 1
        cents *= 2
        dollars = cents / 100
        dollars = round(dollars)
        days = hours / 24
        days = round(days, 1)
        weeks = days / 7
        weeks = round(weeks, 5)
        if hours >= 24:
            if days >= 7:
                if weeks == 1:
                    print(f"${dollars} after {round(weeks)} week.")
                else:
                    print(f"${dollars} after {weeks} weeks ({days} days).")
            else:
                if days == 1:
                    print(f"${dollars} after {round(days)} day.")
                else:
                    if hours == 69:
                        print(f"${dollars} after {days} days (noice hours).")
                    else:
                        print(f"${dollars} after {days} days ({hours} hours).")
        else:
            if hours == 1:
                print(f"${dollars} after {hours} hour.")
            else:
                print(f"${dollars} after {hours} hours.")
        sleep(0.5)
    except Exception as e:
        print("Error:", e)