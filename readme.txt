mysql��װ��
	1. mysql.zip��ѹ������ѹ�����е��ļ��ŵ�C:\Program Files\MySQL\MySQL Server 5.7
	2. cmd������Աģʽ��cd��binĿ¼�ִ������ mysqld -install mysql --default-file= my.ini�ľ���·�� (������������mysql���񣬲���my.ini��Ϊ�����ļ���
	3. ִ������ mysqld --initialize-insecure --user=������û���  �����������Ϊ�˳�ʼ�����ݿ�data��
	4. ִ������ net start mysql��������ɾ������mysqld �Cremove mysql��

my.ini�ļ����ݣ�
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