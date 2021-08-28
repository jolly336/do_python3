#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 爬虫
# @Time    : 2019/4/21 下午6:01
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

'''
案例：简单爬虫

一个完善的爬虫需要反扒机制、自动登录、代理 IP等辅助功能比较繁琐。
目的：更好理解学到的知识；演示 Python 小工具项目应该遵守的一些基本规范；好的代码如何编写。

需求：爬虫的目的，爬什么内容？
-> 某个游戏分类下的各个主播的人气排行，用 rank list 打印出来。（思路：先拿到数据，再计算分类）

观看人数

HTML 字符串繁多，字符串内置函数有点吃力，需要使用正则了。

---

爬虫前奏：

* 明确目的
* 找到数据对应的网页
* 分析网页的结构找到数据所在的「标签」位置-标签启到定位的作用，常量字符串（常量标签）可以达到定位边界的效果

code:

* 模拟 HTTP 请求，向服务器发送这个请求，获取到服务器返回给我们的 HTML。
* 用正则表达式提取我们要的数据（主播名字，人气）

* 爬虫框架

- Beautiful Soup 提炼内容，爬虫框架，可以偷懒，简化代码 https://www.crummy.com/software/BeautifulSoup/
- Scrapy https://scrapy.org
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
    # 熊猫 TV 页面应该是模板编写的，把 lol 换成 hearthstone 炉石传说
    url = 'https://www.panda.tv/cate/lol'
    # \w\W \s\S . 说明：\w 表示字符，\W 表示非字符，两个一起使用就可以匹配所有内容
    # Python 默认是贪婪模式，需要使用非贪婪 ?
    # () 使用组来剔除不需要的字符
    # 思考1：为啥要加 ？答案：因为 </div> 闭合标签不止一个，所以要使用非贪婪
    # 思考2：把 [\s\S] 换成 [.] 可以吗？为什么？答案：. 匹配除了换行符 \n 之外的字符
    # 思考2：() 圆括号的作用？答案：分组，因为我们只要定界标签内部的字符串，不包括定界标签！
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

        # bytes 字节码
        htmls = r.read()
        # 不建议使用 print 来断点调试
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
            'number': anchor['number'][0]
        }
        return map(l, anchors)

    # 有了数据，下一步就是业务处理，排序
    # 业务处理阶段，排序(降序)
    def __sort(self, anchors):
        # key函数，指定哪个元素作为比较大小，dict不支持比较
        # sort 默认是升序排序，加个 reverse=True 改成降序排序
        # 字符串比较要改成数字比较
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    # 比较器，作为 sort 函数的 key 来做比较
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
