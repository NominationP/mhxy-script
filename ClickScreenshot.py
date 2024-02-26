import pyautogui
pyautogui.FAILSAFE = False
import random
import time

from AnchorRecord import get_certain_coordinate
from screenShot import get_window_coordinates


def is_within_area(a, b):
    if a is None or b is None:
        return False
    # Extract coordinates for a and b
    a_coords = a
    b_coords = b

    # Get the minimum and maximum values for each axis for rectangle a
    min_x_a = min(a_coords[0][0], a_coords[1][0])
    max_x_a = max(a_coords[0][0], a_coords[1][0])
    min_y_a = min(a_coords[0][1], a_coords[1][1])
    max_y_a = max(a_coords[0][1], a_coords[1][1])

    # Get the minimum and maximum values for each axis for rectangle b
    min_x_b = min(b_coords[0][0], b_coords[1][0])
    max_x_b = max(b_coords[0][0], b_coords[1][0])
    min_y_b = min(b_coords[0][1], b_coords[1][1])
    max_y_b = max(b_coords[0][1], b_coords[1][1])

    # Check if all four corners of rectangle a are within rectangle b
    if min_x_b <= min_x_a <= max_x_b and min_y_b <= min_y_a <= max_y_b and \
            min_x_b <= max_x_a <= max_x_b and min_y_b <= max_y_a <= max_y_b:
        return True
    else:
        return False


def click_screenshot(text, app_coordinates):
    t, coordinate = get_certain_coordinate("点击禁区")
    if is_within_area(app_coordinates, coordinate):
        print("not click ! app_coordinates {} is in area of coordinate {}".format(app_coordinates, coordinate))
        return

    left_top_x, left_top_y = app_coordinates[0]
    right_down_x, right_down_y = app_coordinates[1]

    x, y, app_width, app_height = get_window_coordinates()

    # Calculate the range of x and y coordinates within the specified area

    x_range = (x + left_top_x, x + right_down_x)
    y_range = (y + left_top_y, y + right_down_y)

    # Generate random coordinates within the specified area
    random_x = random.randint(x_range[0], x_range[1])
    random_y = random.randint(y_range[0], y_range[1])

    print("text:{} app_coordinates:{} random_xy:{},{}".format(text, app_coordinates, random_x, random_y))
    # Click on a random coordinate within the specified area
    time.sleep(0.8)
    pyautogui.click(random_x, random_y)

    # 多点一次
    if text in ("日常-捉鬼", "曰常-捉鬼", "曰常-捉鬼", "日常-宝图任务"):
        time.sleep(0.8)
        pyautogui.click(random_x, random_y)


def click_screenshot_pair(pair):
    click_screenshot(pair[0], pair[1])


if __name__ == '__main__':
    # click_screenshot("快速应战", [[631, 385], [0, 0], [813, 415], [676, 240]])
    click_screenshot_pair(("打开小地图", [[113, 66], [1, 2], [285, 149]]))
    # click_screenshot_pair(("百晓仙子", [[557, 517], [1, 2], [646, 531]]))
    click_screenshot_pair(("郑镖头", [[284, 495], [1, 2], [300, 509]]))
