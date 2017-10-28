#coding:utf-8
import excsv
import getinfo
import getid
import time
def run():
    min=0
    max=4323
    start=120
    end=max
    pageid=start
    while(pageid<=end):
        idlist=getid.getlist(pageid)
        for id in idlist:
            userinfo=getinfo.get_user_info(id)
            excsv.add(userinfo)
        print 'page',pageid,'analysis success'
        pageid=pageid+1
        time.sleep(10)
        with open('last','w') as f:
            f.write(str(pageid))
            f.close()
    print u'本次读取完成，信息保存在userinfo.csv中'
run()



