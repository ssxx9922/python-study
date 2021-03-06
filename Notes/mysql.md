### 安装 brew install mysql
### 启动 brew services start mysql
### 查看 brew services list
### 配置脚本 /usr/local/opt/mysql/bin/mysql_secure_installation
```
$ /usr/local/opt/mysql/bin/mysql_secure_installation   //mysql 提供的配置向导
Securing the MySQL server deployment.
Connecting to MySQL using a blank password.
VALIDATE PASSWORD PLUGIN can be used to test passwordsand improve security. It     checks the strength of password and allows the users to set only those passwords which are secure enough. Would you like to setup VALIDATE PASSWORD plugin?

Press y|Y for Yes, any other key for No: k //是否采用mysql密码安全检测插件（这里作为演示选择否，密码检查插件要求密码复杂程度高，大小写字母+数字+字符等）
Please set the password for root here. // 首次使用自带配置脚本，设置root密码

New password:

Re-enter new password:

By default, a MySQL installation has an anonymous user, allowing anyone to log into MySQL without having to have a user account created for This is intended only for testing, and to make the installation go a bit smoother. You should remove them before moving into a production environment.    
Remove anonymous users? [Y/n] Y //是否删除匿名用户
 ... Success!

Normally, root should only be allowed to connect from 'localhost'.This
ensures that someone cannot guess at the root password from the network.

Disallow root login remotely? [Y/n] Y //是否禁止远程登录
 ... Success!

By default, MySQL comes with a database named 'test' that anyone can
access.This is also intended only for testing, and should be removed
before moving into a production environment.

Remove test database and access to it? [Y/n] Y //删除测试数据库，并登录
 Dropping test database...
 ... Success!
 Removing privileges on test database...
 ... Success!

Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.

Reload privilege tables now? [Y/n] Y//重新载入权限表
 ... Success!

All done!  If you've completed all of the above steps, your MySQL
installation should now be secure.

Thanks for using MySQL!

Cleaning up...
```
### 修改路径 `$ PATH="$PATH":/usr/local/opt/mysql/bin/`
### 登录 `$ mysql -u root -p`
### 检查编码 `mysql> show variables like '%char%';`

### 停止 `brew services stop mysql`
### 重启 `brew services restart mysql`

### 安装MySQL驱动
#### 官方mysql-connector-python `$ pip install mysql-connector-python --allow-external mysql-connector-python`
#### pymysql `pip3 install pymysql`

/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
