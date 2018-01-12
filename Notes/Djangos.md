# Django教程

### 安装
`pip install Django`
### 新建工程
`django-admin startproject project_name`
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

### 编译模型
`python3 manage.py makemigrations`

### 导入数据库
`python3 manage.py migrate`

### 数据库命令行
`python manage.py dbshell`

### 环境终端
`python manage.py shell`
`pip install bpython`

# ubantu安装Python3

1. 安装python3

`apt-get install python3`
 
2. 安装pip3

`apt-get install python3-pip`

3. 为python3添加包

`pip3 install packagename`

4. 安装pillow

> 首先安装支持包

`apt-get install libjpeg-dev libfreetype6-dev zlib1g-dev libpng12-dev`

> 安装pillow

`pip3 install pillow`

5. 创建python3的虚拟环境

`virtualenv -p /usr/bin/python3 环境名称`或者`virtualenv -p python3 环境名称`

6. 如果不能安装python3-pip（比如低版本ubuntu），如何使用pip安装python3 库

`python3 -m pip install 包`

7. 另一个安装pip3方法:

`aptitude install python3-setuptools # 安装easy_install3工具`
`easy_install3 pip`     # 安装pip3

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

- zip压缩文件
`zip -r archive_name.zip directory_to_compress`

- zip解压文件
`unzip unzip archive_name.zip`