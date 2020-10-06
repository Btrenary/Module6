"""
Author: Brady Trenary
Program: validate_input_in_function.py


prompts user for name and score, prints values to console
"""
import unittest


def score_input(test_name, test_score = 0, invalid_message='Invalid test score, try again!'):
    """
    Function that accepts and returns a string....
    :param test_name: The name of a test/exam
    :type test_name: String
    :param test_score: A value between 0 and 100 representing a test score
    :type test_score: int
    :param invalid_message: Message displayed when an invalid score is provided
    :type invalid_message: String
    :return: formatted string with test and test score
    :rtype: String
    """
    if 0 <= test_score <= 100:
        # print(f"{test_name}: {test_score}")
        return f"{test_name}: {test_score}"
    else:
        return invalid_message

if __name__ == '__main__':
    unittest.main("test1", 45)