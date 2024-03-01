import time
import random

from AnchorRecord import next_is_down, anchors_time, anchors_check_then, custom_operate, get_certain_coordinate, certain_coordinate_windows, model_type,model_type_instance, click_sorted_update
from ClickScreenshot import click_screenshot, click_screenshot_pair
from main import do_shot_get_coordinate_click, check_text_in_read

flag = "副本已完成"  # Define the flag to check for after encountering "..."


def find_coordinates(target):
    if target in certain_coordinate_windows:
        return certain_coordinate_windows.get(target)
    return None


def random_sleep_less():
    sleep_duration = random.uniform(0.100, 0.350)  # Generate a random float between 1 and 5
    time.sleep(sleep_duration)


def random_sleep_less_less():
    sleep_duration = random.uniform(0.3, 1.2)  # Generate a random float between 1 and 5
    time.sleep(sleep_duration)


def random_sleep():
    sleep_duration = random.uniform(1, 5)  # Generate a random float between 1 and 5
    time.sleep(sleep_duration)


def sleep_certain_seconds(second):
    time.sleep(second)


current_task_name = None


def do_online():
    global current_task_name
    for task_name in model_type.get(model_type_instance):
        sublist = click_sorted_update.get(task_name)
        do_process(sublist, task_name)
        print("DONE task:{}".format(task_name))

    # for task, sublist in click_sorted:
    #     do_process(sublist, task)


def do_process(sublist, task):
    global current_task_name
    current_task_name = task
    # for index, certain_coordinate_key in enumerate(sublist):
    index = 0
    while index < len(sublist):
        random_sleep_less()
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
                elif click_text == "通关":
                    index += 1
                    break
                elif click_text in custom_operate:
                    for op in custom_operate.get(click_text):
                        if isinstance(click_text, (int, float)):
                            sleep_certain_seconds(click_text)
                        else:
                            click_screenshot_pair(get_certain_coordinate(op))
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
                random_sleep_less()
                click_screenshot("确定", find_coordinates("确定"))
                index += 1
            else:
                break
        else:
            print("index:{}".format(index))
            click_screenshot(certain_coordinate_key, find_coordinates(sublist[index]))
            index += 1
            time.sleep(3)


if __name__ == '__main__':
    do_online()
