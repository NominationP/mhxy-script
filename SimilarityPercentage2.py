import cv2


class CompareImage(object):

    def __init__(self, image_1_path, image_2_path, region_1, region_2, width, height):
        self.minimum_commutative_image_diff = 1
        self.image_1_path = image_1_path
        self.image_2_path = image_2_path
        self.region_1 = region_1
        self.region_2 = region_2
        self.width = width
        self.height = height

    def compare_image(self):
        image_1 = cv2.imread(self.image_1_path, 0)
        image_2 = cv2.imread(self.image_2_path, 0)

        # Extract regions of interest from the images
        roi_1 = image_1[self.region_1[1]:self.region_1[1] + self.height, self.region_1[0]:self.region_1[0] + self.width]
        roi_2 = image_2[self.region_2[1]:self.region_2[1] + self.height, self.region_2[0]:self.region_2[0] + self.width]

        commutative_image_diff = self.get_image_difference(roi_1, roi_2)

        if commutative_image_diff < self.minimum_commutative_image_diff:
            print("Matched")
            return commutative_image_diff
        return 10000

    @staticmethod
    def get_image_difference(roi_1, roi_2):
        img_hist_diff = cv2.compareHist(cv2.calcHist([roi_1], [0], None, [256], [0, 256]),
                                        cv2.calcHist([roi_2], [0], None, [256], [0, 256]),
                                        cv2.HISTCMP_BHATTACHARYYA)

        result = cv2.matchTemplate(roi_1, roi_2, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, _, _ = cv2.minMaxLoc(result)
        img_template_diff = 1 - max_val

        # taking only 10% of histogram diff, since it's less accurate than template method
        commutative_image_diff = (img_hist_diff / 10) + img_template_diff
        return commutative_image_diff


if __name__ == '__main__':
    # Define the regions of interest and their dimensions
    region_1 = (676, 108)  # (x, y) coordinates of the top-left corner of the first ROI
    #           848,446
    region_2 = (676, 108)  # (x, y) coordinates of the top-left corner of the second ROI
    width = 172  # Width of the ROI
    height = 338  # Height of the ROI

    compare_image = CompareImage('screenshot/20231224-114031_screenshot.png',
                                 'screenshot/20231226-105428_screenshot.png',
                                 region_1, region_2, width, height)
    image_difference = compare_image.compare_image()
    print(image_difference)

    # Other comparisons...
