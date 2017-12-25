#coding:utf-8

import random


def game(min,max):
    num = random.randint(min,max)
    while True:
        guess = int(input('请输入一个数'))
        if guess < num:
            min = guess
            print('小了')
        elif guess > num:
            max = guess
            print('大了')
        else:
            print('答对了')
            break

game(1,1000)