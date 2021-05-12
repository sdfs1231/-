#转换excel为list
import os
import re
import xlrd
import time
import datetime


def trans_time(time_str):
    #转换 str -> time 转换为时间time,分三种情况 xxxx xx:xx x:xx
    if not isinstance(time_str,str) :
        time_str = str(int(time_str));
    time_str = str(time_str);
    if re.match(r'\d{2}:\d{2}',time_str):
        return time.strptime(time_str,"%H:%M");
    elif re.match(r'\d{2}\d{2}',time_str):
        return time.strptime(time_str,"%H%M");
    elif re.match(r'\d:\d{2}',time_str):
        return time.strptime(time_str,"%H:%M");
    elif re.match(r'\d:\d{2}:\d{2}',time_str):
        return time.strptime(time_str,"%H:%M:%S");
    

class _Transfer:
    #读取excel数据
    
    def __init__(self,excel_path):
        #excel文件的路径
        self.excel_path = excel_path;
        self.data = self._read_excel();

    def _read_excel(self):
        #读取excel内容,返回list

        excel_data = [];
        
        try:
            _excel = xlrd.open_workbook(self.excel_path);
        except PermissionError:
            print("请关闭",self.excel_path,"后再进行操作");
            return -1;
        except FileNotFoundError:
            print("文件不存在")
            return -1;
        
        _tables = [ _excel.sheet_by_index(0) , _excel.sheet_by_index(1) ];

        for i,table in enumerate(_tables):
            index = 0;
            if i == 0:
                #第一张表
                index = 10;
                #index+=1;
            elif i==1:
                #第二张表
                index = 13;
                
            raw_data = table.row_values(index);
            #原始数据
            

            while(raw_data[1] != "" and raw_data[1] != None and raw_data[1]!=" "):
                raw_date = xlrd.xldate.xldate_as_datetime(table.cell(index,1).value, 0);
                #转换为datetime基础，后续需要填时间

                temp1 = raw_data[6];
                temp2 = raw_data[7];
                if isinstance(raw_data[6],float) and raw_data[6]<=1:
                    temp1 = raw_data[11]
                if isinstance(raw_data[7],float) and raw_data[7]<=1:
                    temp2 = raw_data[12]
                raw_sch_time = trans_time(temp1);
                raw_act_time = trans_time(temp2);

                day_delta = 0;
                if (raw_act_time < raw_sch_time and raw_sch_time.tm_hour == 23 and raw_act_time.tm_hour==0):
                    day_delta = 1
                    #跨天,days+1

                raw_data[6] = raw_date + datetime.timedelta(hours=raw_sch_time.tm_hour, minutes=raw_sch_time.tm_min );
                #计划时间
                raw_data[7] = raw_date + datetime.timedelta(days=day_delta,hours=raw_act_time.tm_hour, minutes=raw_act_time.tm_min );
                #实际时间

                if not isinstance(raw_data[2],str):
                    raw_data[2] = str(int(raw_data[2]));
                #航班号转换为字符串

                data = raw_data[2:8] + [raw_data[10]]
                excel_data.append(data);
                
                index+=1;
                raw_data = table.row_values(index);
        return excel_data;

    

if __name__ == "__main__":
    test = _Transfer(os.path.abspath("改航数据汇总--返航备降数据.xls"));
    print(test.data);
   
    
