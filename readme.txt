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
�½�mysql�˻�: CREATE USER 'dog'@'localhost' IDENTIFIED BY '123456'; 