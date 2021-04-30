import os
import sys
import config
import configparser
from tools._Database import _Database
from tools._Transfer import _Transfer

if __name__ == "__main__":
    print("初始化config");
    config = configparser.ConfigParser();
    config.read("config"+os.path.sep+"config.ini",encoding="utf-8");

    print("初始化数据库");
    database_name = config["Database"]["DBname"];
    db = _Database(database_name);
    
    for table in config["Tables"]:
        if not db.isexist_table(table):
            #db不存在table
            columns = config["Tables"][table].split(",");
            y = "";
            for i,x in enumerate(columns):
                a = input("请输入"+table+"表"+x+"属性 ");
                r = input("请输入"+table+"表"+x+"需求,以空格分割");
                y += x + " " + a +" " + r +",";
            pk = input("选择主键 ");
            fk_r = input("是否选择外键: y or n");
            if fk_r =="y":
                fk = input("选择外键 ");
                fk_t = input("选择关联表 ");
                fk_pk = input("选择关联表pk");
                sql = "CREATE TABLE IF NOT EXISTS "+ table + "(" +\
                       y + " PRIMARY KEY( "+pk+"), FOREIGN KEY( "+fk+") REFERENCES "+fk_t+"("+fk_pk+")"+")" ;
            else:
                sql = "CREATE TABLE IF NOT EXISTS "+ table + "(" +\
                      y + " PRIMARY KEY("+pk+")"+")" ;
            db.create_table(table,sql)
        

    print("数据转换");
    transfer = _Transfer(".\excels\改航数据汇总--返航备降数据.xls");
    
    db.quit();
    
    
