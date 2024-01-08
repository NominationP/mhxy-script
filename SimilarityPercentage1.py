import cv2
import os
from PIL import Image


class CompareImage(object):

    def __init__(self, image_1_path, image_2_path):
        self.minimum_commutative_image_diff = 1
        self.image_1_path = image_1_path
        self.image_2_path = image_2_path

    def compare_image(self):
        image_1 = cv2.imread(self.image_1_path, 0)
        image_2 = cv2.imread(self.image_2_path, 0)
        commutative_image_diff = self.get_image_difference(image_1, image_2)

        if commutative_image_diff < self.minimum_commutative_image_diff:
            # print("Matched")
            return commutative_image_diff
        return 10000

    @staticmethod
    def get_image_difference(image_1, image_2):
        first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
        second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

        img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
        img_template_probability_match = \
        cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
        img_template_diff = 1 - img_template_probability_match

        # taking only 10% of histogram diff, since it's less accurate than template method
        commutative_image_diff = (img_hist_diff / 10) + img_template_diff
        return commutative_image_diff


if __name__ == '__main__':
    compare_image = CompareImage('screenshot/20231229-110210_screenshot.png',
                                 'screenshot/20231229-110129_screenshot.png')
    image_difference = compare_image.compare_image()
    print(image_difference)

    compare_image = CompareImage('screenshot/20231229-110129_screenshot.png',
                                 'screenshot/20231229-110129_screenshot.png')
    image_difference = compare_image.compare_image()
    print(image_difference)

    compare_image = CompareImage('screenshot/20231228-093656_screenshot.png',
                                 'screenshot/20231226-100827_screenshot.png')
    image_difference = compare_image.compare_image()
    print(image_difference)

    # Directory path containing the images
    folder_path = 'screenshot/'

    results = {}  # Dictionary to store filename and difference
    # Loop through all files in the directory
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        compare_image = CompareImage('screenshot/20231228-093656_screenshot.png',
                                     filepath)
        image_difference = compare_image.compare_image()
        results[filename] = image_difference

    # Sort the results by image_difference in ascending order
    sorted_results = sorted(results.items(), key=lambda x: x[1])

    # Print sorted results
    for filename, difference in sorted_results:
        print(f"Filename: {filename}, Difference: {difference}")

