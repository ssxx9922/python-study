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

    obj = AES.new(k, AES.MODE_CBC, '1234567812345678')
    length = 16
    count = len(message)
    if count < length:
        add = (length-count)
        text = message + ('\0' * add)
    elif count > length:
        add = (length-(count % length))
        text = text + ('\0' * add)
    ciphertext = obj.encrypt(text) #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题 所以这里统一把加密后的字符串转化为16进制字符串
    text = base64.b64encode(ciphertext)
    print(text)
    return text