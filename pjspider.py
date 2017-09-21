# coding=utf-8
import os
import shutil
import platform
import img
import beauty360
import db360

print 'pjspider start......'
basePath = r"./360photo"
if platform.system() == 'Windows':
    basePath = r"D:/360photo"

if os.path.isdir(basePath):
    shutil.rmtree(basePath)

if not os.path.isdir(basePath):
    os.mkdir(basePath)

for i in xrange(2) :
    db360.db_insert(i*30,'./beauty360.db')
#    beauty360.spider360(i*30,basePath)

db360.db_girlsall('./beauty360.db')

print 'pjspider done ......',img.savecount
