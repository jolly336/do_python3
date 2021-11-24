# -*- coding:utf-8 -*-
# Created by baiy on 2017-06-27
# 获取pandatv房间到弹幕并存入kafka
# python pandatv_danmu.py room_id kafka_server kafka_topic_name log_file
# python pandatv_danmu.py 748737 192.168.2.196:9092 spider_test ../logs/748737.log

import requests
import json
import socket
from struct import pack
import re
import time
import threading
import sys
import multiprocessing
import logging
from spider_adv.conf import *
from kafka import KafkaProducer

def store_panda_tv_danmu_into_kafka(room_id, kafka_server, kafka_topic_name):
    producer = KafkaProducer(bootstrap_servers=kafka_server)

    room_requests = requests.get(ROOM_INFO_URL.format(room_id))
    room_info = json.loads(room_requests.text)
    chat_addr = room_info['data']['chat_addr_list'][0].split(':')
    chat_addr_ip = chat_addr[0]
    chat_addr_port = chat_addr[1]
    rid = room_info['data']['rid']
    appid = room_info['data']['appid']
    auth_type = room_info['data']['authType']
    sign = room_info['data']['sign']
    ts = room_info['data']['ts']

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((chat_addr_ip, int(chat_addr_port)))

    def keep_alive():
        while True:
            client.sendall(b'\x00\x06\x00\x06')
            logging.info('{0} room_id:{1} keep alive'.format(time.strftime(TIME_FORMAT, time.localtime()),
                                                             room_id))
            time.sleep(120)

    keep_alive_thread = threading.Thread(target=keep_alive)
    keep_alive_thread.setDaemon(True)
    keep_alive_thread.start()

    send_message = '\n'.join(['u:{0}@{1}'.format(rid, appid),
                              'k:1',
                              't:300',
                              'ts:{0}'.format(ts),
                              'sign:{0}'.format(sign),
                              'authtype:{0}'.format(auth_type)])
    send_message = b'\x00\x06\x00\x02\x00' + \
                   pack('B', len(send_message)) + \
                   send_message.encode('utf-8') + \
                   b'\x00\x06\x00\x00'
    client.sendall(send_message)
    danmu_count = 0
    while True:
        content = client.recv(9999)
        try:
            for danmu in re.findall(b'({"type":.*?}})', content):
                danmu = json.loads(danmu.decode('utf-8', 'ignore'))
                producer.send(kafka_topic_name, json.dumps(danmu, ensure_ascii=False).encode('utf-8'))
                producer.flush()
                danmu_count += 1
                if danmu_count % 100 == 0:
                    logging.info('{0} room_id:{1} danmu_count:{2}'.format(time.strftime(TIME_FORMAT, time.localtime()),
                                                                          room_id,
                                                                          danmu_count))
        except:
            continue


def main():
    # 多进程方案如果报错不好维护
    # room_ids = ['748737', '10455']
    # for room_id in room_ids:
    #     p = multiprocessing.Process(target=store_panda_tv_danmu_into_kafka, args=(room_id,))
    #     p.start()
    if len(sys.argv) < 5:
        print
        'python pandatv_danmu.py room_id kafka_server kafka_topic_name log_file'
        sys.exit()

    room_id = sys.argv[1]
    kafka_server = sys.argv[2]
    kafka_topic_name = sys.argv[3]
    log_file = sys.argv[4]

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt=TIME_FORMAT,
                        filename=log_file,
                        filemode='a')

    store_panda_tv_danmu_into_kafka(room_id, kafka_server, kafka_topic_name)


if __name__ == '__main__':
    main()
