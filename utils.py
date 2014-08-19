#!/usr/bin/env python
# -*- coding=utf8 -*-

"""
    author: liangchao01
    date:   20140818
    version: 1.0
"""

import sys
import xlwt
from calculator import *
import nameDecorator

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
base_style = xlwt.XFStyle()
base_style.alignment = alignment
float_style = xlwt.easyxf(num_format_str='0.00%')
float_style.alignment = alignment

class ConfInfo(object):
    def __init__(self, fileName):
        self.block_list = []
        self.sid_list = []
        self.srcid_dict = {}
        self.date_list = None
        self.sheet_name = []
        self.loadConf(fileName)
    def loadConf(self, fileName):
        f = open(fileName, 'r')
        for line in f:
            line = line.strip()
            if line.startswith('#') or len(line) == 0:
                continue
            if line.startswith('@'):
                sheet_block = []
                for line in f:
                    line = line.strip()
                    if line.startswith('SheetName'):
                        self.sheet_name.append(line.split(':')[1])
                        continue
                    if line.startswith('@'):
                        self.block_list.append(sheet_block)
                        break
                    sheet_block.append(line.split(','))
            elif line.startswith('Sid'):
                info = line.split(' ')
                sid_info = info[0]
                sid = sid_info.split(':')[1]
                self.sid_list.append(sid)

                if len(info) != 2:
                    continue
                srcid_info = info[1]
                self.srcid_dict[sid] = srcid_info.split(":")[1].split(',')

            elif line.startswith('Date'):
                self.date_list = line.split(':')[1].split(',')
    # for test
    def printSelf(self):
        print self.block_list
        print self.sheet_name
        print self.sid_list
        print self.srcid_dict
        print self.date_list

class Write2Excel(object):
    def __init__(self, confInfo, final_data_list):
        self.confInfo = confInfo
        self.final_data_list = final_data_list
        self.total_result = None
    def insertData(self, ws, title, start_row, start_column):
        for r in range(0, len(self.final_data_list)):
            SidDataDict = self.final_data_list[r]
            cal = eval("%sCal(self.confInfo, SidDataDict)"%(title))
            result = cal.getResult()
            self.addTotle(result)
            for c in range(0, len(result)):
                style = base_style
                if title.endswith('Rate'):
                    style = float_style
                ws.write(start_row+r, start_column+c, result[c], style)
        # write to avg value
        for k in range(0, len(self.total_result)):
            if title.endswith('Rate'):
                ws.write(start_row+len(self.final_data_list), start_column+k,
                        self.total_result[k]/len(self.final_data_list), float_style)
            else:
                ws.write(start_row+len(self.final_data_list), start_column+k,
                        round(self.total_result[k]/len(self.final_data_list)), base_style)
        self.total_result = None
    def addTotle(self, result):
        if self.total_result == None:
            self.total_result = result[:]
        else:
            for i in range(0, len(result)):
                self.total_result[i] += result[i]

    def format(self):
        #=============== format workbook ===============
        wb = xlwt.Workbook(encoding='utf-8')
        exp_num = len(self.confInfo.sid_list)
        date_list_len = len(self.confInfo.date_list)
        # --------------sheet 0 and sheet 1-----------------
        for sheet_num, sheet_list in enumerate(self.confInfo.block_list):
            # pass sheet 2 because it is special
            if sheet_num == 2:
                break
            ws = wb.add_sheet(self.confInfo.sheet_name[sheet_num])
            for block_num, title_list in enumerate(sheet_list):
                for i in range(0, len(title_list)):
                    ws.write_merge(block_num*(4+date_list_len), block_num*(4+date_list_len), 1+i*exp_num, (i+1)*exp_num,
                                   nameDecorator.getTitleName(title_list[i]), base_style)
                    for j in range(0, exp_num):
                        ws.write(1+block_num*(4+date_list_len), 1+i*exp_num+j,
                                 nameDecorator.getSidName(self.confInfo.sid_list[j], self.confInfo.sid_list), base_style)
                    self.insertData(ws, title_list[i], 2+block_num*(4+date_list_len), 1+i*exp_num)

                #----- write date info ------
                dates = self.confInfo.date_list
                for k in range(0, date_list_len):
                    ws.write(block_num*(4+date_list_len)+k+2, 0, dates[k], base_style)
                ws.write(block_num*(4+date_list_len)+2+date_list_len, 0, '均值', base_style)
        # -------------sheet 2 -----------------------------
        sheet_list2 = self.confInfo.block_list[2]
        ws = wb.add_sheet(self.confInfo.sheet_name[2])
        merge_len = 0
        for sid, srcid_list in self.confInfo.srcid_dict.items():
            merge_len += len(srcid_list)
        for block_num, title_list in enumerate(sheet_list2):
            for i in range(0, len(title_list)):
                offset = 1
                ws.write_merge(block_num*(5+date_list_len), block_num*(5+date_list_len), 1+merge_len*i, (i+1)*merge_len,
                               nameDecorator.getTitleName(title_list[i]), base_style)
                for sid in self.confInfo.sid_list:
                    if not self.confInfo.srcid_dict.has_key(sid):
                        continue
                    srcid_list = self.confInfo.srcid_dict[sid]
                    ws.write_merge(1+block_num*(5+date_list_len), 1+block_num*(5+date_list_len),
                                   offset, offset+len(srcid_list)-1,
                                   nameDecorator.getSidName(sid, self.confInfo.sid_list), base_style)
                    for idx, srcid in enumerate(srcid_list):
                        ws.write(2+block_num*(5+date_list_len), offset+idx, srcid, base_style)
                    offset += len(srcid_list)
                self.insertData(ws, title_list[i], 3+block_num*(5+date_list_len), 1+i*merge_len)
            #----- write date info ------
            dates = self.confInfo.date_list
            for k in range(0, date_list_len):
                ws.write(block_num*(5+date_list_len)+k+3, 0, dates[k], base_style)
            ws.write(block_num*(5+date_list_len)+3+date_list_len, 0, '均值', base_style)
        # ----------------sheet 3 (pos info)-----------------------
        if len(self.confInfo.block_list) >= 4:
            sheet_list3 = self.confInfo.block_list[3]
            ws = wb.add_sheet(self.confInfo.sheet_name[3])
            sid_list_len = len(self.confInfo.sid_list)
            merge_len = 5*sid_list_len
            for block_num, title_list in enumerate(sheet_list3):
                for i in range(0, len(title_list)):
                    ws.write_merge(block_num*(5+date_list_len), block_num*(5+date_list_len),
                                   1+merge_len*i, (i+1)*merge_len,
                                   nameDecorator.getTitleName(title_list[i]), base_style)
                    start_c = 1+merge_len*i
                    for j in range(1, 6):
                        ws.write_merge(1+block_num*(5+date_list_len), 1+block_num*(5+date_list_len),
                                   start_c, start_c+sid_list_len-1, 'pos='+str(j), base_style)
                        for idx, sid in enumerate(self.confInfo.sid_list):
                            ws.write(2+block_num*(5+date_list_len), start_c+idx,
                                     nameDecorator.getSidName(sid, self.confInfo.sid_list), base_style)
                        start_c += sid_list_len
                    self.insertData(ws, title_list[i], 3+block_num*(5+date_list_len), 1+i*merge_len)

                #----- write date info ------
                dates = self.confInfo.date_list
                for k in range(0, date_list_len):
                    ws.write(block_num*(5+date_list_len)+k+3, 0, dates[k], base_style)
                ws.write(block_num*(5+date_list_len)+3+date_list_len, 0, '均值', base_style)

        wb.save("result1.0.xls")
        print 'Done.'

if "__main__" == __name__:
    confInfo = ConfInfo('conf.ini')
    confInfo.printSelf()
    #w2e = Write2Excel(confInfo, [])
    #w2e.format()
