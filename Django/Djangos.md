### 安装
`pip install Django`
### 新建工程
`django-admin.py startproject project_name`
### 新加App
cd到工程目录下
`python manage.py startapp app_name`
### 创建数据库
```
# 1. 创建更改的文件
python manage.py makemigrations
# 2. 将生成的py文件应用到数据库
python manage.py migrate
```
### 运行服务器
`python manage.py runserver`

`或者 python manage.py runserver 9999`

`或者 python manage.py runserver 0.0.0.0:8000`
### 清空数据库
`python manage.py flush`
### 创建超级管理员
`python manage.py createsuperuser`
### 修改密码
`python manage.py changepassword username`

### 导入/导出数据
```
python manage.py dumpdata appname > appname.json
python manage.py loaddata appname.json
```

### 数据库命令行
`python manage.py dbshell`

### 环境终端
`python manage.py shell`
`pip install bpython`