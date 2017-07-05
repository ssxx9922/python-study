#!/usr/bin/python3
# coding=utf-8

import time
import datetime

"""
密名函数
"""
# 单行注释

# 装饰器打印函数名
def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '...'
        return f(*args, **kw)
    return fn

@log
def showdate(scound):
    starttime = datetime.datetime.now()
    time.sleep(scound)
    endtime = datetime.datetime.now()
    print(endtime - starttime)

showdate(0.5)

# 装饰器打印函数执行时间
import time
def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args,**kw)
        t2 = time.time()
        print('call '+ f.__name__ + '() in ' +str(t2-t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

# 装饰器传参数
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1)*1000 if unit =='ms' else (t2 - t1)
            print 'call %s() in %f %s'%(f.__name__, t, unit)
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

# 修改装饰器内部的函数名
import functool  ## 系统自带复制函数名的方法
def performance(unit):
    def f1(f):
        @functools.wraps(f)
        def f2(*args, **kw):
            t1 = time.time()
            print 'call %s() in %s%s' % (f.__name__, t1, unit)
            return f(*args,**kw)
        return f2
    return f1

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial.__name__

# import functools
"""
functools.partial可以把一个参数多的函数变成一个参数少的新函数，少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了。
"""
sorted_ignore_case = functools.partial(sorted,key=str.lower)
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

int2 = functools.partial(int, base=2)
print(int2('1000000')) ##将参数格式化成2进制