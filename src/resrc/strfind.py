#-*- coding: utf-8 -*-
import re


def find_str(str_param, str_src):
    res = re.findall(str_param, str_src)
    return res


def upperlowser_change(matched):
    char = matched.group()
    if char.isupper():
        return char.lower()
    else:
        return char.upper()


def main():
    print '\n'

############### EASY ##############

    # 1.查找 asdfjvjadsffvaadfkfasaffdsasdffadsafafsafdadsfaafd,该字符串中有多少个af
    str1 = r"asdfjvjadsffvaadfkfasaffdsasdffadsafafsafdadsfaafd"
    print len(find_str(r"af", str1))
    print '\n'

    # 2.输入任意一个字符串，如：“abDEe23dJfd343dPOddfe4CdD5ccv!23rr”。
    # 取出该字符串中所有的字母。顺序不能改变！并把大写字母变成小写，小写字母变成大写！
    str2 = r"abDEe23dJfd343dPOddfe4CdD5ccv!23rr"
    str2char = re.sub(r'[^a-zA-Z]', '', str2)
    print 'filter1 ', str2char
    print 'filter2 ', re.sub(r'[a-z]|[A-Z]', upperlowser_change, str2char)
    print '\n'

    # 3.匹配电话号码
    str3 = '18610003225'
    if re.match(r'^[0-9]{11}$', str3):
        print 'is phone number'
    else:
        print 'is not phone number'



