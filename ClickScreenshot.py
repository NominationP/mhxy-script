import pyautogui
import random
import time
from screenShot import get_window_coordinates


def click_screenshot(text, app_coordinates):
    # Define the dimensions of the app window
    app_width = 480  # Width of the app window
    app_height = 568  # Height of the app window

    window_rect = get_window_coordinates()
    # Define the position of the app window within the display
    app_x = window_rect["X"]  # X-coordinate of the app window
    app_y = window_rect["Y"]  # Y-coordinate of the app window

    # Calculate the range of x and y coordinates within the specified area
    x_range = (app_x + app_coordinates[0][0], app_x + app_coordinates[1][0])
    y_range = (app_y + app_coordinates[0][1], app_y + app_coordinates[1][1])

    # Generate random coordinates within the specified area
    random_x = random.randint(x_range[0], x_range[1])
    random_y = random.randint(y_range[0], y_range[1])

    print("text:{} app_coordinates:{} random_xy:{},{}".format(text, app_coordinates, random_x, random_y))
    # Click on a random coordinate within the specified area
    time.sleep(0.8)
    pyautogui.click(random_x, random_y)

    # 多点一次
    if text in ("日常-捉鬼", "曰常-捉鬼", "曰常-捉鬼","日常-宝图任务"):
        time.sleep(0.8)
        pyautogui.click(random_x, random_y)


def click_screenshot_pair(pair):
    click_screenshot(pair[0], pair[1])


if __name__ == '__main__':
    # click_screenshot("快速应战", [[631, 385], [0, 0], [813, 415], [676, 240]])
    click_screenshot_pair(("打开小地图", [[61, 56], [1, 2], [139, 80]]))
    click_screenshot_pair(("百晓仙子", [[295, 294], [1, 2], [330, 297]]))
