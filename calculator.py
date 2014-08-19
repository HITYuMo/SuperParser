#!/usr/bin/env python
# -*- coding=utf8 -*-

"""
    author: liangchao01
    date:   20140818
    version: 1.0
"""


class BaseCal(object):
    def __init__(self, confInfo, SidDataDict):
        self.SidDataDict = SidDataDict
        self.sid_list = confInfo.sid_list
        self.srcid_dict = confInfo.srcid_dict

class DispCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(sidData.disp_ent.disp)
        return result

class HasClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.has_click) / sidData.disp_ent.disp)
        return result

class ClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.click) / sidData.disp_ent.disp)
        return result

class TurnRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.next1['turn']) / sidData.disp_ent.disp)
        return result

class ChangeRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.next1['change']) / sidData.disp_ent.disp)
        return result

class RsRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.next1['rs']) / sidData.disp_ent.disp)
        return result

class TabRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.tab_click) / sidData.disp_ent.disp)
        return result

class NormalClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.normal_click) / sidData.disp_ent.disp)
        return result

class RightZhixinClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.alxr_click) / sidData.disp_ent.disp)
        return result

class LeftZhixinClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.alxl_click) / sidData.disp_ent.disp)
        return result

class UnknownClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.unknown_click) / sidData.disp_ent.disp)
        return result

class PPClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.pp_click) / sidData.disp_ent.disp)
        return result

class PPIMClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.ppim_click) / sidData.disp_ent.disp)
        return result

class PLClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.pl_click) / sidData.disp_ent.disp)
        return result

class LMClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.lm_click) / sidData.disp_ent.disp)
        return result

class IMClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.im_click) / sidData.disp_ent.disp)
        return result

class PLRClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.click_ent.plr_click) / sidData.disp_ent.disp)
        return result

class CardClickCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            card_click = 0
            sidData = self.SidDataDict[sid]
            if sid not in self.SidDataDict or sid not in self.srcid_dict:
                continue
            for srcid in self.srcid_dict[sid]:
                card_click += sidData.srcid_dict[srcid].click_ent.click
            result.append(card_click)
        return result

class CardDLRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            card_click = 0
            sidData = self.SidDataDict[sid]
            if sid not in self.SidDataDict or sid not in self.srcid_dict:
                continue
            for srcid in self.srcid_dict[sid]:
                card_click += sidData.srcid_dict[srcid].click_ent.click
            result.append(float(card_click) / float(sidData.disp_ent.disp) )
        return result

class RightCoverageRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.given_right_disp_ent.disp) / float(sidData.disp_ent.disp))
        return result

class RightCDRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.given_right_click_ent.alxr_click) / float(sidData.given_right_disp_ent.disp))
        return result

class DLDispCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict or sid not in self.srcid_dict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(sidData.dl_disp_ent.disp)
        return result

class DLHasClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict or sid not in self.srcid_dict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.dl_click_ent.has_click) / float(sidData.dl_disp_ent.disp))
        return result

class DLClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict or sid not in self.srcid_dict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(float(sidData.dl_click_ent.click) / float(sidData.dl_disp_ent.disp))
        return result

class AddedHasClickDispCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict or sid not in self.srcid_dict:
                continue
            sidData = self.SidDataDict[sid]
            result.append(sidData.dl_click_ent.has_click)
        return result

class CardDispCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict or sid not in self.srcid_dict:
                continue
            sidData = self.SidDataDict[sid]
            for srcid in self.srcid_dict[sid]:
                if srcid not in sidData.srcid_dict or sidData.srcid_dict[srcid].disp_ent is None:
                    result.append(0) # "-"
                else:
                    result.append(sidData.srcid_dict[srcid].disp_ent.disp)
        return result

class CardHasClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict or sid not in self.srcid_dict:
                continue
            sidData = self.SidDataDict[sid]
            for srcid in self.srcid_dict[sid]:
                if srcid not in sidData.srcid_dict:
                    result.append("0")
                elif sidData.srcid_dict[srcid].click_ent is None or sidData.srcid_dict[srcid].disp_ent is None:
                    result.append("0")
                else:
                    result.append(float(sidData.srcid_dict[srcid].click_ent.has_click) / sidData.srcid_dict[srcid].disp_ent.disp)
        return result

class CardClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict or sid not in self.srcid_dict:
                continue
            sidData = self.SidDataDict[sid]
            for srcid in self.srcid_dict[sid]:
                if srcid not in sidData.srcid_dict:
                    result.append("0")
                elif sidData.srcid_dict[srcid].click_ent is None or sidData.srcid_dict[srcid].disp_ent is None:
                    result.append("0")
                else:
                    result.append(float(sidData.srcid_dict[srcid].click_ent.click) / sidData.srcid_dict[srcid].disp_ent.disp)
        return result

class CardBehzClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for sid in self.sid_list:
            if sid not in self.SidDataDict or sid not in self.srcid_dict:
                continue
            sidData = self.SidDataDict[sid]
            for srcid in self.srcid_dict[sid]:
                if srcid not in sidData.srcid_dict:
                    result.append("0")
                elif sidData.srcid_dict[srcid].click_ent is None or sidData.srcid_dict[srcid].disp_ent is None:
                    result.append("0")
                else:
                    result.append(float(sidData.srcid_dict[srcid].click_ent.behz_click) / sidData.srcid_dict[srcid].disp_ent.disp)
        return result

class CardPosDispCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for pos in ['1', '2', '3', '4', '5']:
            for sid in self.sid_list:
                if sid not in self.SidDataDict:
                    continue
                sidData = self.SidDataDict[sid]
                if pos not in sidData.pos_dict or sidData.pos_dict[pos].disp_ent is None:
                    result.append("-")
                else:
                    result.append(sidData.pos_dict[pos].disp_ent.disp)
        return result

class CardPosHasClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for pos in ['1', '2', '3', '4', '5']:
            for sid in self.sid_list:
                if sid not in self.SidDataDict:
                    continue
                sidData = self.SidDataDict[sid]
                if pos not in sidData.pos_dict or sidData.pos_dict[pos].disp_ent is None or sidData.pos_dict[pos].click_ent is None:
                    result.append("0")
                else:
                    result.append(float(sidData.pos_dict[pos].click_ent.has_click) / float(sidData.pos_dict[pos].disp_ent.disp))
        return result

class CardPosClickRateCal(BaseCal):
    def __init__(self, confInfo, SidDataDict):
        BaseCal.__init__(self, confInfo, SidDataDict)
    def getResult(self):
        result = []
        for pos in ['1', '2', '3', '4', '5']:
            for sid in self.sid_list:
                if sid not in self.SidDataDict:
                    continue
                sidData = self.SidDataDict[sid]
                if pos not in sidData.pos_dict or sidData.pos_dict[pos].disp_ent is None or sidData.pos_dict[pos].click_ent is None:
                    result.append("0")
                else:
                    result.append(float(sidData.pos_dict[pos].click_ent.click) / float(sidData.pos_dict[pos].disp_ent.disp))
        return result
