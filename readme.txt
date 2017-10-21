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
查看有哪些数据库：show databases;
选择数据库：use databasename;
新建mysql账户: CREATE USER 'dog'@'localhost' IDENTIFIED BY '123456'; 
执行文件中的sql命令：source C:/github/Diamond-net-manager/sql/sql.txt;

数据库设计：
表1：入库出库表
	字段：材质类型，规格，颜色，高度，入库时间，入库数量，出库时间，出库数量
表2：库存表
	字段：材质类型，规格，颜色，高度，库存量

-- 建入库出库表	
create table in_out_storage_log
(
	id int unsigned auto_increment,
	record_user varchar(10) not null, -- 操作员
	material varchar(10) not null, -- 材质类型
	spec varchar(10) not null, -- 规格
	color varchar(10) not null, -- 颜色
	hight varchar(10) not null, -- 高度
	in_storage_date datetime not null default now(), -- 入库时间
	in_storage_num int unsigned not null, -- 入库数量
	out_storage_date datetime not null default now(), -- 出库时间
	out_storage_num int not null, -- 出库数量
	primary key (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8
;

-- 建库存表
create table storage_num
(
	id int unsigned auto_increment,
	material varchar(10) not null, -- 材质类型
	spec varchar(10) not null, -- 规格
	color varchar(10) not null, -- 颜色
	hight varchar(10) not null, -- 高度
	storage_num int not null default 0
	primary key (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
;