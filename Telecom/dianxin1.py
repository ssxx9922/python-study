#coding: utf-8
#-电信登录密码加密
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import hashlib
import base64


def process_pwd(message):
    m = hashlib.md5()
    m.update('login.189.cn'.encode('utf-8'))
    k = m.hexdigest()
    print('md5=',k)

    text = message.encode('utf-8')
    obj = AES.new(k, AES.MODE_CBC, '1234567812345678')
    length = 16  
    count = len(text)  
    add = length - (count % length)  
    text = text + (b'\0' * add)  
    ciphertext = obj.encrypt(text) #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题 所以这里统一把加密后的字符串转化为16进制字符串
    text = base64.b64encode(ciphertext)
    print(text)
    return text


# 加密ECS_ReqInfo_login1 有问题
def get_ECS_Reqinfo(mobile,provinceId):
    text = mobile + '$' + '' + '$' + '201' + '$' + '地市（中文/拼音）' + '$' + provinceId + '$' + '' + '$' + '' + '$' + '0'
    text = text.encode("utf-8")
    k = 'login.189.cn\x00\x00\x00\x00'.encode('utf-8')
    obj = AES.new(k, AES.MODE_ECB)
    length = 16  
    count = len(text)  
    add = length - (count % length)  
    text = text + (b'\0' * add)  
    ciphertext = obj.encrypt(text)  
    # ciphertext = obj.encrypt(text) #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题 所以这里统一把加密后的字符串转化为16进制字符串
    text = base64.b64encode(ciphertext)
    print(text)
    return text

import time

def get_wId():
    wId = time.time() * 1000 % 1000
    return str(int(wId))

import random

def get_pvid():
    return str(int(random.random() * 2147483647) * int(time.time() * 1000 % 1000) % 10000000000)

def get_lvid():
    a = ''
    b = list('abcdef1234567890')
    for i in range(0,32):
        a += b[int(random.random() * (len(b) - 1))]
    return a

def get_trkId():
    chars = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    uuid = [''] * 36
    rnd = 0
    r = 0
    for i in range(0,36):
        if i==8 or i==13 or i == 18 or i == 23:
            uuid[i] = '-'
        elif i==14:
            uuid[i] = '4'
        else:
            if rnd <= 0x02:
                rnd = 0x2000000 + int(random.random() * 0x1000000) | 0
            r = rnd & 0xf
            rnd = rnd >> 4
            uuid[i] = chars[r&0x3|0x8 if i==19 else r]
    return ''.join(uuid)

import math

def get_fid():
    b = ''
    c = ''
    d = ''
    f = 8
    e = 4
    for i in range(0,16):
        f = math.floor(random.random() * f) 
        b += '0123456789ABCDEF'[f:f+1]
        f = math.floor(random.random() * e)
        d += '0123456789ABCDEF'[f:f+1]
        f = 16
        e = 16
    c = b + '-' + d
    return c

def get_cookie():
    cookie = {}
    cookie['__qc_wId'] = get_wId()
    cookie['pgv_pvid'] = get_pvid()
    cookie['lvid'] = get_lvid()
    cookie['nvid'] = '1'
    cookie['code_v'] = '20170913'
    cookie['s_cc'] = 'true'
    cookie['s_fid'] = get_fid()
    cookie['loginStatus'] = 'non-logined'
    cookie['trkId'] = get_trkId()
    return cookie


def get_new_cookie():
    cookie = {}
    cookie['__qc_wId'] = get_wId()
    cookie['pgv_pvid'] = get_pvid()
    return cookie