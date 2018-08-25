import re

import logging

str1 = r'xf_product_v7.10.0_hyy_guanwang_07_19_15_43.apk'
str2 = r'xm_product_v7.10.0_flavortest_07_19_15_43.apk'


def get_channel(apkname):
    ma_channel = re.search(
        r'v([0-9]+).([0-9]+).([0-9]+)_(.*?)_([0-9]+)'
        , apkname
        , re.M | re.I)
    channel = ''
    if ma_channel:
        channel = ma_channel.groups()[3]
    return channel


def get_network(apkname):
    ma_network = re.search(
        r'([a-z]+)_([a-z]+)_'
        , apkname
        , re.M | re.I
    )
    network = ''
    if ma_network:
        network = ma_network.groups()[1]
    return network


def get_appname(apkname):
    ma_appname = re.search(
        r'([a-z]+)_'
        , apkname
        , re.M | re.I
    )
    appname = ''
    if ma_appname:
        appname = ma_appname.groups()[0]
    return appname

def re_do():
    print 'channel:', get_channel(str1), '\tnetwork:', get_network(str1), '\tappname:', get_appname(str1)
    print 'channel:', get_channel(str2), '\tnetwork:', get_network(str2), '\tappname:', get_appname(str2)
    logging.warning('channel:' + get_channel(str1)+'\tnetwork:'+get_network(str1)+'\tappname:'+get_appname(str1))