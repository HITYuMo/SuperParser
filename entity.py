#!/usr/bin/env python
#coding=utf-8
import pub

"""
author: zhuang li, huang haiyuan
date: 2013/01/28
description:
    This is so Java!
"""

class DisplayEntity(pub.Entity) :
    def __init__(self) :
        super(DisplayEntity, self).__init__()
        self.disp = 0
        self.click_disp = 0
        self.noclick_disp = 0

class ClickEntity(pub.Entity):
    def __init__(self):
        super(ClickEntity, self).__init__()
        self.click = 0

class RealClickEntity(ClickEntity):
    def __init__(self):
        super(RealClickEntity, self).__init__()
        self.has_click = 0
        self.tab_click = 0
        self.behz_click = 0
        self.pos_click = [0]*21
        self.pos_hasclick = [0]*21
        self.pp_click = 0
        self.ppim_click = 0
        self.pl_click = 0
        self.lm_click = 0
        self.im_click = 0
        self.plr_click = 0
        self.unknown_click = 0
        self.normal_click = 0
        self.alxl_click = 0
        self.alxr_click = 0
        self.alxt_click = 0
        self.p1p10_has_click = 0
        self.p2p10_has_click = 0
        # this must be the same with the tab_values in accesslog
        tabs = ['logo', 'news', 'tieba', 'zhidao', 'music', 'pic', 'video', 'map', 'wenku', 'more']
        self.tabs = {}
        for tab in tabs :
            self.tabs[tab] = 0

class FirstClickEntity(ClickEntity):
    def __init__(self):
        super(FirstClickEntity, self).__init__()
        self.first_tm = 0
        self.first_pos = 0
        self.first_vclick = 0

class LastClickEntity(ClickEntity):
    def __init__(self):
        super(LastClickEntity, self).__init__()
        self.last_tm = 0
        self.last_pos = 0
        self.last_vclick = 0

class NextClickEntity(ClickEntity) :
    def __init__(self):
        super(NextClickEntity, self).__init__()
        self.click_change = 0
        self.noclick_change = 0

class CubeEntity(pub.Entity) :
    def __init__(self) :
        super(CubeEntity, self).__init__()
        self.cube = []
        for i in range(0, 80) :
            self.cube.append(0)

class CardCubeEntity(pub.Entity) :
    def __init__(self) :
        super(CardCubeEntity, self).__init__()
        self.cube = []
        for i in range(0, 25) :
            self.cube.append(0)
