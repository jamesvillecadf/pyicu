import time
import os
NowTime=time.strftime('%m%d',time.localtime())
currentpath=os.getcwd()
projectdir="python"
from os.path import isfile,join,isdir
filelist=[f for f in os.listdir(join(currentpath,projectdir)) if isfile(join(currentpath,projectdir,f))]
