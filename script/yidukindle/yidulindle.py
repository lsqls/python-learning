import urllib
import urllib2
import cookielib
import re
filename="cookie.txt"
url="http://www.yidukindle.com/login.php"
postdata=urllib.urlencode({
'useremail':'',
'userpwd':''
})
cookie=cookielib.MozillaCookieJar(filename)
hander=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(hander)
respose=opener.open(url,data=postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
nexturl="http://www.yidukindle.com/magzine.list.php?magid=72"
nextrespose=opener.open(nexturl)
gethtml=str(nextrespose.read())
with open("yidukindle.html","w") as f:
    f.write(gethtml)
    f.close()
time_pattern=re.compile(r'\d{4}-\d{2}-\d{2}')
gettime=re.search(time_pattern,gethtml)
if gettime:
    print gettime.group()
with open("lasttime","r") as f:
    last_time=f.read()
    f.close()
now_time=str(gettime.group()).split('-')
last_time=last_time.split('-')
print last_time
print now_time
def send():
    link_pattern=re.compile(r'magzine\.send\.php\?dateid=\d+')
    send_link=re.search(link_pattern,gethtml)
    link="http://www.yidukindle.com/{}".format(str(send_link.group()))
    print link
    opener.open(link)
    with open("lasttime","w") as f:
        f.write(str(gettime.group()))
        f.close()
    print "send success"
if int(last_time[0])<int(now_time[0]):
   send()
else:
    if int(last_time[1])<int(now_time[1]):
        send()
    else:
            if int(last_time[2])<int(now_time[2]):
                send()







