#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/10 下午7:39
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
import os
import json
import collections
from functools import wraps

# users = dict(tom={'password': 'tom0PASS', 'mobile': '13000000001', 'balance': 5000, },
#                jerry={'password': 'jerry0PASS', 'mobile': '13000000002', 'balance': 5000, })

# 获取用户信息
def get_users(user_db_file):
    result = None
    try:
        with open(user_db_file, 'r') as data_file:
            result = json.load(data_file)
    except:
        # print('File error.')
        result = 'File error.'
    return result

user_db = get_users('user_db.json')
# print(user_db)

# 保存用户数据
def save_users(user_db_file: str = 'user_db.json', user_info = user_db):
    try:
        with open(user_db_file, 'w') as data:
            json.dump(user_info, data)
    except:
        print('File error.')

def get_cmd(fn):
    '''
    Get command.

    :param fn:
    :return:
    '''
    @wraps(fn)
    def wrapper(*args, **kwargs):
        '''
        wrapper function.

        :param args:
        :param kwargs:
        :return: command
        '''
        cmd_list = fn(*args, **kwargs)
        if not cmd_list:
            return 'Invalid argument.'
        cmd = str(input('Command: ')).lower()
        return cmd if cmd in cmd_list else 'Input Error!'
    return wrapper

# 打印功能菜单：
@get_cmd    # menus = get_cmd(menus)(menu_item) = wrapper(menu_item) = menus(menu_item)
def menus(menu_item):
    '''
    All menu

    :param menu_item: index, feature
    :return: command list for menu
    '''
    def feature_menu():
        '''
            Feature Menu

            :return:
            '''
        f_menu = collections.OrderedDict(
            dict(b='Balance inquiry(B)', d='Deposits(D)', r='Draw money(R)', t='Transfer(T)', s='Settings(S)',
                 o='Sign out(O)',
                 h='Help(H)'))
        menu_settings = collections.OrderedDict(dict(c='Change Password(C)', u='Delete account(D)'))
        print('{:=^30}'.format('Menu'))
        print('\n'.join(f_menu.values()))
        # print('\n'.join(menu_settings.values()))
        print('=' * 30)
        return f_menu.keys()

    # 获取一级菜单命令
    def index_menu():
        '''
            First menu

            :return: first menu command
            '''
        i_menu = collections.OrderedDict(dict(l='Login(L)', s='Sign in(S)', q='Quit(Q)'))
        print()
        print('\t'.join(i_menu.values()))
        return i_menu.keys()

    if menu_item == 'index':
        result = index_menu()
    elif menu_item == 'feature':
        result = feature_menu()
    else:
        return None
    return result


# 用户登录并认证
def login():
    '''
    完成用户认证：如果认证成功则返回用户名
    :return: username or None
    '''
    def auth_user(username, password, usdb=user_db):
        if username in usdb.keys():
            return True if password == usdb[username]['password'] else False
        else:
            res_mess = "Fileld: {} doesn't exist!".format(username)
            return False

    for i in range(3):
        current_user = input('Please enter your username: ')
        current_pass = getpass.getpass('Please enter your password: ')
        login_state = auth_user(current_user, current_pass)
        if login_state:  # 用户认证通过
            print('INFO: \n\t{} login Success!\n'.format(current_user))
            return current_user
        else:
            print('INFO: \n\tAccess denied. \n\t{} more chances!\n'.format(2 - i))
    else:
        print("Too many authentication failures.")


# 用户注册
def sign_in(usdb: dict = user_db) -> str:
    '''
    实现用户注册功能
    :param usdb:
    :return: 新用户名
    '''
    register_status = False
    while not register_status:  # 如果用户名重复刚重新输入
        username = input('Please input your name or "q" to Quit: ').lower()
        if username == 'q': return None
        if username in usdb.keys():  # 判断用是否已经存在
            print('{} exists!'.format(username))
        else:  # 用户名不重复
            while True:  # 输入合法信息
                pass1 = getpass.getpass('Please input your password: ')
                pass2 = getpass.getpass('Retype input password: ')
                if pass1 == pass2:
                    mobile = input('Please input your mobile: ')
                    new_user_info = {username: {'password': pass2, 'mobile': mobile, 'balance': 5000}}
                    usdb.update(new_user_info)
                    register_status = True
                    break
                else:
                    print('Different inputs!')

    return username

# 业务处理
def business_analyst():
    pass

# 主程序
# os.system('clear')
# print('\n' * 20, '{:^130s}'.format('Welcom to xxx ATM system.'), '\n' * 20)
while True:
    # cmd1 = get_first_command()
    cmd1 = menus('index')
    if cmd1 == 'l':  # 进入用户登陆界面
        user = login()
        cmd2 = menus('feature')
        print(cmd2)
    elif cmd1 == 's':  # 进入用户注册界面
        new_user = sign_in()
        if new_user in user_db.keys():
            print('{} Registered successfully!'.format(new_user))
            print(
                'Account Info: \n\tAccount: {user}\n\tMobile: {mobile}\n\tBalance: {balance:.2f} [USD]\n\n'.format(
                    user=new_user, mobile=user_db[new_user]['mobile'],
                    balance=user_db[new_user]['balance']))
        else:
            print('Registered failed!')
    elif cmd1 == 'q':  # 即出系统
        save_users()
        break
    else:
        print('Input Error!')


