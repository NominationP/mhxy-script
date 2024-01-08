import os
from datetime import datetime
import time
from PIL import ImageGrab
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
import Quartz

app_name = "网易MuMu"  # Specify the exact window title

# Create a folder named "screenshot" if it doesn't exist
folder_name = "screenshot"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


def get_window_coordinates():
    windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
    for window in windows:
        owner_name = window.get('kCGWindowOwnerName', '')
        if app_name in owner_name:
            window_rect = window.get('kCGWindowBounds', {})
            # print("window_rect:{}".format(window_rect))
            return window_rect
    return None, None


def get_screenshot_path():
    # Get the window by its title
    windows = CGWindowListCopyWindowInfo(
        kCGWindowListOptionOnScreenOnly, kCGNullWindowID
    )
    for window in windows:
        title = window.get('kCGWindowOwnerName', '')
        if app_name in title:
            window_id = window['kCGWindowNumber']
            window_rect = window['kCGWindowBounds']

            left = int(window_rect['X'])
            top = int(window_rect['Y'])
            width = int(window_rect['Width'])
            height = int(window_rect['Height'])

            right = left + width
            bottom = top + height

            # Capture the screenshot of the window using ImageGrab
            screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

            # Save or process the screenshot as needed
            current_time = datetime.now()
            # Format the current time as a string in "yyyymmdd-hhmmss" format
            formatted_time = current_time.strftime("%Y%m%d-%H%M%S")
            path = os.path.join(folder_name, f"{formatted_time}_screenshot.png")
            screenshot.save(path)
            return path


if __name__ == '__main__':
    # get_window_coordinates()
    get_screenshot_path()
