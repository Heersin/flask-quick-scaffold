# Flask-Quick-Scaffold

## 简介
本项目基于flask-adminlte-handler项目进行二次开发，完善了一些常用的功能，目的是能够快速搭建一个用于展示的小型demo项目。其中将数据库转为sqlite3，简化开发中数据库方面的问题。

## 新加入效果
### 前台首页
![https://github.com/Heersin/flask-quick-scaffold/blob/master/log/index.jpg]
### 注册
![https://github.com/Heersin/flask-quick-scaffold/blob/master/log/reg.png]
### 上传文件
![https://github.com/Heersin/flask-quick-scaffold/blob/master/log/upload.png]
 

## 项目结构
- /app 代码部分
    - /templates 项目的模板文件及html文件
    - /main 前台的视图
    - /auth 处理登录注册的视图
    - /errors 出错视图
    - /admin 后台视图
    - /static 项目静态文件
    - /upload_data 存放上传数据处
    - utils.py 原项目自带工具
    - models.py 数据库相关
- /conf 配置
- /log 日志
- run_app_dev.py 启动器


## 安装
推荐使用虚拟环境virtualenv
```
# For Linux
mkdir venv
virtualenv venv
source venv/bin/activate

# For Windows
mkdir venv
virtualenv venv
venv/Scripts/activate
```

启动虚拟环境后安装本项目依赖
```
pip install -r requirements.txt
```
修改配置文件conf/log-app.conf，将日志文件路径修改为相应路径
```
args=('/path/to/log/flask-rest-sample.log','a','utf8')
```

## 启动
```
python run_app_dev.py
```
若部署于远程服务器，需要自行修改为production配置。或是利用ssh端口转发，使本机能够访问远程服务器

## 声明
本项目素材大量来源于pixaday，且前端界面使用了Fonik模板的部分内容。
