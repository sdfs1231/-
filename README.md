# 改航数据库
## python改造excel数据表成数据库，在网页中呈现并操作

### 1- 数据库  
  1.1- 原始数据表（pk-序号（int） 航班号(char(4)) 起飞机场(char(3)) 到达机场(char(3)) 实际航路(char(5)) 计划起飞时间(datetime) 实际起飞时间(datetime) remarks(text)）  
  2.1- 延误表（pk-序号(int) 航班id（外键关联原始数据表）(int) 是否延误(bool) 延误时间(int)）  
  3.1- 机场信息表（pk-序号(int) 三字码(char(3)) 四字码(char(4))）  
  4.1- 用户表（pk-员工号(int,注意不是自增) 姓名(varchar(45)) 密码(varchar(45)) 权限(varchar(45)默认all)）  

### 2- 网页操作  
  2.1- 登录界面  
  2.2- 注册界面  
  2.3- 个人信息界面  
  2.4- 主界面（查询功能，插入功能，信息查询功能）  

### 3- 其他  
  3.1- 初始化操作工具（数据迁移）  
       利用python中的xlwr讲excel数据初始化到sql中  
  3.2- 后端cmd-line界面  
