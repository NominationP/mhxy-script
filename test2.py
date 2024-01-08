target_text = "日常-捉鬼"
text = "日常-捉鬼(1/10)"

if target_text.startswith(text[:4]):
    print("target_text starts with the first four characters of text")
else:
    print("target_text does not start with the first four characters of text")


if text.startswith(target_text[:4]):
    print("target_text starts with the first four characters of text")
else:
    print("target_text does not start with the first four characters of text")