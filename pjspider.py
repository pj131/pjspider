# coding=utf-8
import os
import shutil
import platform
import img
import beauty360

basePath = r"./360photo"
if platform.system() == 'Windows':
    basePath = r"D:/360photo"

if os.path.isdir(basePath):
    shutil.rmtree(basePath)

if not os.path.isdir(basePath):
    os.mkdir(basePath)

for i in xrange(2) :
    beauty360.spider360(i*30,basePath)

print 'beauty360 done ......',img.savecount
