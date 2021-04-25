import os
from _Transfer import _Transfer
from _Database import _Database



if __name__=="__main__":
    test_excel = _Transfer(os.path.abspath("改航数据汇总--返航备降数据.xls"));
    test_database = _Database();
    test_database.select_database("改航");
    test_database.insert_datas("改航原始数据表",test_excel.data);
    test_database.quit();
    
