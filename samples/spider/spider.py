#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 爬虫
# @Time    : 2019/4/21 下午6:01
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
    模块注释
    This is a module
'''

import re
from urllib import request

# --- 这不是注释，这是文案，多行注释需要使用''' ''' ---
# 断点调试
# BeautifulSoup, Scrapy
# 爬虫、反爬虫、反反爬虫
# ip 封
# 代理ip库

class Spider():
    '''
        类注释
        This is a class
        Spider写的不好，抵御业务变化的能力太差了
        防御性风格代码
    '''

    # 类变量
    url = 'https://www.panda.tv/cate/lol'
    # \w\W \s\S .
    # Python 默认是贪婪模式，需要使用非贪婪 ?
    # () 使用组来剔除不需要的字符
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    # 私有函数
    # python自带库来获取数据 request
    def __fetch_content(self):
        '''
        方法注释
        Python的注释是写在里面的，其它语言写在外部
        :return:
        '''

        # This is a HTTP request 代码单行注释，注释和紧接行最好空行，阅读感良好
        # 代码行数最好控制在 10-20行，不然无法复用
        r = request.urlopen(Spider.url)

        # bytes
        htmls = r.read()
        # 不建议使用print来断点调试
        # print(htmls)
        htmls = str(htmls, encoding='utf-8')
        return htmls

    # 正则分析
    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        # print(root_html[0])
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        print(anchors)
        return anchors

    # 精炼数据(规范数据)，去除名字空格，strip() 去除前后空格
    def __refine(self, anchors):
        # 使用lambda，或者可以使用for-in循环
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'[0]]
        }
        return map(l, anchors)

    # 业务处理阶段，排序(降序)
    def __sort(self, anchors):
        # key函数，指定哪个元素作为比较大小，dict不支持比较
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    # 比较种子
    def __sort_seed(self, anchor):
        # 返回字符串，以字符串第一个字符开始比较，应该换算成数字比较
        # return anchor['number']
        r = re.findall('\d*', anchor['number'])
        # 有可能有小数
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    # 展现
    def __show(self, anchors):
        # for anchor in anchors:
        #     print(anchor['name'] + '---' + anchor['number'])

        for rank in range(0, len(anchors)):
            print('rank ' + str(rank + 1)
                  + ' : ' + anchors[rank]['name']
                  + '   ' + anchors[rank]['number'])

    # 存储数据库/大数据

    # 入口函数
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
