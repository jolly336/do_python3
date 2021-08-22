#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : flask web框架
# @Time    : 2019/4/21 下午5:51
# @Author  : Nelson
# @Contact : haoxunwang525@gmail.com
# @Site    : nelsonblog.me

"""

"""

# 装饰器
# 控制器

# 成百上千个接口，在需要的函数上添加`控制器`即可
@api.route('/get', methods=['GET'])
def test_javascript_http():
    p = request.args.get('name')
    return p, 200

# 权限控制，身份验证，需要验证才能调用控制器，这里可以看到装饰器很灵活
# 了解AOP思想
@api.route('/psw', methods=['GET'])
@auth.login_required
def get_psw():
    p = request.args.get('psw')
    r = generate_password_hash(p)
    return 'aaaaaa', 200
