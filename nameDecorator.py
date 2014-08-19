#!/usr/bin/env python
# -*- coding=utf8 -*-

"""
    author: liangchao01
    date:   20140818
    version: 1.0
"""

title_map = {
    'Disp': '展现量',
    'HasClickRate': '有点击行为比例',
    'ClickRate': '点击率',
    'RightCoverageRate': '右侧覆盖率',
    'RightCDRate': '右侧点展比',
    'TurnRate': '翻页率',
    'ChangeRate': '换query比例',
    'RsRate': 'RS点击率',
    'TabRate': 'Tab点击率',
    'NormalClickRate': '左侧点击率(自然结果+ALD)',
    'RightZhixinClickRate': '右侧知心点击率',
    'LeftZhixinClickRate': '左侧知心点击率',
    'UnknownClickRate': '未知点击率',
    'PPClickRate': 'PP点击率',
    'PPIMClickRate': 'PPIM点击率',
    'PLClickRate': 'PL点击率',
    'LMClickRate': 'LM点击率',
    'IMClickRate': 'IM点击率',
    'PLRClickRate': 'Plr点击率',
    'CardClick': '卡片点击量',
    'CardDLRate': '卡片导流率',
    'DLDisp': '导流PV',
    'DLHasClickRate': '导流后有点击行为比例',
    'DLClickRate': '导流后点击率',
    'AddedHasClickDisp': '新增有点PV',
    'CardDisp': '卡片展现量',
    'CardHasClickRate': '卡片有点击行为比例',
    'CardClickRate': '卡片点击率',
    'CardBehzClickRate': '卡片交互点击率',
    'CardPosDisp': '各个位置卡片展现量',
    'CardPosHasClickRate': '各个位置卡片有点比例',
    'CardPosClickRate': '各个位置卡片点击率'
    }

def getTitleName(className):
    if title_map.has_key(className):
        return title_map[className]
    else:
        return 'NotFound'

def getSidName(sid, sid_list):
    if sid == sid_list[-1]:
        return '对照组'
    if len(sid_list) == 2:
        return '实验组'
    for i in range(0, len(sid_list)):
        if (sid == sid_list[i]):
            return '实验'+str(i+1)
    return 'NotFound'


