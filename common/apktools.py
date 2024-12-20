# -*- coding: utf-8 -*-
"""
====================================
@File Name ：apktools.py
@Time ： 2022/5/4 20:29
@Create by Author ： lileilei
====================================
"""


from androguard.misc import AnalyzeAPK

def get_apkname(apk):
    
    a, _, _ = AnalyzeAPK(apk, False, "r")
    return a.get_package()


def get_apk_lanchactivity(apk):
    
    a, _, _ = AnalyzeAPK(apk, False, "r")
    return a.get_main_activity()