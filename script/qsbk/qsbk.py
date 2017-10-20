# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
main_url="https://www.qiushibaike.com/text/page"
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
def get_page_respose(page_num):
        page_url=main_url+str(page_num)
        requst=urllib2.Request(page_url,headers=header)
        respose=urllib2.urlopen(requst)
        html=respose.read().decode('utf-8')
        return html
def get_page_item(page_num):
        html=get_page_respose(page_num)
        pattern=re.compile(r'<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<i.*?class="number">(.*?)</i>'
                            +r'.*?<i.*?class="number">(.*?)</i>',re.S)
        items=re.findall(pattern,html)
        page=[]
        for item in items:
            content=re.sub('<br/>','\n',item[1])
            page.append([item[0].strip(),content.strip(),item[2].strip(),item[3].strip()])
        return page
def run(page_num):
    page=get_page_item(page_num)
    user_input=raw_input(u"Enter to contiue(or q to exit)\n")
    while(user_input!='q'):
        if(len(page)>0):
            one_story=page[0]
            print u"%s(作者)\n%s\n点赞 %s \t评论 %s"%(one_story[0],one_story[1],one_story[2],one_story[3])
            del page[0]
        else:
            page_num=page_num+1
            page = get_page_item(page_num)
            one_story = page[0]
            print u"%s(作者)\n%s\n点赞 %s \t评论 %s" % (one_story[0], one_story[1], one_story[2], one_story[3])
            del page[0]
        user_input = raw_input("Enter to contiue(or q to exit)\n")
num=int(raw_input(u"input page number you want to look \n"))
run(num)





