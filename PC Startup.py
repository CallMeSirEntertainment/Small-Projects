from pyttsx3 import speak
import psutil
from time import sleep
psutil.cpu_percent()
sleep(0.1)
i = 1
if psutil.sensors_battery().power_plugged == True:
    battery_message = "currently plugged in"
else:
    battery_message = "not plugged in"
psutil.virtual_memory().percent
speak(f"Good day, Here are your system diagnostics! Battery is at {psutil.sensors_battery().percent} percent, and is {battery_message}. CPU core count: {psutil.cpu_count()} . Total CPU usage: {psutil.cpu_percent()} percent")
sleep(0.1)
for cpu_percent in psutil.cpu_percent(percpu=True):
    speak(f"Core {i}: {cpu_percent} percent.")
    i += 1
speak(f"Memory comsumption is {psutil.virtual_memory().percent} percent. Total disk usage is {psutil.disk_usage('c:').percent} percent. This PC has been booted for a total of {round((psutil.boot_time()/60)/60)} hours.")