from difflib import SequenceMatcher
import easyocr
from PIL import Image
import ssl

from AnchorRecord import get_all_odds, fuzzy_match_def
from log.recordLog import log_not_found

ssl._create_default_https_context = ssl._create_unverified_context


def get_read_text(image_path):
    # Initialize the OCR reader with Chinese language setting
    reader = easyocr.Reader(['ch_sim', 'en'])
    # Perform OCR on the image
    result = reader.readtext(image_path)
    # print("result:{}".format(result))
    return result


class TargetInfo:
    def __init__(self, text, position):
        self.text = text
        self.position = position

    def __str__(self):
        return f"Text: {self.text}, Position: {self.position}"


def start_with_compare(target_text, text):
    # Truncate strings to match length for comparison
    length = min(len(target_text), len(text))
    target_truncated = target_text[:length]
    text_truncated = text[:length]

    # Check if the truncated target_text starts with the truncated text
    result = target_truncated.startswith(text_truncated)

    return result


def recognize_chinese_text(read_result, target_text):
    # Check for the target text within the OCR results
    target_text = target_text.strip()
    for detection in read_result:
        text = detection[1].strip()

        similarity_ratio = SequenceMatcher(None, target_text, text).ratio()
        # print("target_text:{}, text:{}, target_text in text:{}".format(target_text, text,target_text in text))
        if text:
            fuzzy_result = fuzzy_match_def(text)
            if fuzzy_result:
                return TargetInfo(fuzzy_result, detection[0])

        if text and ((target_text in text) or similarity_ratio >= 0.8):  # Adjust the threshold as needed
            return TargetInfo(target_text, detection[0])
    return None


if __name__ == '__main__':
    # Call the function
    image_path_main = (
        '/Users/yibo/Documents/python/projects/pythonProject1/screenshot/20231224-120225_screenshot.png')

    read_text_main = get_read_text(image_path_main)
    for odd in get_all_odds():
        is_find = recognize_chinese_text(read_text_main, odd)
        if is_find is not None:
            print("found {} in {} read_text:{}".format(is_find, image_path_main, read_text_main))
            exit()
    print("not found in {} read_text: {} {}".format(image_path_main, read_text_main, get_all_odds()))
    log_not_found("not found in {} read_text: {} {}".format(image_path_main, read_text_main, get_all_odds()))

# [([[45, 3], [75, 3], [75, 17], [45, 17]], '』:}9', 0.003100337227806449), ([[69, 19], [109, 19], [109, 39], [69, 39]], '长安域', 0.03384565668684891), ([[43, 41], [123, 41], [123, 61], [43, 61]], '[时 (9,103)', 0.13424944213783815), ([[265, 59], [299, 59], [299, 79], [265, 79]], '9点', 0.5808349065185165), ([[59, 111], [91, 111], [91, 129], [59, 129]], '5节', 0.0033887174637315877), ([[49, 131], [97, 131], [97, 147], [49, 147]], '16:21:03', 0.5008950458046337), ([[502, 132], [630, 132], [630, 158], [502, 158]], '主线 回溯 |遵遇 ', 0.0032586928989292293), ([[503, 161], [627, 161], [627, 181], [503, 181]], '凛骨长老的绝技(建议组', 0.05404923656411737), ([[501, 179], [525, 179], [525, 197], [501, 197]], '叭', 0.0392928578087981), ([[502, 210], [604, 210], [604, 234], [502, 234]], '日常-捉鬼(1/10)', 0.19136895492393957), ([[503, 237], [611, 237], [611, 257], [503, 257]], '捉掌夷时二刻捣大鬼', 0.0031722246848463276), ([[120, 254], [170, 254], [170, 278], [120, 278]], ']夜/', 0.0027204037988239997), ([[110, 272], [172, 272], [172, 296], [110, 296]], 'Uuir奶', 0.005811449154073667), ([[222, 262], [290, 262], [290, 290], [222, 290]], '%鬼酶', 0.0020849864090450804), ([[502, 282], [628, 282], [628, 306], [502, 306]], '考古-古董鉴赏(5/20)', 0.9234596731543622), ([[504, 308], [622, 308], [622, 332], [504, 332]], '与银瓶痂媳探讨古-收', 0.0001352789668523737), ([[503, 361], [559, 361], [559, 381], [503, 381]], '袖粤领悟', 0.05529218167066574), ([[227, 391], [255, 391], [255, 411], [227, 411]], '钾宦', 0.0005242153455483802), ([[225, 443], [265, 443], [265, 463], [225, 463]], '网萧萧', 0.0106300364540474), ([[273, 443], [305, 443], [305, 463], [273, 463]], 'S', 0.02437096130458727), ([[202, 558], [566, 558], [566, 586], [202, 586]], '听闻寅时二刻捣大鬼又跑出去了 ,少侠帮我捉回来吧。', 0.5208306672890611), ([[90, 600], [126, 600], [126, 624], [90, 624]], '钟馗', 0.9826524228817768)]
