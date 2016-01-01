#mysql-5.6.28-winx64的安装与简单配置

+   在官网上下载[mysql-5.6.28-winx64](http://dev.mysql.com/downloads/mysql/5.6.html#downloads)
+   解压mysql-5.6.28-winx64
+   另命名mysql-5.6.28-winx64目录为mysqlserver
+   另命名my-default.ini 为my.ini

##修改my.ini
    change
        # These are commonly set, remove the # and set as required.
        # basedir = .....
        # datadir = .....
        # port = .....
        # server_id = .....
    to 
        # These are commonly set, remove the # and set as required.
        basedir = C:\Program Files\MySQL\mysqlserver
        datadir = C:\Program Files\MySQL\mysqlserver\data
        port = 3306
        # server_id = .....
+   以管理员的身份进入C:\Program Files\MySQL\mysqlserver\bin

##安装与启动
    mysqld -install     # mysqld -remove
    net start mysql     # net stop mysql

##修改root密码
    #>mysqladmin -u root password "123456"
    Warning: Using a password on the command line interface can be insecure.

    #>mysql -u root -p
    Enter password: ******

##解决中文编码问题
###统一成utf-8编码
###在my.ini中添加
    [client]
        default-character-set=utf8
    [mysqld]
        default-storage-engine=INNODB
        character-set-server=utf8
        collation-server=utf8_general_ci

###建database的时候加上
    character set 'utf8'
###建table的时候加上
    engine=InnoDB default charset=utf8
###看编码可以用
    show create database db_name
    show create table tb_name

    show variables like 'character_set_%'
    show variables like '%char%'
###终端上修改可以这样
    set character_set_client='utf-8'
    set character_set_connection='utf-8'
    set character_set_results='utf-8'
