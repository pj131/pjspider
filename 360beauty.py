# coding=utf-8
import re
import requests
import os
import shutil
import img

#basePath = r"D:/360photo"
basePath = r"./360photo"


#if os.path.isdir(basePath):
#    shutil.rmtree(basePath)
if not os.path.isdir(basePath):
    os.mkdir(basePath)


#idcount=0
#url=r'http://image.so.com/z?ch=beauty&t1=625'
#url=r'http://image.so.com/zj?ch=beauty&t1=625&sn=30'


def spider360(idcount):
    url=r'http://image.so.com/zj?ch=beauty&t1=625&sn=%s' % (idcount)
    findstring=r'"id":"(.*?)".*?"group_title":"(.*?)".*?"tag":"(.*?)".*?"label":"(.*?)"'
    print 'start ......',idcount
    for id in  img.req_get_findall(url, findstring) :
        print '[%s]%s - %s - %s' % (idcount,id[1].decode('unicode_escape'),id[2].decode('unicode_escape'),id[3].decode('unicode_escape'))
        url = r'http://image.so.com/zvj?ch=beauty&t1=625&id=%s' % (id[0])
        findstring=r'"qhimg_url":"(.*?)"'
        count=1
        for imgurl in img.req_get_findall(url, findstring) :
            imgurl = imgurl.replace("\/", "/")
            suffix=imgurl.split('.')[-1]
            filename = r"%s/[%s]%s_%s.%s" % (basePath,idcount,id[1].decode('unicode_escape'),count,suffix)
            filename=filename.replace("\/", "")
            count=count+1
            img.save_url(filename,imgurl)
        idcount=idcount+1

for i in xrange(10) :
    spider360(i*30)
#spider360(197)
print 'done',img.savecount
