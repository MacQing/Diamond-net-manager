mysql��װ��
	1. mysql.zip��ѹ������ѹ�����е��ļ��ŵ�C:\Program Files\MySQL\MySQL Server 5.7
	2. ��MySQL Server 5.7Ŀ¼�½�my.ini�ļ�����д���������ݣ�
		[client]
		port=3306
		default-character-set=utf8
		[mysqld]
		port=3306
		character_set_server=utf8
		#��ѹĿ¼
		basedir=C:\Program Files\MySQL\MySQL Server 5.7
		#��ѹĿ¼��dataĿ¼
		datadir=C:\Program Files\MySQL\MySQL Server 5.7\data
		sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
	3. cmd������Աģʽ��cd��binĿ¼�ִ������mysqld -install 
	4. mysqld -install(������������mysql���񣬲���my.ini��Ϊ�����ļ���
	3. mysqld --initialize-insecure
	4. ִ������ net start mysql��������ɾ������mysqld �Cremove mysql��

����mysql: mysql -uroot
�鿴����Щ���ݿ⣺show databases;
ѡ�����ݿ⣺use databasename;
�½�mysql�˻�: CREATE USER 'dog'@'localhost' IDENTIFIED BY '123456'; 
ִ���ļ��е�sql���source C:/github/Diamond-net-manager/sql/sql.txt;

���ݿ���ƣ�
��1���������
	�ֶΣ��������ͣ������ɫ���߶ȣ����ʱ�䣬�������������ʱ�䣬��������
��2������
	�ֶΣ��������ͣ������ɫ���߶ȣ������

-- ���������	
create table in_out_storage_log
(
	id int unsigned auto_increment,
	record_user varchar(10) not null, -- ����Ա
	material varchar(10) not null, -- ��������
	spec varchar(10) not null, -- ���
	color varchar(10) not null, -- ��ɫ
	hight varchar(10) not null, -- �߶�
	in_storage_date datetime not null default now(), -- ���ʱ��
	in_storage_num int unsigned not null, -- �������
	out_storage_date datetime not null default now(), -- ����ʱ��
	out_storage_num int not null, -- ��������
	primary key (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8
;

-- ������
create table storage_num
(
	id int unsigned auto_increment,
	material varchar(10) not null, -- ��������
	spec varchar(10) not null, -- ���
	color varchar(10) not null, -- ��ɫ
	hight varchar(10) not null, -- �߶�
	storage_num int not null default 0
	primary key (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
;