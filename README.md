# MysqlMonitor
一款监控mysql执行语句的工具

使用方法：[root@AdminSS ~]# python mysql.py -l yourhost -u youruser -p yourpass 
# 原理
运行程序会开启mysql的general_log，并在本地生成log，程序根据正则匹配log中执行sql语句
