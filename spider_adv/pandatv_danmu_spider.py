# -*- coding:utf-8 -*-
# Created by baiy on 2017-06-27
# 读取配置文件中到room_id 批量运行爬虫脚本
# room.conf三列分别为：房间id 房主 房间分类 中间TAB分割
# python pandatv_danmu_spider.py start|monitor|stop

import os
import sys
import time
import logging
from conf import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt=TIME_FORMAT,
                    filename=os.path.join(LOGS_DIR, 'monitor_spider.log'),
                    filemode='a')


def start():
    logging.info('pandatv danmu spider start')
    with open(CONF_PATH) as room_file:
        for line in room_file:
            room_id = line.split('\t')[0]
            os.system(START_CMD.format(room_id, KAFKA_SERVER, KAFKA_TOPIC_NAME, LOGS_DIR))
            logging.info('room_id:{0} start!'.format(room_id))


def monitor():
    logging.info('pandatv danmu spider monitor start')
    while True:
        with open(CONF_PATH) as room_file:
            for line in room_file:
                room_id = line.split('\t')[0]
                process_search_result = os.popen(SEARCH_CMD.format(LOGS_DIR, room_id)).read()
                if len(process_search_result.split('\n')) < 3:
                    os.system(START_CMD.format(room_id, KAFKA_SERVER, KAFKA_TOPIC_NAME, LOGS_DIR))
                    logging.info('room_id:{0} restart!'.format(room_id))
                else:
                    logging.info('room_id:{0} running!'.format(room_id))
        time.sleep(300)


def stop():
    logging.info('pandatv danmu spider stop')
    with open(CONF_PATH) as room_file:
        for line in room_file:
            room_id = line.split('\t')[0]
            process_search_result = os.popen(SEARCH_CMD.format(LOGS_DIR, room_id)).read()
            if len(process_search_result.split('\n')) >= 3:
                pid = [v for v in process_search_result.split('\n')[0].split(' ') if v != ''][1]
                os.system(STOP_CMD.format(pid))
                logging.info('romm_id:{0} pid:{1} stop!'.format(room_id, pid))
            else:
                logging.info('romm_id:{0} stop!'.format(room_id))


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ['start', 'monitor', 'stop']:
        print
        'python pandatv_danmu_spider.py start|monitor|stop'
        sys.exit()

    run_type = sys.argv[1]
    if run_type == 'start':
        start()
    if run_type == 'monitor':
        monitor()
    if run_type == 'stop':
        stop()


if __name__ == '__main__':
    main()
