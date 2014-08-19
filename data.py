import entity

class SrcidData(object):
    def __init__(self, srcid):
        self.srcid = srcid
        self.disp_ent = None # DisplayEntity
        self.click_ent = None # RealClickEntity

    def setSrcidDisp(self, json_ent):
        self.disp_ent = json_ent

    def setSrcidClick(self, json_ent):
        self.click_ent = json_ent

class SidData(object):
    def __init__(self, sid):
        self.sid = sid
        self.disp_ent = None # DisplayEntity
        self.click_ent = None # RealClickEntity
        self.next1 = {} # type -> count # just limit query
        self.next2 = {} # type -> count # limit any-right-disp
        self.next3 = {} # type -> count # limit given-right-disp
        self.srcid_dict = {} # srcid -> SrcidData

        self.right_disp_ent = None # DisplayEntity, how many disp has right_disp
        self.right_click_ent = None

        self.given_right_disp_ent = None
        self.given_right_click_ent = None

        self.dl_disp_ent = None
        self.dl_click_ent = None
        self.dl_srcid_dict = {}

        self.pos_dict = {}

    def setSidGRightDisp(self, sid, json_ent):
        self.given_right_disp_ent = json_ent

    def setSidGRightClick(self, sid, json_ent):
        self.given_right_click_ent = json_ent

    def setSidDisp(self, sid, json_ent):
        self.disp_ent = json_ent

    def setSidClick(self, sid, json_ent):
        self.click_ent = json_ent

    def setSidRightDisp(self, sid, json_ent):
        self.right_disp_ent = json_ent

    def setSidRightClick(self, sid, json_ent):
        self.right_click_ent = json_ent

    def setSidSrcidDisp(self, sid, srcid, json_ent):
        if srcid not in self.srcid_dict:
            self.srcid_dict[srcid] = SrcidData(srcid)
        self.srcid_dict[srcid].setSrcidDisp(json_ent)

    def setSidSrcidClick(self, sid, srcid, json_ent):
        if srcid not in self.srcid_dict:
            self.srcid_dict[srcid] = SrcidData(srcid)
        self.srcid_dict[srcid].setSrcidClick(json_ent)

    def setSidNext(self, sid, next_key, json_ent, typ):
        if typ == 1:
            self.next1[next_key] = json_ent.click
        elif typ == 2:
            self.next2[next_key] = json_ent.click
        elif typ == 3:
            self.next3[next_key] = json_ent.click

    def setDlDisp(self, sid, json_ent):
        self.dl_disp_ent = json_ent

    def setDlClick(self, sid, json_ent):
        self.dl_click_ent = json_ent

    def setDlSrcidDisp(self, sid, srcid, json_ent):
        if srcid not in self.dl_srcid_dict:
            self.dl_srcid_dict[srcid] = SrcidData(srcid)
        self.dl_srcid_dict[srcid].setSrcidDisp(json_ent)

    def setDlSrcidClick(self, sid, srcid, json_ent):
        if srcid not in self.dl_srcid_dict:
            self.dl_srcid_dict[srcid] = SrcidData(srcid)
        self.dl_srcid_dict[srcid].setSrcidClick(json_ent)

    def setPosDisp(self, sid, pos, json_ent):
        if pos not in self.pos_dict:
            self.pos_dict[pos] = SrcidData(pos)
        self.pos_dict[pos].setSrcidDisp(json_ent)

    def setPosClick(self, sid, pos, json_ent):
        if pos not in self.pos_dict:
            self.pos_dict[pos] = SrcidData(pos)
        self.pos_dict[pos].setSrcidClick(json_ent)

class FinalData(object):
    def __init__(self, date_list):
        self.final_data_dict = []
        self.date_list = date_list
        self.execute()
    def _analyzeOneLine(self, data_dict, head, key, value, tag):
        head_eles = head.split("#")
        task_id = head_eles[1]
        job_id = head_eles[2]

        key_eles = key.split("{_\a_}")
        tag_id = key_eles[0]

        output_id = "_".join((task_id, job_id, tag_id))

        cur_sid = key_eles[1]
        if cur_sid not in data_dict:
            data_dict[cur_sid] = SidData(cur_sid)

        if True:
            # === Task 0 ===
            # --- DisplayJob ---
            # Sid
            if output_id == "0_0_0":
                cur_sid = key_eles[1]
                cur_entity = entity.DisplayEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setSidDisp(cur_sid, cur_entity)
            # Sid, RightDisplay
            elif output_id == '0_0_1':
                cur_sid = key_eles[1]
                cur_entity = entity.DisplayEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setSidRightDisp(cur_sid, cur_entity)
            # Sid, ZhixinSrcid
            elif output_id == "0_0_2":
                cur_sid = key_eles[1]
                cur_srcid = key_eles[2]
                cur_entity = entity.DisplayEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setSidSrcidDisp(cur_sid, cur_srcid, cur_entity)
            # --- ClickJob ---
            # Sid
            elif output_id == "0_1_0":
                cur_sid = key_eles[1]
                cur_entity = entity.RealClickEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setSidClick(cur_sid, cur_entity)
            # Sid, RightDisplay
            elif output_id == '0_1_1':
                cur_sid = key_eles[1]
                cur_entity = entity.RealClickEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setSidRightClick(cur_sid, cur_entity)
            # Sid, ZhixinSrcid
            elif output_id == "0_1_2":
                cur_sid = key_eles[1]
                cur_srcid = key_eles[2]
                cur_entity = entity.RealClickEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setSidSrcidClick(cur_sid, cur_srcid, cur_entity)
            # === Task 1 === (right given srcid)
            # --- DisplayJob ---
            # Sid
            elif output_id == '1_0_0':
                cur_sid = key_eles[1]
                cur_entity = entity.DisplayEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setSidGRightDisp(cur_sid, cur_entity)
            # Sid, RightPos
            elif output_id == "1_0_2":
                cur_sid = key_eles[1]
                cur_pos = key_eles[2]
                cur_entity = entity.DisplayEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setPosDisp(cur_sid, cur_pos, cur_entity)
            # --- ClickJob ---
            # Sid
            elif output_id == '1_1_0':
                cur_sid = key_eles[1]
                cur_entity = entity.RealClickEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setSidGRightClick(cur_sid, cur_entity)
            # Sid, RightPos
            elif output_id == "1_1_2":
                cur_sid = key_eles[1]
                cur_pos = key_eles[2]
                cur_entity = entity.RealClickEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setPosClick(cur_sid, cur_pos, cur_entity)
            # === Task 2 ===
            # --- NextClickJob
            # Sid_Next_Click(just query limit)
            elif output_id == "2_0_0":
                cur_sid = key_eles[1]
                cur_next_typ = key_eles[2]
                cur_entity = entity.NextClickEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setSidNext(cur_sid, cur_next_typ, cur_entity, 1)
            # === Task 3 ===
            # --- NextClickJob ---
            # Sid_Next click (any right disp)
            elif output_id == '3_0_0':
                cur_sid = key_eles[1]
                cur_next_typ = key_eles[2]
                cur_entity = entity.NextClickEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setSidNext(cur_sid, cur_next_typ, cur_entity, 2)
            # Sid_Next click (given right disp)
            elif output_id == '4_0_0':
                cur_sid = key_eles[1]
                cur_next_typ = key_eles[2]
                cur_entity = entity.NextClickEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setSidNext(cur_sid, cur_next_typ, cur_entity, 3)
            elif output_id == '5_0_0':
                cur_sid = key_eles[1]
                cur_entity = entity.DisplayEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setDlDisp(cur_sid, cur_entity)
            elif output_id == '5_1_0':
                cur_sid = key_eles[1]
                cur_entity = entity.RealClickEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setDlClick(cur_sid, cur_entity)
            elif output_id == "6_0_1":
                cur_sid = key_eles[1]
                cur_srcid = key_eles[2]
                cur_entity = entity.DisplayEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setDlSrcidDisp(cur_sid, cur_srcid, cur_entity)
            elif output_id == "6_1_1":
                cur_sid = key_eles[1]
                cur_srcid = key_eles[2]
                cur_entity = entity.RealClickEntity()
                cur_entity = cur_entity.fromJson(value)
                data_dict[cur_sid].setDlSrcidClick(cur_sid, cur_srcid, cur_entity)

    def getOneDayData(self, date):
        data_dict = {}
        for line in open(r"data/"+date, 'r'):
            line = line.strip()
            if line is None or len(line) == 0:
                continue
            head, key, value, tag = line.split("\t")
            self._analyzeOneLine(data_dict, head, key, value, tag)
        return data_dict
    def execute(self):
        for date in self.date_list:
            result = self.getOneDayData(date)
            self.final_data_dict.append(result)
    def getFinalDataList(self):
        return self.final_data_dict
