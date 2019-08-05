#!/usr/bin/env python

import getpass
import os
import json
import collections



def get_cmd(fn):
    def wrapper(*args, **kwargs):
        cmd_list = fn()
        cmd = str(input('Command: ')).lower()
        return cmd if cmd in cmd_list else 'Input Error!'
    return wrapper

# 打印菜单：
@get_cmd    # menu = get_cmd(menu) = wrapper()
def menu():
    menu_feature = collections.OrderedDict(
        dict(b='Balance inquiry(B)', d='Deposits(D)', r='Draw money(R)', t='Transfer(T)', s='Settings(S)',
             o='Sign out(O)',
             h='Help(H)'))
    menu_settings = collections.OrderedDict(dict(c='Change Password(C)', u='Delete account(D)'))
    print('{:=^30}'.format('Menu'))
    print('\n'.join(menu_feature.values()))
    # print('\n'.join(menu_settings.values()))
    print('=' * 30)
    return menu_feature.keys()

print(menu())



