import getinfo
import re
def getlist(pageid):
    userlistpage = 'http://bt.byr.cn/users.php?page='
    listurl=userlistpage+str(pageid)
    page=getinfo.get_respose(listurl).read()
    pattern=re.compile(r'userdetails.php\?id=(.*?)"',re.S)
    idlist=re.findall(pattern,page)
    del idlist[0]
    return idlist

