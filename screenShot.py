import os
from datetime import datetime
import time
from PIL import ImageGrab
# from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
# import Quartz
import os
import time
import win32gui
from PIL import ImageGrab
import os
import time

import pygetwindow as gw
import pyautogui
pyautogui.FAILSAFE = False
app_name = "网易MuMu"  # Specify the exact window title

# Create a folder named "screenshot" if it doesn't exist
folder_name = "screenshot"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# def get_window_coordinates():
#     windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
#     for window in windows:
#         owner_name = window.get('kCGWindowOwnerName', '')
#         if app_name in owner_name:
#             window_rect = window.get('kCGWindowBounds', {})
#             # print("window_rect:{}".format(window_rect))
#             return window_rect
#     return None, None

import pygetwindow as gw


def get_window_coordinates():
    try:
        window = gw.getWindowsWithTitle(app_name)[0]
        return window.left, window.top, window.width, window.height
    except IndexError:
        return None




app_name = "MuMu模拟器12"
folder_name = "screenshots"
folder_path = "screenshots"


def get_screenshot_path():
    # Get the window with the title of your app
    app_left, app_top, app_width, app_height = get_window_coordinates()
    # Get the coordinates of the app window

    # Calculate the coordinates of the bottom right corner of the app window
    app_right = app_left + app_width
    app_bottom = app_top + app_height

    # Capture a screenshot of the app window
    app_screenshot = pyautogui.screenshot(region=(app_left, app_top, app_width, app_height))

    current_time = time.strftime("%Y%m%d-%H%M%S")
    path = os.path.join(folder_path, f"{current_time}_screenshot.png")

    app_screenshot.save(path)

    return path


# def get_screenshot_path():
#     # Get the window by its title
#     windows = CGWindowListCopyWindowInfo(
#         kCGWindowListOptionOnScreenOnly, kCGNullWindowID
#     )
#     for window in windows:
#         title = window.get('kCGWindowOwnerName', '')
#         if app_name in title:
#             window_id = window['kCGWindowNumber']
#             window_rect = window['kCGWindowBounds']
#
#             left = int(window_rect['X'])
#             top = int(window_rect['Y'])
#             width = int(window_rect['Width'])
#             height = int(window_rect['Height'])
#
#             right = left + width
#             bottom = top + height
#
#             # Capture the screenshot of the window using ImageGrab
#             screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
#
#             # Save or process the screenshot as needed
#             current_time = datetime.now()
#             # Format the current time as a string in "yyyymmdd-hhmmss" format
#             formatted_time = current_time.strftime("%Y%m%d-%H%M%S")
#             path = os.path.join(folder_name, f"{formatted_time}_screenshot.png")
#             screenshot.save(path)
#             return path


if __name__ == '__main__':
    # get_window_coordinates()
    get_screenshot_path()
