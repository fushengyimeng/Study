#1.安装scrapy等模块较慢时 可以用国内镜像源来安装
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scrapy(模块名称)
   
  #2. scrapy创建项目流程
    - scrapy startproject first  创建项目
    - scrapy genspider spiderName xxx.com 创建爬虫源文件
    - scrapy crawl spiderName 启动爬虫项目
   
  #3. settings.py 项目配置文件 
      pipelines.py 管道文件 通常用来链接数据库 插入数据
      middleware.py 中间件文件 通常用来自定义中间件 如代理中间件、异常捕获中间件
      items.py item文件 通常用来申明数据字段
      
  #4. 要存储数据时 settings.py中的ITEM_PIPELINES要打开
  #5. 重写start_requests方法
  #6. pipelines.py中 可批量插入 提高数据插入性能 将传过来的item对象 
        先放入到一个对象中 判断该对象的长度 当该对象长度达到指定长度时 再执行插入操作