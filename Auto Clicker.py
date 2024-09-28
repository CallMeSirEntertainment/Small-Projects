import pyautogui
import time
user_choice = input("Would you like to choose the amount of time to click or the amount of clicks? (t/c)\n").lower()
if user_choice == 'c':
    num_clicks = int(input("\nHow many clicks do you want?\n"))
    clicks = 0
    print('Auto clicker starting in 10 seconds. Please move your mouse to the desired position.')
    time.sleep(10)
    while clicks in range(0, num_clicks + 1):
        pyautogui.click()
        clicks += 1
elif user_choice == 't':
    click_time = int(input("\nHow many seconds should it click?\n"))
    click_time *= 10
    print('Auto clicker starting in 10 seconds. Please move your mouse to the desired position.')
    time.sleep(10)
    for i in range(click_time):
        pyautogui.click()
else:
    print("Invalid input. Please enter 'c' for clicks or 't' for time.")