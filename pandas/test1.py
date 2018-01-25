from pandas import Series,DataFrame
import pandas as pd

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

print('-')

print(frame2.loc['three'])

