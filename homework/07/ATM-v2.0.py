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
import re
import os
import json
import collections
from functools import wraps

# users = dict(tom={C:\Users\Yinkai\Projects\MyMiniProgrames\homework\07\ATM-v2.0.py: 'tom0PASS', 'mobile': '13000000001', 'balance': 5000, },
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

# 保存用户数据
def save_users(user_db_file: str = 'user_db.json', user_info = user_db):
    try:
        with open(user_db_file, 'w') as data:
            json.dump(user_info, data)
    except:
        print('File error.')

def error_mes(mes: str):
    return "\033[0;{c};40m{f}\033[0m{m}".format(c=31, f='Error: ', m=mes)

def normal_mes(mes: str):
    return "\033[0;{c};40m{f}\033[0m{m}".format(c=32, f='INFO: ', m=mes)

def get_mobile():   # 生成手机号码
    while True:
        mobile = input('Please input your mobile: ')
        if len(mobile) == 11 and re.match(r'1\d{10}', mobile):
            return mobile
        else:
            print(error_mes('Invalid input.'))

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
        if not cmd_list:    # 如果在调用menu函数时菜单实参选项输错，则返回None
            return cmd_list
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
    # 获取一级菜单命令
    def index_menu():
        '''
            First menu

            :return: first menu command
            '''
        i_menu = collections.OrderedDict(dict(i='Login(I)', s='Sign in(S)', q='Quit(Q)'))
        print()
        print('\t'.join(i_menu.values()))
        return i_menu.keys()

    def feature_menu():
        '''
            Feature Menu

            :return:
            '''
        f_menu = collections.OrderedDict(
            dict(b='Balance inquiry(B)', d='Deposits(D)', r='Draw money(R)', t='Transfer(T)', s='Settings(S)',
                 o='Sign out(O)'))
        print('\n{:=^30}'.format('Menu'))
        print('\n'.join(f_menu.values()))
        print('=' * 30)
        return f_menu.keys()

    def settings_menu():
        s_menu = collections.OrderedDict(dict(p='Show profile(P)', cp='Change Password(CP)', cm='Change Mobile(CM)', d='Delete account(D)', b='Back(B)'))
        print()
        print('\n'.join(s_menu.values()))
        return s_menu.keys()

    if menu_item == 'index':
        result = index_menu()
    elif menu_item == 'feature':
        result = feature_menu()
    elif menu_item == 'settings':
        result = settings_menu()
    else:
        result = None
    return result


# 用户登录并认证
def login():
    '''
    完成用户认证：如果认证成功则返回用户名
    :return: 登陆成功返回其用户名，否则返回None
    '''
    def auth_user(username, password, usdb=user_db):
        if username in usdb.keys():
            return True if password == usdb[username]['password'] else False
        else:
            return False

    for i in range(3):
        current_user = input('Please enter your username: ')
        current_pass = getpass.getpass('Please enter your password: ')
        login_state = auth_user(current_user, current_pass)
        if login_state:  # 用户认证通过
            print(normal_mes('\n\t{} login Success!\n'.format(current_user)))
            return current_user
        else:
            print(error_mes('\n\tAccess denied. \n\t{} more chances!\n'.format(2 - i)))
    else:
        print(error_mes("Too many authentication failures."))


# 用户注册
def sign_in(usdb: dict = user_db) -> str:
    '''
    实现用户注册功能
    :param usdb:
    :return: 新用户名
    '''
    register_status = False
    while not register_status:  # 如果用户名重复刚重新输入
        while True:     # 检查用户名是否合法
            username = input('Please input your name or "q" to Quit: ').lower()
            if username == 'q': return None
            if re.match(r'^\w{3,10}$', username):
                # 用户名规则：
                # 1. 可以包含字母、数字，不能包含特殊字符
                # 2. 三至十位
                break
            else:
                print(error_mes("The user name does not follow the rules."))
        if username in usdb.keys():  # 判断用是否已经存在
            print('{} exists!'.format(username))
        else:  # 用户名不重复
            while True:  # 输入合法信息
                pass1 = getpass.getpass('Please input your password: ')
                pass2 = getpass.getpass('Retype input password: ')
                if pass1 == pass2:
                    mobile = get_mobile()
                    new_user_info = {username: {'password': pass2, 'mobile': mobile, 'balance': 5000}}
                    usdb.update(new_user_info)
                    register_status = True
                    break
                else:
                    print(error_mes('Different inputs!'))

    return username


# 业务功能
def business_features(current_user, feature_cmd: str = None):
    cmd = str(feature_cmd).lower()
    if cmd == 'b':  # 查询余额
        print(normal_mes('\n\tBalance: {:.2f} [USD]\n'.format(user_db[current_user]['balance'])))
    elif cmd == 'd':    # 存款
        try:
            deposit = abs(int(input('Amount of deposit: ')))
            pre = user_db[current_user]['balance']
            user_db[current_user]['balance'] += deposit
            if user_db[current_user]['balance'] == pre + deposit:
                print(normal_mes('\n\tExecute completes. \n\tThe current balance: {:.2f} [USD]\n'.format(
                user_db[current_user]['balance'])))
            else:
                print(error_mes('Execute failed.'))
        except:
            print(error_mes('Invalid input!'))
    elif cmd == 'r':    # 取款
        try:
            cash = abs(int(input('Withdrawal amount: ')))
            pre = user_db[current_user]['balance']
            user_db[current_user]['balance'] -= cash
            if user_db[current_user]['balance'] == pre - cash:
                print(normal_mes('\n\tExecute completes. \n\tThe current balance: {:.2f} [USD]\n'.format(
                user_db[current_user]['balance'])))
            else:
                print(error_mes('Execute failed.'))
        except:
            print(error_mes('Invalid input!'))
    elif cmd == 't':    # 转账
        receiver = input('Receiver: ')
        try:
            amount = abs(int(input('Amount: ')))
        except:
            print(error_mes('Invalid input!'))
            return
        if receiver in user_db.keys():
            receiver_pre = user_db[receiver]['balance']
            sender_pre = user_db[current_user]['balance']
            user_db[receiver]['balance'] += amount
            user_db[current_user]['balance'] -= amount
            if user_db[receiver]['balance'] == receiver_pre + amount and user_db[current_user]['balance'] - amount:
                print(normal_mes('\n\tTransfer to complete!\n\tThe current balance: {:.2f} [USD]\n'.format(user_db[current_user]['balance'])))
            else:
                print(error_mes('\n\tExecute failed.'))
        else:  # 收款人不存在
            print(error_mes('\n\tReceiver dose not exist.\n'))
    elif cmd == 's':    # 设置
        while True:
            set_cmd = menus('settings')
            if set_cmd == 'cp':  # 修改密码
                current_pass = getpass.getpass('Please enter your current password: ')
                if current_pass == user_db[current_user]['password']:
                    for _ in range(3):
                        new_pass1 = getpass.getpass('New password: ')
                        new_pass2 = getpass.getpass('Retype new password: ')
                        if new_pass1 == new_pass2:
                            user_db[current_user]['password'] = new_pass2
                            if user_db[current_user]['password'] == new_pass2:
                                print(normal_mes('Password changed successfully.'))
                                break
                            else:
                                print(error_mes('System Error! Password change failed.'))
                                break
                        else:
                            print(error_mes('Sorry, passwords do not match.'))
                    else:
                        print(error_mes("Too many authentication failures."))
                else:
                    print(error_mes('Authentication password manipulation error.'))

            elif set_cmd == 'cm':   # 修改手机号吗
                new_mobile = get_mobile()
                user_db[current_user]['mobile'] = new_mobile
                if user_db[current_user]['mobile'] == new_mobile:
                    print(normal_mes('Mobile modified successfully.'))
                    continue
                else:
                    print('\033[0;31;40mInfo: System Error! Mobile modification failed.\033[0m')
                    continue
            elif set_cmd == 'd':    # 删除账户
                password = getpass.getpass('Please enter your password: ')
                if password == user_db[current_user]['password']:
                    del_cmd = str(input('Are you sure you want to delete your account? (y/N) :')).lower()
                    if del_cmd == 'y':
                        user_db.pop(current_user)
                        if not user_db.get(current_user):   # 确认用户账号删除成功
                            print(normal_mes('{} deleted successfully'.format(current_user)))
                            return True
                        else:
                            print(error_mes('System Error! Delete failed.'))
                else:
                    print(error_mes("Authentication failed! "))
            elif set_cmd == 'p':    # 列出用户信息
                print(normal_mes('\n\tUsername: {username}\n\tMobile: {mobile}'.format(username = current_user, mobile = user_db[current_user]['mobile'])))
            elif set_cmd == 'b':    # 返回
                return
            else:
                print(error_mes('Invalid Input.'))
    else:
        return

# 主程序
os.system('clear')
print('\n' * 20, '{:^130s}'.format('Welcom to xxx ATM system.'), '\n' * 20)
while True:
    cmd1 = menus('index')
    if cmd1 == 'i':  # 进入用户登陆界面
        logout_flag = False
        current_user = login()
        if current_user:    # 用户登陆成功
            while True:
                cmd2 = menus('feature')     # 打印功能菜单并获取用户命令
                if cmd2 == 'b':     # 查询余额
                    business_features(current_user, cmd2)
                    continue
                elif cmd2 == 'd':   # 存款
                    business_features(current_user, cmd2)
                    continue
                elif cmd2 == 'r':   # 取款
                    business_features(current_user, cmd2)
                    continue
                elif cmd2 == 't':   # 转账
                    business_features(current_user, cmd2)
                    continue
                elif cmd2 == 's':   # 设置
                    logout_flag = business_features(current_user, cmd2)
                    if logout_flag:
                        break
                    continue
                elif cmd2 == 'o':
                    break
                else:
                    print(error_mes('Invalid input'))

    elif cmd1 == 's':  # 进入用户注册界面
        new_user = sign_in()
        if new_user in user_db.keys():
            print(normal_mes('{} Registered successfully!'.format(new_user)))
            print(
                'Account Info: \n\tAccount: {user}\n\tMobile: {mobile}\n\tBalance: {balance:.2f} [USD]\n\n'.format(
                    user=new_user, mobile=user_db[new_user]['mobile'],
                    balance=user_db[new_user]['balance']))
        else:
            print(normal_mes('Registered failed!'))
    elif cmd1 == 'q':  # 即出系统
        save_users()
        break
    elif not cmd1:  # 如果在调用menu函数时菜单实参选项输错，则直接退出程序
        print(error_mes('Invalid argument.'))
        break
    else:
        print(error_mes('Input Error!'))


