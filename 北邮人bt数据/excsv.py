#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import csv
headers = [u'用户id',u'用户名', u'等级',u'性别',u'注册时间',u'最近活跃时间',u'上传量', u'下载量', u'学校']
with open('userinfo.csv','wb') as f:
    f.write(u'\ufeff'.encode('utf8'))
    w = csv.writer(f)
    w.writerow([item.encode('utf8') for item in headers])
def add(userinfo):
    userinfo=map(unicode,userinfo)
    with open('userinfo.csv', 'ab') as f:
        f.write(u'\ufeff'.encode('utf8'))
        w = csv.writer(f)
        w.writerow([item.encode('utf8') for item in userinfo])

