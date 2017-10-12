mysql安装：
	1. mysql.zip解压，并将压缩包中的文件放到C:\Program Files\MySQL\MySQL Server 5.7
	2. cmd（管理员模式）cd到bin目录里，执行命令 mysqld -install mysql --default-file= my.ini的绝对路径 (这句命令是添加mysql服务，并把my.ini设为配置文件）
	3. 执行命令 mysqld --initialize-insecure --user=任意的用户名  （这句命令是为了初始化数据库data）
	4. 执行命令 net start mysql启动服务（删除服务：mysqld –remove mysql）

my.ini文件内容：
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