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
    
    if db.show_record_nums("改航原始数据表")[0] == 0:
       #若原始数据表没有数据 需要从excel表中插入数据
       for data in transfer.data:
           str_sch = data[4].strftime("%Y-%m-%d %H:%M");
           str_act = data[5].strftime("%Y-%m-%d %H:%M");
           delays = 0;
           if data[5] > data[4] and (data[5] - data[4]).seconds/60 >30:
               delays = (data[5] - data[4]).seconds / 60;
           
           sql = "INSERT INTO 改航原始数据表"+" (flt_number,tof_3airport,arv_3airport,airroute,sch_time,act_time,delay_time,remarks)"\
                      " VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"%\
                      (data[0],data[1],data[2],data[3],str_sch,str_act,delays,data[6]);
           
           db.insert_data("改航原始数据表",sql);
    print("原始数据转移完成...");
    
    db.quit();
    
    
