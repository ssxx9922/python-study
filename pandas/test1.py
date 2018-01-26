from pandas import Series,DataFrame
import pandas as pd
import numpy as np

obj = Series([4,7,-5,3])
print(obj)

print(obj.values)

obj2 = Series([4,7,-5,3],index=['b','d','a','c'])
print(obj2)

print(obj2[obj2>0])
print(obj2 * 2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

print('-')

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)

print('-')

print(obj4.isnull)
print(obj4.notnull)

print('-')

obj4.name = 'population'
obj4.index.name = 'state'

print(obj4)

print('-')

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)

print('-')

print(frame.head())

print('-')

print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

print('=> 多维缺省')

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],index=['one', 'two', 'three', 'four', 'five', 'six'])

print(frame2)

print('通过位置或名称的方式进行获取，比如用loc属性 =>')

print(frame2.loc['three'])

print('')

frame2['debt'] = np.arange(6.)

print(frame2)

print('')

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])


frame2['debt'] = val
print(frame2)

print('新增列=>')
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

print('删除列 =>')
del frame2['eastern']
print(frame2)
print(frame2.columns)


print('嵌套字典 =>')
pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
print(' => T' , '\n',frame3.T)