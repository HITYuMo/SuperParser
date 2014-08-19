#!/usr/bin/env python
# -*- coding=utf8 -*-

"""
    author: liangchao01
    date:   20140818
    version: 1.0
"""

import utils
import data

confInfo = utils.ConfInfo('conf.ini')
finalData = data.FinalData(confInfo.date_list)
final_data_list = finalData.getFinalDataList()
w2e = utils.Write2Excel(confInfo, final_data_list)
w2e.format()
