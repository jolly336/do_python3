# -*- coding:utf-8 -*-
# 常量配置文件

# pandatv 房间信息获取url
ROOM_INFO_URL = "http://www.panda.tv/ajax_chatinfo?roomid={0}"

# 命令行配置
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
SEARCH_CMD = 'ps -ef | grep pandatv_danmu.py | grep {0}/{1}.log'
START_CMD = 'nohup python pandatv_danmu.py {0} {1} {2} {3}/{0}.log > /dev/null 2>&1 &'
STOP_CMD = 'kill -9 {0}'

# KAFKA配置
KAFKA_SERVER = '192.168.2.196:9092'
KAFKA_TOPIC_NAME = 'spider_test'

# 日志目录
LOGS_DIR = '../logs'

# 待爬取房间信息配置
CONF_PATH = 'room.conf'
