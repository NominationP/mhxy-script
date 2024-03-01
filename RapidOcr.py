from rapidocr_onnxruntime import RapidOCR



engine = RapidOCR()

# img_path = 'screenshots/20240112-101403_screenshot.png'
img_path = 'screenshots/20240112-121025_screenshot.png'
result, elapse = engine(img_path)
print(result)

# 默认都为True
# result, elapse = engine(img_path, use_det=True, use_cls=True, use_rec=True)
# print(result)
# print(elapse)


# result, elapse = engine(img_path, use_det=False, use_cls=False, use_rec=True)
# print(result)
# print(elapse)