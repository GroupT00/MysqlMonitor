#!/use/bin/python
# -*- coding:utf-8 -*- -
import MySQLdb,os,re,argparse
parser = argparse.ArgumentParser()
parser.add_argument('-l',default="localhost")
parser.add_argument('-u')
parser.add_argument('-p')
args = parser.parse_args()
path = os.getcwd().replace('\\','/')+'/4dmin55.log'
db = MySQLdb.connect(args.l,args.u,args.p,'mysql')
mysql = db.cursor()
mysql.execute('show variables like "general_log" #4dmin55')
general_log = mysql.fetchone()
mysql.execute('show variables like "general_log_file" #4dmin55')
general_log_file = mysql.fetchone()

if general_log[1] == 'OFF':
	mysql.execute('set global general_log = On')

if general_log_file[1] != path:
	open(path)
	mysql.execute('SET global general_log_file="%s"'%(path))
while(True):
	put = raw_input('>>>')
	if 'exit' in put:
		break
	if os.path.exists(path):
		log = open(path).read()
		find = re.findall(r'\d+ \d\d:\d\d:\d\d.*?Connect.*?\n',log)
		time = find[-1].split()
		rfind =  log.split(find[-1])
		sqlLog = re.findall(r'\d+ Query\t(.*?)\n',rfind[-1])
		for x in range(len(sqlLog)):
			if '4dmin55' in sqlLog[x]:
				pass
			else:
				print '[%s] '%(time[1])+sqlLog[x]
	else:
		mysql.execute('SET global general_log_file="%s"'%(path))

