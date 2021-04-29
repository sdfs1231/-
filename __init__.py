import os
import sys
import config
import configparser
from _Database import _Database

if __name__ == "__main__":
    config = configparser.ConfigParser();
    config.read("config"+os.path.sep+"config.ini",encoding="utf-8");
    
    database_name = config["Database"]["DBname"];

    db = _Database(database_name);
    
    for table in config["Tables"]:
        columns = config["Tables"][table].split(",")
        #sql = "CREATE TABLE IF NOT EXISTS "+ table + "(" +\
              #lambda x+",":for x in columns + ")" + "VALUES ("+\
              
        db.create_table()
