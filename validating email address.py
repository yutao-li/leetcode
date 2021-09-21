import re


def f1(s: str):
    return re.match('[a-z]{1,6}_?([0-9]{0,4})@hackerrank\.com', s)


