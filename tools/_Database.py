#mysql版数据库
import pymysql
import hashlib
import configparser
from datetime import datetime;

class _Database:
    def __init__(self):
        try:
            self.conn = pymysql.connect(host="127.0.0.1",user=input("请输入用户名："), password=input("请输入密码："),charset = "utf8",port=3306);
        except Exception as E:
            print("链接数据库失败")
            print(E);
        self.cursor = self.conn.cursor();
        

    def _execute(self, sql_command):
        try:
            self.cursor.execute(sql_command + ";");
        except pymysql.err.ProgrammingError as E:
            print(E);
        except pymysql.err.OperationalError as E:
            print(E);

    def _show_databases(self):
        self._execute("show databases");
        res = self.cursor.fetchall();#tupel中的tupel
        return res;

    def isexist_database(self,database):
        res = self._show_databases();
        for t in res:
            if database == t[0]:
                return True;
        return False;

    def _create_database(self,database_name):
        res = self._show_databases();
        flag = False;
        for db in res:
            if database_name == db[0]:
                flag = True;
                break;
        if not flag:
            print("创建数据库:",database_name,"...");
            sql = "CREATE DATABASE "+ database_name;
            self._execute(sql);
            print("创建成功");

    def select_database(self,database):
        self._execute("USE "+ database);
        self.conn.commit();#一定要 commit 才能选择某个表

    def _show_tables(self,database):
        self.select_database(database);
        sql = "show tables";
        self._execute(sql);
        res = self.cursor.fetchall();
        return res;

    def isexist_table(self,database,table):
        tables = self._show_tables(database);
        for t in tables:
            if table == t[0]:
                return True;
        return False;

    def create_table(self,database,table,create_table_sql):
        if not self.isexist_table(database,table):
            self._execute(create_table_sql);
        else:
            print(table,"已经存在");

    def insert_datas(self,table_name,data):
        # list类型
        if isinstance(data[0],list):
            for i in data:
                str_sch = i[4].strftime("%Y-%m-%d %H:%M");
                str_act = i[5].strftime("%Y-%m-%d %H:%M");
                sql = "INSERT INTO "+ table_name +" (flt_number,tof_3airport,arv_3airport,airroute,sch_time,act_time,remarks)\
                       VALUES ('%s','%s','%s','%s','%s','%s','%s')"%\
                       (i[0],i[1],i[2],i[3],str_sch,str_act,i[6]);
                self._execute(sql);
            print("载入完成");
            self.conn.commit();
        
        #dict类型

    def insert_data(self,table_name,data):
        #插入一条数据
        if isinstance(data,list):
        
            str_sch = data[4].strftime("%Y-%m-%d %H:%M");
            str_act = data[5].strftime("%Y-%m-%d %H:%M");
            sql = "INSERT INTO "+ table_name +" (flt_number,tof_3airport,arv_3airport,airroute,sch_time,act_time,remarks)\
                       VALUES ('%s','%s','%s','%s','%s','%s','%s')"%\
                       (data[0],data[1],data[2],data[3],str_sch,str_act,data[6]);
            self._execute(sql);
            print("载入完成");
            self.conn.commit();

    def quit(self):
        self.conn.close();
        
        
        
            

if __name__=="__main__":
    test = _Database();
    #test._show_databases();
    print(test._show_tables("改航"));
    table_name = "";
    print(test.isexist_table("改航","改航原始数据表"));
    #test._create_database();
    #test._create_tables("改航","改航原始数据表");
    
    
    
        
