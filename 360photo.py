# coding=utf-8
import re
import requests
import os
import shutil


basePath = r"D:/360photo"


if os.path.isdir(basePath):
    shutil.rmtree(basePath)
    os.mkdir(basePath)
else:
    os.mkdir(basePath)


def req_get_findall(url,string) :
    '''requests url , and re findall string , return list'''
    r=requests.get(url)
    l=re.findall(string,r.content,re.M + re.S + re.DOTALL)
    print 'found ',len(l),' from ',url
    return l

def save_url(filename,url) :
    '''save url as file'''
    r=requests.get(url)
    imgfile=open(filename, "wb")
    imgfile.write(r.content)
    imgfile.close()

savecount=0
url=r'http://image.so.com/z?ch=beauty&t1=625'
findstring=r'"id":"(.*?)".*?"group_title":"(.*?)".*?"tag":"(.*?)".*?"label":"(.*?)"'
for id in  req_get_findall(url, findstring) :
    print '%s - %s - %s' % (id[1].decode('unicode_escape'),id[2].decode('unicode_escape'),id[3].decode('unicode_escape'))
    url = r'http://image.so.com/zvj?ch=beauty&t1=625&id=%s' % (id[0])
    findstring=r'"qhimg_url":"(.*?)"'
    count=1
    for imgurl in req_get_findall(url, findstring) :
        imgurl = imgurl.replace("\/", "/")
        suffix=imgurl.split('.')[-1]
        filename = r"%s/%s_%s.%s" % (basePath,id[1].decode('unicode_escape'),count,suffix)
        count=count+1
#        print filename
        save_url(filename,imgurl)
        savecount=savecount+1

print '爬取完成',savecount
