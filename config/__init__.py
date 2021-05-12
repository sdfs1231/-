import os
import sys
import configparser

if __name__=="config":
    file_path = os.path.realpath(__file__);
    dir_path = os.path.dirname(file_path);
    project_path = os.path.dirname(dir_path);

    config_file = os.path.join(dir_path,"config.ini")

    config = configparser.ConfigParser();

    with open(config_file,"w+",encoding="utf-8") as cf:
        
        #初始化参数
        
        config.read(cf);
            
        config["Path"] = {};
        config["Database"] = {};
        config["Path"]["root_path"] = project_path; #项目路径
        #数据库
        config["Database"]["DBname"] = "改航";
        config["Tables"] = {};
        config["Tables"]["改航原始数据表"] = "id,flt_number,tof_3airport,arv_3airport,airroute,sch_time,act_time,delay_time,remarks";
        config["Tables"]["机场三四码表"] = "id,3airport,4airport";
        config["Tables"]["用户表"] = "id,name,password,auth";
        
        
        #网站

        config.write(cf);
        print("config.ini初始化完成");

    

        
        
        
        
        
