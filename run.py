""" 
@author: lileilei
@file: run.py 
@time: 2018/5/6 17:32 
"""
from case.uicrawler import run
import  os
from common.log import LOG
from common.execlog import run_adb_log
import multiprocessing
from common.Makecasenum import call_num
from common.apktools import get_apkname,get_apk_lanchactivity
basepth=os.getcwd()

def uicrawler():
    
    LOG.name = "基于Appium UI遍历测试"
    os.path.join(os.path.join(basepth, 'testlog'), 'UI-' + call_num + '.log')
    path=os.path.join(os.path.join(os.getcwd(),"installapk"),'autohome.apk')
    testapk = get_apkname(path)
    testapklanchactivity = get_apk_lanchactivity(
        path)
    path = os.path.join(os.path.join(os.getcwd(), 'testlog'), call_num)
    if os.path.exists(path) is False:
        os.mkdir(path)
    runlog = multiprocessing.Pool()
    runlog.apply_async(run_adb_log, ("0A311FDD4006QW", path))
    run('0A311FDD4006QW', testapk, '4723', 'Android', call_num,testapklanchactivity)
    runlog.close()
    runlog.terminate()

if __name__=="__main__":
    uicrawler()