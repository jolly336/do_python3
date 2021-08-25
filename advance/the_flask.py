#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : flask web框架
# @Time    : 2019/4/21 下午5:51
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""
flash web 框架
"""


# 装饰器
# 控制器

# 成百上千个接口，在需要的函数上添加`控制器`即可
# 访问控制器的 url 地址，http 方法
@api.route('/get', methods=['GET'])
def test_javascript_http():
    p = request.args.get('name')
    return p, 200


# 一个中大型项目接口 三五十个太正常了，rest 接口能少点，如果不是 rest，业务性接口成百上千很正常

# 权限控制，身份验证，需要验证才能调用控制器，这里可以看到装饰器很灵活
# 了解AOP思想，从一个横切面来解决问题
# 多个装饰器
# 图书信息服务，任何人都可以访问，像豆瓣 api。但删除接口不是任何人都能访问
@api.route('/psw', methods=['GET'])
@auth.login_required
def get_psw():
    p = request.args.get('psw')
    r = generate_password_hash(p)
    return 'aaaaaa', 200
