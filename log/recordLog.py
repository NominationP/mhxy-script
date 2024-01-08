import os


def log_not_found(string):
    # Append text to the file
    file_path = os.path.join("/Users/yibo/Documents/python/projects/pythonProject1/log/", "NotFoundRecord.txt")
    with open(file_path, "a") as file:
        file.write(string + "\n")


if __name__ == '__main__':
    log_not_found("test")
    log_not_found("test")
    log_not_found("not found in {} read_text: {} {}")
