# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import os
import time
from bs4 import BeautifulSoup
def get_respose(url):
    User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    cookie=''#手动登陆后，复制cookie值到这里
    headers={'User-Agent':User_Agent,'Cookie':cookie}
    requst=urllib2.Request(url,headers=headers)
    try:
        respose=urllib2.urlopen(requst)
        return respose
    except urllib2.URLError,e:
        print e.reason
def get_table():
    url='http://bt.byr.cn/'
    respose=get_respose(url)
    print u"登录成功"
    html=BeautifulSoup(respose.read(),'lxml')
    table_all=html.find_all(limit=1,name='table',attrs={'width':'100%','border':'1','cellspacing':'0','cellpadding':'5'})
    for i in table_all:
        table=i
    print u"成功取得种子列表"
    return table
def get_have_download_list():
    with open('downloaded.txt','r') as f:
            list=[]
            downloadeds=f.read()
            downloadeds=downloadeds.split()
            for downloaded in downloadeds:
                list.append(downloaded)
            f.close()
            return list
def write_to_downloaded(download):
    with open('downloaded.txt', 'a') as f:
        f.write(str(download)+'\n')
      #  print u'写入ID成功'
        f.close()
def get_size_if_free(id):
    link='http://bt.byr.cn/details.php?id='+str(id)+'&hit=1'
    torrent_html = BeautifulSoup(get_respose(link).read(), 'lxml')
    iffree=False
    twofree=torrent_html.find_all(name='font',attrs={'class':'free'})
    free=torrent_html.find_all(name='font',attrs={'class':'twoupfree'})
    if (free or twofree):
        iffree=True
    #torrent_size = torrent_html.find_all(name='td', attrs={'valign': 'top', 'align': 'left'}, limit=2)
    #size = torrent_size[1].next_element.next_element.next_element.next_element.strip()
    #if re.search('GB', size):
    #    num = re.sub('GB', '', size)
    #    size = float(num) * 1000
    #else:
    #    re.search('MB', size)
    #    num = re.sub('MB', '', size)
    #    size = float(num)
    return iffree
def get_download_list():
    table=get_table()
    b = table.find_all('b')
    list = []
    for i in b:
        name=i.contents[0]
        seeder=i.next_element.next_element.contents[0]
        download=i.next_element.next_element.next_element.next_element.contents[0]
        href=i.previous_element['href']
        id_pattern=re.compile('id=(.*?)&')
        __id = re.findall(id_pattern, str(href))
        for i in __id:
            id=str(i)
        have_download_list=get_have_download_list()
        free=get_size_if_free(id)
        #and (size<10000)
        if not(id in have_download_list) and (int(seeder)<=2 and int(download)>=4) and (free):
            list.append({'name':name,'id':id})
            print u'有种子可以下载了'
            write_to_downloaded(id)
    if not(list):
            print u'没有种子可以下载'
    return list
def download_list():
    torrentss = get_download_list()
    for torrent in torrentss:
        link='http://bt.byr.cn/download.php?id='+str(torrent['id'])
        torrent_file = get_respose(link).read()
        with open(torrent['id']+'.torrent', 'wb') as f:
            f.write(torrent_file)
            print u'成功下载种子文件'
            f.close()
    return torrentss
def download():
    torrentss=download_list()
    download_tool='uTorrent.exe'#修改这里为你的utorrent程序的位置
    for torrent in torrentss:
        cmd=download_tool+' '+os.path.abspath(torrent['id']+'.torrent')
        print u'打开utorrent中.......'
        os.system(cmd)
        print u'已使用Utorrent下载'
def run():
    while(True):
        print u'系统启动中..........'
        download()
        print u'系统休眠中...........'
        time.sleep(180)

run()