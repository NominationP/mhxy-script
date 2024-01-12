import os
import time

import pygetwindow as gw
import pyautogui

app_name = 'MuMu模拟器12-1'
folder_path = "screenshots"

def get_screenshot_path():
    # Get the window with the title of your app
    app_window = gw.getWindowsWithTitle(app_name)[0]

    # Get the coordinates of the app window
    app_left, app_top, app_width, app_height = app_window.left, app_window.top, app_window.width, app_window.height

    # Calculate the coordinates of the bottom right corner of the app window
    app_right = app_left + app_width
    app_bottom = app_top + app_height

    # Capture a screenshot of the app window
    app_screenshot = pyautogui.screenshot(region=(app_left, app_top, app_width, app_height))

    current_time = time.strftime("%Y%m%d-%H%M%S")
    path = os.path.join(folder_path, f"{current_time}_screenshot.png")

    app_screenshot.save(path)


if __name__ == '__main__':
    get_screenshot_path()
