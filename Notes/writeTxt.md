### 操作TXT文件

`file = open('explore.txt','a',encoding='utf-8')`
第二个参数我们设置成了 a，这样在每次写入文本时不会清空源文件，而是在文件末尾写入新的内容，这是一种文件打开方式。关于文件打开方式，其实还有另外的几种，在此列举如下：
- r，以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
- rb，以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
- r+，打开一个文件用于读写。文件指针将会放在文件的开头。
- rb+，以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
- w，打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- wb ，以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- w+， 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- wb+，以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- a，打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 - ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
- a+，打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
- ab+，以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
##### 简写
```
with open('explore.txt', 'a', encoding='utf-8') as file:
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
```


### csv操作

###### 写入
```
import csv
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
```
字典的写入方式
```
with open('data.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
```
###### 读取
```
import csv
with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
```
利用 Pandas 的 read_csv() 方法将数据从 CSV 中读取出来
```
import pandas  as pd

df = pd.read_csv('data.csv')
print(df)
```

### json操作
###### 读取
```
import json
data = json.loads(str)
```
###### 输出
```
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
```