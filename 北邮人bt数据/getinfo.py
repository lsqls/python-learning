# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
import urllib2
import re
import os
import time
from bs4 import BeautifulSoup
import excsv
def get_respose(url):
    User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    cookie='c_secure_uid=MjQ3NTI1; c_secure_pass=5b8ea8a3380a030dccbf9ff3713e89cf; ' \
           'c_secure_ssl=bm9wZQ%3D%3D; c_secure_tracker_ssl=bm9wZQ%3D%3D; ' \
           'c_secure_login=bm9wZQ%3D%3D; ' \
           'byrbta4=0; byrbta154=0; byrbta1=1; byrbta2=1; byrbta3=0; byrbta=1;' \
           ' _ga=GA1.2.389372178.1493985064; _gid=GA1.2.328643244.1508565229'#手动登陆后，复制cookie值到这里
    headers={'User-Agent':User_Agent,'Cookie':cookie}
    requst=urllib2.Request(url,headers=headers)
    try:
        respose=urllib2.urlopen(requst)
        return respose
    except urllib2.URLError,e:
        print e.reason
def tran_to_GB(row_size):
    row_size=row_size.split()
    num=float(row_size[1])
    unit=row_size[2]
    unit_dic={"KB":0.000001,"MB":0.001,"GB":1,"TB":1000,"PB":1000000}
    size=num*unit_dic[unit]
    return size
def get_user_info(id):
    user_page_url='http://bt.byr.cn/userdetails.php?id='+str(id)
    user_page=BeautifulSoup(get_respose(user_page_url).read(),'lxml')
#print user_page.prettify()
    username_info=user_page.find(name='h1')
    userid=(id)
    username=username_info.b.string
#  country=username_info.img
    able_read=user_page.find('td',text=u'等级')
    if(able_read):
        level=user_page.find('td', text=u'等级').next_sibling.img['alt']
        male=user_page.find('img',attrs={'class':'male'})
        if male:
            sex=u'男'
        else:
            sex=u'女'
        register_time=user_page.find('td',text=u'加入日期').next_sibling.span['title']
        recent_active_time=user_page.find('td',text=u'最近动向').next_sibling.span['title']
        upload_size=tran_to_GB(user_page.find('strong',text=u'上传量').next_element.next_element)
        download_size=tran_to_GB(user_page.find('strong',text=u'下载量').next_element.next_element)
        school=user_page.find('td',text=u'学校').next_sibling.string
        return [userid, username, level, sex, register_time, recent_active_time, upload_size, download_size, school]
    else:
        return [userid, username]

