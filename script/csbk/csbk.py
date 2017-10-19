# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import random
main_url="https://www.qiushibaike.com/article/"
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
def get_page_respose(page_num):
        page_url=main_url+str(page_num)
        requst=urllib2.Request(page_url,headers=header)
        respose=urllib2.urlopen(requst)
        html=respose.read().decode('utf-8')
        return html
def get_page_item(page_num):
        html=get_page_respose(page_num)
        pattern=re.compile('<div.*?class="author.*?clearfix">.*?<h2>(.*?)</h2>.*?<div.*?class="content">(.*?)</div>'+'(.*?)</div>',re.S)
        items=re.findall(pattern,html)
        author_content="".join(items[0])
        if(re.search('img',author_content)):
            get_page_item(page_num+1)
        else:
            author_content=re.sub('<br/>','\n',author_content)
            print author_content
while(True):
    user_input=raw_input("Enter to contiue\n")
    if(user_input!='q'):
        page_num=int(random.randint(0,100000))
        get_page_item(page_num)


#下一页问题未解决

