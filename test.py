anchors_check_then = [
    "押送普通镖银",
    "押送高级镖银(有难度)",
]

certain_coordinate_key = "押送高级镖银(有难度)"

if certain_coordinate_key in anchors_check_then:
    print(False)  # If the key exists in the list, it will not print this statement
else:
    print(True)  # If the key doesn't exist in the list, it will print this statement

p = certain_coordinate_key in anchors_check_then

print(p)