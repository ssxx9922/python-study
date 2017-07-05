# map 函数  传入一个值 返回一个值
def format_name(s):
    return s[:1].upper() + s[1:].lower()
print(map(format_name, ['adam', 'LISA', 'barT']))
# reduce 函数  传入两个值 返回一个值
def prod(x, y):
    return x*y
print(reduce(prod, [2, 4, 5, 7, 12]))
# filter 函数   出入两个值  可以不返回值  过滤
import math
def is_sqr(x):
    if math.sqrt(x)%1==0:
        return x
print(filter(is_sqr, range(1, 101)))
# sorted 排序方法
def cmp_ignore_case(s1, s2):
    return cmp(s1.lower(),s2.lower())
print(sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case))
# 返回参数为函数
def calc_prod(lst):
    def haha():
        s = 1
        for i in lst:
            s = s*i
        return s
    return haha
f = calc_prod([1, 2, 3, 4])
print(f())
# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            return lambda: i*i
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())

# 密名函数
def is_not_empty(s):
    return s and len(s.strip()) > 0
print(filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END']))

# @decorator 装饰器
"""
  打印日志 ：@log
  性能检测 ：@performance
  数据库事物 ：@transaction
  URL路由 ：post('register')
"""