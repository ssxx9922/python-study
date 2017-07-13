# Django教程

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


# ssh 上传文件至服务器

- 从服务器上下载文件
`scp username@servername:/path/filename /var/www/local_dir（本地目录）`
> 例如scp root@192.168.0.101:/var/www/test.txt  把192.168.0.101上的/var/www/test.txt 的文件下载到/var/www/local_dir（本地目录）


- 上传本地文件到服务器
`scp /path/filename username@servername:/path`
> 例如scp /var/www/test.php  root@192.168.0.101:/var/www/  把本机/var/www/目录下的test.php文件上传到192.168.0.101这台服务器上的/var/www/目录中

 

- 从服务器下载整个目录
`scp -r username@servername:/var/www/remote_dir/（远程目录） /var/www/local_dir（本地目录）`
> 例如:scp -r root@192.168.0.101:/var/www/test  /var/www/  

- 上传目录到服务器
`scp  -r local_dir username@servername:remote_dir`
>例如：scp -r test  root@192.168.0.101:/var/www/   把当前目录下的test目录上传到服务器的/var/www/ 目录

