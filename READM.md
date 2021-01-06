## 一.环境配置
1.VSCode下载 安装puthon，chinese，nom，npm intellisence，Vetur，Vue3，Snippts，vscode-icons,live server这些插件
2.配置终端
切换到cmd
3.安装前端开发工具HbuilderX https://www.dcloud.io/hbuilderx.html
4.安装小程序开发工具 https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html


## 二。安装git：https://git-scm.com/'
1.创建原创仓库myBlog
2.初始化本地仓库，也就是在本地的myBlog文件下执行：git init 执行完后会创建一个。git的隐藏文件
3.远程仓库和本地仓库进行关联：git remore add origin“你的远程仓库地址”
4.如果出现错误，ssh没有创建
5.先去创建密钥：ssh-keygen，一路enter，生成密钥
6.查看生成的密钥cat-/。ssh/id_rsa.pub.将密钥写入到github上的settings下的SSH and GPG keys下
7.推送四步骤：
git status   查看发生变化的文件
git add .  追踪所有发生变化的文件
git  commit -m "备注"
git push -u origin master   第一次提交
git push


## 三.创建myBlog项目
1空文件夹下，执行django-admin startproject myBlog
2.给myBlog创建虚拟环境，使用：python-m venv env
3.进入到虚拟环境，windows下：.\\env\\Scripts\\activate;
4.退出虚拟环境，windows下，deactivate；
5.室友vsCode打开myBlog，执行：python manage.py startapp articles

## 四.创建articles的models
1.创建model
2.数据库同步
3.在admin.py中注册model

## 五.业务逻辑
1.文章列表页.分页
2.文章详情页.评论
3.全局搜索功能 Q对象
4.最新文章，最新评论的排行
5.按照分类，标签的一个聚类操作
6.联系我页面，发送邮件 

## 六、将所有app归拢到apps文件夹下
import sys
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
1. 如何加载静态页面  os.path.join(BASE_DIR,'templates')   
os.path.join(BASE_DIR,'static')网上图片不需要解析  加标签  
2. 在settings.py文件中注册静态页面和templates模板  创建公共模板进行继承extends 实现模板复用   
将公共内容base.html父类模板/aside.html侧边栏写入common文件夹中实现模板复用减少冗余代码的写入  嵌套复用模板 include 
3. 注册静态内容 {% load static %}  css/js   继承父类模板 {%extends 'common/base.html'%}   {%include 'common/aside.html'%}
4. 数据展示在前端上用模板语法 {{}} 
循环语句 {% for i in articles %} {{ i }} {% endfor %}  判断语句 {% if  true %} {{i}} {% endif %}
5. 前端页面数据展示是来自views.py中的参数 也就是数据库中

## 七.评论和集成markdownfy插件
django-contrib-comments
django-markdownfy