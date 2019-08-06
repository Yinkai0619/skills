#!/usr/bin/env python

import getpass
import os
import json
import collections
from functools import wraps



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

    :param menu_item:
    :return: command for menu
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
        # print('Invalid argument.')
        return
    return result

# fun = index_menu
# fun = menus('index')
# fun = menus('feature')
# print(fun)
print(menus('index'))
# print(fun.__name__, fun.__doc__)

