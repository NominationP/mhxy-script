import pyautogui
import random
import time
from screenShot import get_window_coordinates


def click_screenshot(text, app_coordinates):

    left_top_x, left_top_y = app_coordinates[0]
    right_down_x, right_down_y = app_coordinates[2]

    x, y, app_width, app_height = get_window_coordinates()
    print(x, y, app_width, app_height)

    # Calculate the range of x and y coordinates within the specified area

    x_range = (x + left_top_x, x + right_down_x)
    y_range = (y + left_top_y, y + right_down_y)
    print(x_range, y_range)

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
    click_screenshot_pair(("打开小地图", [[113, 66], [1, 2], [285, 149]]))
    # click_screenshot_pair(("百晓仙子", [[557, 517], [1, 2], [646, 531]]))
    click_screenshot_pair(("郑镖头", [[284, 495], [1, 2], [300, 509]]))
