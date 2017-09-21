# coding=utf-8
import re
import requests
import os
import shutil
import sqlite3
import img

#cursor.execute('delete from girls where id <> \'\' ')

def db_insert(sn_index,dbfile):
    '''insert girls info to db'''
#    conn = sqlite3.connect('./beauty360.db')
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    url=r'http://image.so.com/zj?ch=beauty&t1=625&sn=%s' % (sn_index)
    string=r'[^>:]{"(.*?)}'
    index=sn_index
    for l in img.req_get_findall(url,string):
    #    l = l.replace('\/','/')
        index=index+1
        print '-------------',index
        string=r'"*(.*?)":"*(.*?)[,"]*["]'
        insert_string1=r''
        insert_string2=r''
        for a in re.findall(string,l,re.M + re.S + re.DOTALL):
    #        print a[0]
#            print a[0],'---',a[1].decode('unicode_escape')
            if insert_string1!='':
                insert_string1+=','
            if insert_string2!='':
                insert_string2+=','
            insert_string1=insert_string1+'\''+a[0]+'\''
            insert_string2=insert_string2+'\''+a[1].decode('unicode_escape')+'\''
    #    print insert_string1
    #    print insert_string2
        insert_string='insert into girls (%s) values (%s)' % (insert_string1,insert_string2)
#        print insert_string

        try :
            cursor.execute(insert_string)
            conn.commit()
            print "插入数据库成功",index
        except sqlite3.Error,e:
            print "插入数据库失败",index, e

    cursor.close()
    conn.close()


#for i in xrange(10):
#    db_insert(i*30)

def db_girlsall(dbfile):
    '''select all info from girls table'''
    print 'select start ......'
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    select_string='select * from girls'
    cursor.execute(select_string)
    i=0
    for row in cursor:
        i=i+1
        print '[',i,']','--',row[2],'--',row[6],'--',row[7]
#        for item in row:
#            print item
    cursor.close()
    conn.close()
    print 'select down'



