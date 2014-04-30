__author__ = 'wybe'


def log(message):
    with open("log.txt", 'w') as f:
        f.write(message)

    return