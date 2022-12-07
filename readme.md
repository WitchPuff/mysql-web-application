# mysql-web-application

基于[数据库实验10](https://www.db-book.com/university-lab-dir/exercises-dir/servlet.html)完成，实现一个简易的网页交互应用，能连接本地数据库进行查询、修改等操作，并显示查询结果。

环境：Python + Django + mysql

基础的网页实现了如下功能模块：

1. 学生查询（输入学号查询）
2. 课程查询（输入课程关键字模糊查询）
3. 有两次或以上挂科记录的学生查询
4. 新学生注册
5. 新教职员工注册

在注册模块中，创建用于为学生和教师表插入记录的表单接口，并使用一个下拉菜单作为系名，显示所有有效的系名。

## 运行方式

默认Python + Django + mysql环境已经配置好了，连接的是本地数据库（db-book官网的大学数据库模板），数据库结构定义在`DDL.sql`中，导入数据可以选择`largeRelationsInsertFile.sql`或`smallRelationsInsertFile.sql`。

克隆仓库：
```
git clone https://github.com/WitchPuff/mysql-web-application
cd mysite
```

可以在`/mysite/mysite/settings.py`中修改连接的数据库（需要事先在本地创建数据库）：

```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
          'ENGINE':'django.db.backends.mysql',
          'NAME':'university', # your database
          'USER':'root',
          'PASSWORD':'test',
          'HOST':'localhost',
          'PORT':'3306',
    }
}
```

如果想使用你自己的本地数据库，可以用这条命令生成新的模板。

```
python manage.py inspectdb > <your app name>/models.py
```

数据库迁移：

```
python manage.py makemigrations
python manage.py migrate
```

再在`mysite/uni/views.py`中修改对应models的接口及对应html文件即可。

运行网页：

```
cd mysite
python manage.py runserver
```

访问http://127.0.0.1:8000

## 效果展示

### HOME PAGE

![image-20221130174628207](https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202211301746389.png)

### STUDENT QUERY

<img src="https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202211301753010.png" alt="image-20221130175335824" style="zoom:50%;" />

### COURSE QUERY

<img src="https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202211301755892.png" alt="image-20221130175510705" style="zoom:50%;" />

### FAILED QUERY

<img src="https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202211301757801.png" alt="image-20221130175711620" style="zoom:50%;" />

### REGISTER

<img src="https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202211301828854.png" alt="image-20221130182800770" style="zoom:50%;" />

<img src="https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202211301828496.png" alt="image-20221130182815420" style="zoom:50%;" />

<img src="https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202211301833372.png" alt="image-20221130183349302" style="zoom:50%;" />

<img src="https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202211301833936.png" alt="image-20221130183357857" style="zoom:50%;" />
