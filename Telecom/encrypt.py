#coding: utf8  
import sys  
from Crypto.Cipher import AES  
from binascii import b2a_hex, a2b_hex  
import hashlib
import base64


class prpcrypt():  
    def __init__(self, key):  
        self.key = key  
        self.mode = AES.MODE_CBC  
       
    #加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数  
    def encrypt(self, text):  
        cryptor = AES.new(self.key, self.mode, '1234567812345678')  
        text = text.encode("utf-8")  
        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用  
        length = 16  
        count = len(text)  
        add = length - (count % length)  
        text = text + (b'\0' * add)  
        self.ciphertext = cryptor.encrypt(text)  
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题  
        #所以这里统一把加密后的字符串转化为16进制字符串  
        text = base64.b64encode(self.ciphertext)
        return text
       
    #解密后，去掉补足的空格用strip() 去掉  
    def decrypt(self, text):  
        cryptor = AES.new(self.key, self.mode, '1234567812345678')  
        plain_text = cryptor.decrypt(base64.b64decode(text))  
        return plain_text.rstrip(b'\0').decode("utf-8")  
   
if __name__ == '__main__':  
    m = hashlib.md5()
    m.update('login.189.cn'.encode('utf-8'))
    k = m.hexdigest()

    pc = prpcrypt(k)      #初始化密钥  
    e = pc.encrypt("518316")  
    d = pc.decrypt(e)  
    f = pc.decrypt('0uPemJpAdhN40Sj97vogmg==')                      
    print (e, f, d)  
    e = pc.encrypt("我是一个粉刷匠1231繁體testひらがな")  
    d = pc.decrypt(e)                    
    print (e, d)  