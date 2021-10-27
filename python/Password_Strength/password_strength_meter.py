#!/usr/bin/env python

import re

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/10/20 下午9:34
'''

'''
密码强度检测，给定一个密码判断密码强度，强度共分三级。

密码要求：
    必须由10-15位指定字符组成:
        十进制数字
        大写字母
        小写字母
        特殊字符（如: !@#$%^&*-_）

强度规定：
    强（Strong）: 符合所有组合规则， 例如: Aatb32_67mnq,其中包含大写字母、小写字母、数字和特殊字符,是合格的强密码。
    适中（Moderate）： 符合三种组合规则
    弱（Weak）： 符合两种及以下组合规则
'''


def strength_check(password : str) -> str:
    '''
    检查密码强度
    :param password:
    :return: 当密码合法时，返回密码强度，否则返回“Invalid Password”
    '''

    # 检查密码长度
    def length_check(password = password, low = 10, upper = 15) -> bool:
        '''
        密码长度检查
        :param password:
        :param low: 密码位数下限
        :param upper: 密码位数上限
        :return: 密码位数合法时返回： Ture, 否则返回：False
        '''
        return True if low <= len(password) <= upper else False

    # 检查是否有非法字符
    def illegal_check(password : str = password) -> bool:
        '''
        非法字符检查
        :param password:
        :return: 没有非法字符时返回：True，否则返回：False
        '''
        # 生成特殊字符
        # special = {chr(x) for x in range(33, 39)} | {chr(x) for x in range(63, 65)}
        # special.update('*+-_'); special.discard('"')
        # special_characters = ''
        # for s in special:
        #     special_characters += s
        # print(special_characters)

        regex = re.compile('[^a-zA-Z\d!%&#\-@_?*$+]+', re.S)
        # regex = re.compile('[^a-zA-Z\d]+', re.S)
        illegal_characters = regex.findall(password)
        # print(illegal_characters)
        return False if illegal_characters else True

    # 检查字符组合
    def get_grade(password = password) -> int:
        '''
        返回给定密码的组合数量
        :param password:
        :return: 返回密码的组合数量，0～4，0为没有合法字符
        '''
        grade = 0
        upper_regex = re.compile('[A-Z]+', re.S)
        lower_regex = re.compile('[a-z]+', re.S)
        num_regex = re.compile('\d+', re.S)
        special_regex = re.compile('[!%&#\-@_?*$+]+', re.S)

        if special_regex.findall(password): grade += 1
        if num_regex.findall(password): grade += 1
        if upper_regex.findall(password): grade += 1
        if lower_regex.findall(password): grade += 1

        return grade

    if length_check(password) and illegal_check(password):
        grade = get_grade(password)
        if grade == 1: result = 'Weak'
        elif grade == 2 or grade == 3: result = 'Moderate'
        else: result = 'Strong'
        return 'Password Strength: {}'.format(result)
    else:
        return 'Invalid Password!'

if __name__ == '__main__':
    password1 = r'AbCd@135246_'
    password2 = r'AbCa@5,'
    password3 = r'A'
    password4 = r''
    print(strength_check(password4))
