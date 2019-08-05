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


# 打印菜单：
def print_menu():   # TODO: Undone
    # 菜单功能：
    #     B: 查询余额
    #     D: 存款
    #     R: 取款
    #     T: 转账
    #     S: 设置
    #       C: 修改密码
    #       U: 注销账号
    #     O: 退出
    # menu = '\n\n|{:-^30s}|\n{:s}\n{:s}\n{:s}\n{:s}\n{:s}\n{:s}\n{:s}\n'.format('MENU', 'Query Balance(B)', 'Deposits(D)',
    #                                                                        'Draw money(R)', 'Transfer(T)',
    #                                                                        'Change Password(C)', 'Quit(Q)', 'Delete account(D)', 'Help(H)')
    menu = collections.OrderedDict(dict(b='Balance inquiry(B)',  d='Deposits(D)', r='Draw money(R)', t='Transfer(T)', s='Settings(S)', o='Sign out(O)', h='Help(H)'))
    menu_settings = collections.OrderedDict(dict(c='Change Password(C)', u='Delete account(D)'))

    print('{:=^30}'.format('Menu'))
    print('\n'.join(menu.values()))
    # print('\n'.join(menu_settings.values()))
    print('=' * 30)

def get_cmd():




# 获取一级菜单命令
def get_first_command():
    cmd_list = collections.OrderedDict(dict(l='Login(L)', s='Sign in(S)', q='Quit(Q)'))
    print()
    print('\t'.join(cmd_list.values()))
    cmd = input('Command: ').lower()
    return cmd if str(cmd) in cmd_list.keys() else 'Input Error!'


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
            print('INFO: \n\t{} login Success!'.format(current_user))
            return current_user
        else:
            print('INFO: \n\tAccess denied. \n\t{} more chances!\n'.format(2 - i))
    else:
        print("Too many authentication failures.")

# 获取二级菜单命令
def get_second_command():
    pass


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
    cmd1 = get_first_command()
    if cmd1 == 'l':  # 进入用户登陆界面
        user = login()
        print(user)
        print_menu()

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


'''

while True:
    cmd1 = get_first_command()
    if cmd1 == 'l':  # 进入用户登陆界面
        # (1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
        quit_flag = False
        for i in range(3):
            if quit_flag:
                break
            current_user = input('Please enter your username: ')
            current_pass = getpass.getpass('Please enter your password: ')
            login_state, login_message = auth_user(current_user, current_pass)
            if login_state:  # 用户认证通过
                print('INFO: \n\t', login_message)
                print('\tThe current user: {}'.format(current_user))
                print_menu()
                while True:
                    cmd = input('Please enter command or "h" for Help: ').lower()
                    if cmd == 'q':
                        quit_flag = True
                        break
                    elif cmd == 'b':  # 打印余额
                        print('INFO: \n\tBalance: {:.2f} [USD]\n'.format(user_db[current_user]['balance']))
                        continue
                    elif cmd == 'd':  # 存款
                        try:
                            deposit = abs(int(input('Amount of deposit: ')))
                            user_db[current_user]['balance'] += deposit
                            print('INFO: \n\tExecute completes. \n\tThe current balance: {:.2f} [USD]\n'.format(
                                user_db[current_user]['balance']))
                        except:
                            print('Invalid input!')
                        continue
                    elif cmd == 'r':  # 取款
                        try:
                            cash = abs(int(input('Withdrawal amount: ')))
                            user_db[current_user]['balance'] -= cash
                            print('INFO: \n\tExecute completes. \n\tThe current balance: {:.2f} [USD]\n'.format(
                                user_db[current_user]['balance']))
                        except:
                            print('FAILED: \n\tInvalid input!\n')
                        continue
                    elif cmd == 't':  # 转账
                        receiver = input('Receiver: ')
                        try:
                            amount = abs(int(input('Amount: ')))
                        except:
                            print('FAILED: \n\tInvalid input!\n')
                            continue
                        if receiver in user_db.keys():
                            user_db[receiver]['balance'] += amount
                            user_db[current_user]['balance'] -= amount
                            print('INFO: \n\tTransfer to complete!',
                                  '\n\tThe current balance: {:.2f} [USD]\n'.format(user_db[current_user]['balance']))
                        else:  # 收款人不存在
                            print('FAILED: \n\tReceiver dose not exist.\n')
                        continue
                    elif cmd == 'c':  # 修改密码
                        print('Changing password for account {}.'.format(current_user))
                        if getpass.getpass('Please input current password for {}: '.format(current_user)) == \
                                user_db[current_user]['password']:  # 验证当前密码
                            for _ in range(2):  # 尝试两次
                                new_pass1 = getpass.getpass('New password: ')
                                new_pass2 = getpass.getpass('Retype new password: ')
                                if new_pass1 == new_pass2:  # 两次密码是否输入一致
                                    user_db[current_user]['password'] = new_pass2
                                    print('INFO: \n\tThe password updated successfully.\n')
                                    break
                                else:
                                    print('FAILED: \n\tSorry, password do not match.')
                        else:  # 当前密码错误
                            print('FAILED: \n\tManipulation error.')
                        continue
                    elif cmd == 'h':
                        print_menu()
                        continue
                    else:
                        print('Error command!')
            else:
                print('INFO: ', '\n', login_message, '\n{} more chances!\n'.format(2 - i))
        else:
            print('INFO: ', 'Login incorrect!')
    elif cmd1 == 's':  # 进入用户注册界面
        while True:  # 如果用户名重复刚重新输入
            reg_username = input('Please input your name or "q" to Quit: ').lower()
            if reg_username == 'q': break
            sign_result = sign_in(reg_username, user_db)
            if not sign_result:
                continue
            user_db.update(sign_result)
            if reg_username in user_db.keys():
                print('{} Registered successfully!'.format(reg_username))
                print(
                    'Account Info: \n\tAccount: {user}\n\tMobile: {mobile}\n\tBalance: {balance:.2f} [USD]\n\n'.format(
                        user=reg_username, mobile=user_db[reg_username]['mobile'],
                        balance=user_db[reg_username]['balance']))
                break
            else:
                print('{} Registered failed!'.format(reg_username))
        continue
    elif cmd1 == 'q':  # 即出系统
        try:
            with open('user_db.json', 'w') as data:
                json.dump(user_db, data)
        except:
            print('File error.')
        break
    else:
        print(cmd1)
'''
