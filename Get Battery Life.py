import psutil
from time import sleep
from os import system, name
battery_percent = psutil.sensors_battery().percent
battery_seconds = psutil.sensors_battery().secsleft
battery_minutes = battery_seconds / 60
battery_hours = battery_seconds / 3600
def start(battery_seconds):
    if battery_seconds == -2:
        plugged_in(battery_seconds)
    else:
        not_plugged_in(battery_seconds)

def plugged_in(battery_seconds):
    while battery_seconds == -2:
        system('cls' if name == 'nt' else 'clear')
        print(f"Battery Life Left ({battery_percent}%):\n\nInfinite (plugged in).")
        battery_seconds = psutil.sensors_battery().secsleft
        sleep(1)
    not_plugged_in(battery_seconds)

def not_plugged_in(battery_seconds):
    battery_minutes = battery_seconds / 60
    battery_hours = battery_seconds / 3600
    battery_seconds_estimate = psutil.sensors_battery().secsleft
    while battery_seconds_estimate >= 0:
        system('cls' if name == 'nt' else 'clear')
        print(f"Battery Life Left ({battery_percent}%):\n\nAbout {battery_seconds} seconds.\n\n|OR|\n\nAbout {battery_minutes} minutes.\n\n|OR|\n\nAbout {battery_hours} hours.")
        sleep(1)
        battery_seconds -= 1   
        battery_minutes = battery_seconds / 60
        battery_hours = battery_seconds / 3600
        battery_seconds_estimate = psutil.sensors_battery().secsleft
        if battery_seconds_estimate < battery_seconds:
            battery_seconds = battery_seconds_estimate
    plugged_in(battery_seconds_estimate)

start(battery_seconds)