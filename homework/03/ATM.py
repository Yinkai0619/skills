#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/6/22 下午7:39
'''

'''
通过Python编程完成一个银行ATM机模拟系统，具备如下功能:
    (1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
    (2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
    (3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
    (4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
    (5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
'''
import getpass


def auth_user(username, password):
    # 认证用户及其密码

    users = dict(tom='tom0PASS', jerry='jerry0PASS')
    result = False
    res_mess = None

    if username in users.keys():
        if password == users[username]:
            result = True
            res_mess = '{} login Success'.format(username)
        else:
            res_mess = 'Password error!'
    else:
        res_mess = "Fileld: {} doesn't exist!".format(username)

    return result, res_mess


# (1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
for i in range(3):
    username = input('Please enter your username: ')
    password = getpass.getpass('Please enter your password: ')
    res, res_mess = auth_user(username, password)
    if res:  # 用户认证通过
        print(res_mess)
        break
    else:
        print(res_mess, '\n', '{} more chances!'.format(2 - i))

else:
    print('Error too much!')
