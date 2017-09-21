#coding=utf-8
import requests
import urllib
import re
import sys
import os

def req_get_findall(url,string) :
    '''requests url , and re findall string , return list'''
    r=requests.get(url)
    l=re.findall(string,r.content,re.M + re.S + re.DOTALL)
    print 'found ',len(l),' from ',url
    return l

savecount=0
def save_url(filename,url) :
    '''save url as file'''
    if os.path.exists(filename):
        print filename,'is exist'
        return
    global savecount
    r=requests.get(url)
    imgfile=open(filename, "wb")
    imgfile.write(r.content)
    imgfile.close()
    savecount = savecount + 1
