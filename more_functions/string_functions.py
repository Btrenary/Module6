"""
Author: Brady Trenary

Program accepts string and number, then multiplies string by the number.
"""


def multiply_string(message, n):
    """
    :param message: string
    :param n: int
    :return: string
    """
    result = message * n
    print(result)
    return result


if __name__ == '__main__':
    multiply_string('Brady', 5)
