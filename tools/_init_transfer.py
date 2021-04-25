import os
from _Transfer import _Transfer
from _Database import _Database

tables = ["改航原始数据表","延误表","机场信息表","用户表"];
columns = {"改航原始数据表":["id","flt_number","tof_3airport","arv_3airport","airroute","sch_time","act_time","remarks"],
           "延误表":["id","is_delay","delay_mins"],
           "机场信息表":["id","3airport","4airport"],
           "用户表":["id","name","password","permition"]};

if __name__=="__main__":
    create_sql = "CREATE IF NOT EXIST "+ table_name+ "(";
    for i in columns[table_name]:
        if i != len(columns[table_name]) -1 :
            create_sql += i + ",";
        else:
            create_sql += i + ") VALUES ";
        
    test_excel = _Transfer(os.path.abspath("改航数据汇总--返航备降数据.xls"));
    test_database = _Database();
    test_database.select_database("改航");
    test_database.insert_datas("改航原始数据表",test_excel.data);
    test_database.quit();
    
