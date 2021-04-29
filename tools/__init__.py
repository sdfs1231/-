import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 
import config
from _Transfer import _Transfer
from _Database import _Database

if __name__=="__main__":
    '''create_sql = "CREATE IF NOT EXIST "+ table_name+ "(";
    for i in columns[table_name]:
        if i != len(columns[table_name]) -1 :
            create_sql += i + ",";
        else:
            create_sql += i + ") VALUES ";
        
    test_excel = _Transfer(os.path.abspath("改航数据汇总--返航备降数据.xls"));
    test_database = _Database();
    test_database.select_database("改航");
    test_database.insert_datas("改航原始数据表",test_excel.data);
    
    test_database.quit();'''
    
    

if __name__=="tools":
    
    
