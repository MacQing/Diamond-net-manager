mysql安装：
	1. mysql.zip解压，并将压缩包中的文件放到C:\Program Files\MySQL\MySQL Server 5.7
	2. 在MySQL Server 5.7目录新建my.ini文件，并写入如下内容：
		[client]
		port=3306
		default-character-set=utf8
		[mysqld]
		port=3306
		character_set_server=utf8
		#解压目录
		basedir=C:\Program Files\MySQL\MySQL Server 5.7
		#解压目录下data目录
		datadir=C:\Program Files\MySQL\MySQL Server 5.7\data
		sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
	3. cmd（管理员模式）cd到bin目录里，执行命令mysqld -install 
	4. mysqld -install(这句命令是添加mysql服务，并把my.ini设为配置文件）
	3. mysqld --initialize-insecure
	4. 执行命令 net start mysql启动服务（删除服务：mysqld –remove mysql）

进入mysql: mysql -uroot
新建mysql账户: CREATE USER 'dog'@'localhost' IDENTIFIED BY '123456'; 