import time
import random

from AnchorRecord import click_sorted, certain_coordinate, next_is_down, anchors_time, remove_certain_value, \
    next_is_certain, anchors_check_then
from ClickScreenshot import click_screenshot
from main import do_shot_get_coordinate_click, check_text_in_read

flag = "副本已完成"  # Define the flag to check for after encountering "..."


def find_coordinates(target):
    for item in certain_coordinate:
        if item[0] == target:
            return item[1]
    return None


def random_sleep_less():
    sleep_duration = random.uniform(1, 1.5)  # Generate a random float between 1 and 5
    time.sleep(sleep_duration)


def random_sleep():
    sleep_duration = random.uniform(1, 5)  # Generate a random float between 1 and 5
    time.sleep(sleep_duration)


def sleep_certain_seconds(second):
    time.sleep(second)


current_task_name = None


def do_online():
    global current_task_name
    for task, sublist in click_sorted:
        current_task_name = task
        # for index, certain_coordinate_key in enumerate(sublist):
        index = 0
        while index < len(sublist):
            certain_coordinate_key = sublist[index]
            print("task:{} certain_coordinate_key:{}".format(task, certain_coordinate_key))
            if certain_coordinate_key == "...":
                while True:
                    click_text = do_shot_get_coordinate_click()
                    random_sleep()
                    if click_text == "副本已完成":  # 副本已完成 / 捉完一轮鬼
                        index += 1
                        break
                    elif click_text == "少侠已经捉完1轮鬼。是否继续捉鬼?":
                        click_screenshot("确认捉鬼", find_coordinates("确认捉鬼"))
                        index += 2
                        break
                    elif click_text in next_is_down:
                        if click_text in anchors_time:
                            sleep_certain_seconds(anchors_time[click_text])
                        click_screenshot("快速应战", find_coordinates("快速应战"))
                        break
                    elif click_text in next_is_certain:
                        random_sleep_less()
                        click_screenshot("确定", find_coordinates("确定"))
                    elif click_text == "通关":
                        index += 1
                        break

                    # elif click_text in anchors_time:
                    #     anchors_time[click_text] -= 1
                    #     random_sleep_less()
                    #     click_screenshot("确定", find_coordinates("确定"))
                    #
                    #     if anchors_time[click_text] == 0:
                    #         remove_certain_value(click_text)
                    #         remove_certain_anchors_time(click_text)
                    #     break

            elif isinstance(certain_coordinate_key, (int, float)):
                sleep_certain_seconds(certain_coordinate_key)
                index += 1
            elif certain_coordinate_key in anchors_check_then:
                check_text = check_text_in_read(certain_coordinate_key)
                if check_text:
                    print("check_text_in_read:{}".format(check_text))
                    random_sleep_less()
                    click_screenshot(certain_coordinate_key, find_coordinates(sublist[index]))
                    index += 1
            else:
                print("index:{}".format(index))
                click_screenshot(certain_coordinate_key, find_coordinates(sublist[index]))
                index += 1
                time.sleep(3)

        print("DONE task:{}".format(task))


if __name__ == '__main__':
    do_online()
