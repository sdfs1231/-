#mysql版数据库
import pymysql
import hashlib
import configparser
from datetime import datetime;


class _Database:
    def __init__(self,database_name):
        try:
            self.conn = pymysql.connect(host="127.0.0.1",user=input("请输入用户名："), password=input("请输入密码："),charset = "utf8",port=3306);
        except Exception as E:
            print("链接数据库失败,",end="")
            print(E);
        else:
            
            self.cursor = self.conn.cursor();
            self._select_database(database_name);
    
    def _execute(self, sql_command):
        try:
            self.cursor.execute(sql_command + ";");
        except pymysql.err.ProgrammingError as E:
            print(E);
            return 0;
        except pymysql.err.OperationalError as E:
            print(E);
            return 0;
        return 1;

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
        flag = self.isexist_database(database_name);
        if not flag:
            print("创建数据库:",database_name,"...");
            sql = "CREATE DATABASE "+ database_name;
            if self._execute(sql):
                print("创建数据库成功");
            else:
                print("创建数据库失败")
        self._select_database(database_name);

    def _select_database(self,database):
        if self.isexist_database(database):
            if self._execute("USE "+ database):
                self.conn.commit();#一定要 commit 才能选择某个表
                print("选择"+database+"数据库");
                self.database_name = database;
            else:
                print("选择数据库失败")
                self.database_name = None;
        else:
            self._create_database(database);

    def _drop_database(self):
        command = input("是否删除数据库? y or n");
        if command == "y":
            self._execute("DROP DATABASE IF EXISTS " + self.database_name);
            print("删库成功 赶紧跑路");

    def show_tables(self):
        sql = "show tables";
        self._execute(sql);
        res = self.cursor.fetchall();
        return res;

    def isexist_table(self,table):
        tables = self.show_tables();
        for t in tables:
            if table == t[0]:
                return True;
        return False;

    def create_table(self,table,create_table_sql):
        #创建表格 成功返回1 失败返回0
        if not self.isexist_table(table):
            return self._execute(create_table_sql)
        else:
            return 1;

    def drop_table(self,table):
        if self.isexist_table(table):
            sql = "DROP TABLE IF EXISTS "+table;
            return self._execute(sql);
        return 0;

    def truncate_table(self,table):
        if self.isexist_table(table):
            sql = "TRUNCATE TABLE "+table;
            return self._execute(sql);
        return 0;

    def delete_table(self,table):
        if self.isexist_table(table):
            sql = "DELETE FROM "+table +" WHERE id >0";
            return self._execute(sql);
        return 0;

    def show_record_nums(self,table_name):
        sql = "SELECT count(*) from " + table_name;
        self._execute(sql);
        return self.cursor.fetchone();

    def _init_data(self,data):
        pass

##    def insert_datas(self,table_name,sql):
##        # list类型
##        if isinstance(data[0],list):
##            for i in data:
##                str_sch = i[4].strftime("%Y-%m-%d %H:%M");
##                str_act = i[5].strftime("%Y-%m-%d %H:%M");
##                sql = "INSERT INTO "+ table_name +" (flt_number,tof_3airport,arv_3airport,airroute,sch_time,act_time,remarks)\
##                       VALUES ('%s','%s','%s','%s','%s','%s','%s')"%\
##                       (i[0],i[1],i[2],i[3],str_sch,str_act,i[6]);
##                self._execute(sql);
##            print("载入完成");
##            self.conn.commit();
        
        #dict类型 TODO

    def insert_data(self,table_name,sql):
        #插入一条数据
        
            #str_sch = data[4].strftime("%Y-%m-%d %H:%M");
            #str_act = data[5].strftime("%Y-%m-%d %H:%M");
            #sql = "INSERT INTO "+ table_name +" (flt_number,tof_3airport,arv_3airport,airroute,sch_time,act_time,remarks)\
                      # VALUES ('%s','%s','%s','%s','%s','%s','%s')"%\
                       #(data[0],data[1],data[2],data[3],str_sch,str_act,data[6]);
        self._execute(sql);
        self.conn.commit();

    def quit(self):
        self.conn.close();
        
        
        
            

if __name__=="__main__":
    test = _Database("改航");
    #test._show_databases();
    print(test._show_tables());
    print(test.isexist_table("改航原始数据表"));
    print(test.show_record_nums("改航原始数据表"));
    #test._create_database();
    #test._create_tables("改航","改航原始数据表");
    
    
    
        
