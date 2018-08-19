import re


def find_str(str_param, str_src):
    res = re.findall(str_param, str_src)
    print res
    return res


def main():
    str1 = r"test 009 -- 901, 0.1, 11, 212"
    find_str(r"\d+", str1)


