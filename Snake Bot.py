from re import S
import cv2
import numpy as np
import pyautogui
import time

time.sleep(3)
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 25, 255])
threshold = 30
while True:
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    yellow_mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)
    white_mask = cv2.inRange(hsv_frame, lower_white, upper_white)
    food_contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    snake_contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if food_contours and snake_contours:
        largest_food_contour = max(food_contours, key=cv2.contourArea)
        food_x, food_y, food_w, food_h = cv2.boundingRect(largest_food_contour)
        largest_snake_contour = max(snake_contours, key=cv2.contourArea)
        snake_x, snake_y, snake_w, snake_h = cv2.boundingRect(largest_snake_contour)
        target_x = food_x + food_w // 2
        target_y = food_y + food_h // 2
        snake_x = snake_x + snake_w // 2
        snake_y = snake_y + snake_h // 2
        if abs(target_x - snake_x) <= threshold:
            if target_y < snake_y:
                pyautogui.press("w")
                print("Pressed W")
            elif target_y > snake_y:
                pyautogui.press("s")
                print("Pressed S")
        elif abs(target_y - snake_y) <= threshold:
            if target_x < snake_x:
                pyautogui.press("a")
                print("Pressed A")
            elif target_x > snake_x:
                pyautogui.press("d")
                print("Pressed D")