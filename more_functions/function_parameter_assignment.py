"""
Author: Brady Trenary

function takes in a string and a number, then multiplies the string by the number
"""


def multiply_string(message, n):
    result = message * n
    print(result)
    return result


if __name__ == '__main__':
    multiply_string('Chemistry', 5)

