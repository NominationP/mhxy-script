import pytesseract
from PIL import Image
import os

from ClickScreenshot import click_screenshot
from AnchorRecord import get_all_odds
from log.recordLog import log_not_found
from ocr.EasyOCR import recognize_chinese_text, get_read_text
from screenShot import get_screenshot_path


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

def check_text_in_read(text):
    picture_path = get_screenshot_path()
    read_text = get_read_text(picture_path)
    return recognize_chinese_text(read_text, text)


def get_coordinate(image_path):
    read_text = get_read_text(image_path)
    for odd in get_all_odds():
        is_find = None
        if isinstance(odd, str):
            is_find = recognize_chinese_text(read_text, odd)
        if is_find is not None:
            print("found {} in {} read_text:{}".format(is_find, image_path, read_text))
            return is_find
    print("not found in {} read_text: {} {}".format(image_path, read_text, get_all_odds()))
    log_not_found("not found in {} read_text: {} {}".format(image_path, read_text, get_all_odds()))
    return


# 基础测试: 截图,判断坐标,点击
def do_shot_get_coordinate_click() -> object:
    picture_path = get_screenshot_path()
    coordinate = get_coordinate(picture_path)

    if hasattr(coordinate, 'position') & hasattr(coordinate, 'text'):
        click_screenshot(coordinate.text, coordinate.position)
    if hasattr(coordinate, 'text'):
        # todo
        if coordinate.text == '副本己完咸':
            return "副本已完成"
        return coordinate.text
    return None


if __name__ == '__main__':
    do_shot_get_coordinate_click()
