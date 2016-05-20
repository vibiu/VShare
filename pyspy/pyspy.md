# 一只爬虫的修养

## 网络爬虫的定义

参见 [Baidu](http://baike.baidu.com/view/284853.htm)
参见 [Wikipedia](https://zh.wikipedia.org/wiki/網路蜘蛛)

爬虫就是一个自动获得和提取网页或资源的程序，是搜索引擎最重要的组成。

爬虫最基本的技术就是请求页面，分析页面。

更复杂一点的就是表单提交，模拟登陆。

但是爬虫最开始设计出来貌似是用来大范围的对某个站点的资源进行扫描，搜索，克隆。

所以爬虫最终的问题将会是：

+ 对抓取的目标的描述和定义;
+ 对网页或数据的分析与过滤;
+ 对URL的搜索策略。

## 爬虫修养之网页请求

爬虫可以用几乎所有有网络接口的语言实现。比如python,js,c,java,php。甚至是像matlab那样的专门为数学设计的语言。

### 一个简单的node.js实现的爬虫：
    
    var superagent = require('superagent')
    const phoneurl = 'http://www.ncu.edu.cn/zydt/xyhy.htm'
    superagent.get(phoneurl).end(function (err, res) {
        console.log(res.text)
    })
    

node 的http标准库就是http,此外还有各种封装好的node包，比如nodegrass，request，superagent。
每一个都能很好地实现网页的抓取.

### 而python能在一定程度上更优雅地实现：

    import requests
    url = 'http://www.ncu.edu.cn/zydt/xyhy.htm'
    resp = requests.get(url)
    print resp.text

这必须感谢由[kennethreitz](https://github.com/kennethreitz)给我们写了requests，HTTP for human (github地址:[requests](https://github.com/kennethreitz/requests))

要想用灵活地使用requests，有必要通读[request的文档](http://docs.python-requests.org/en/master/)

前段时间我阅读了requests的部分源码，发现正如作者本人所言，注释很清楚，代码也相当pythonic.

### 网页请求的核心技术：

爬虫的技术修养：
+ 了解各种错误（如timeout，connection refuse）
+ 了解实现爬虫的底层，紧跟技术最前沿
+ 了解TCP/IP等网络通信协议

requests的核心技术就是[urllib3](https://urllib3.readthedocs.io/en/latest/),和urllib2一样，我们也可以直接用它进行页面请求。

    import urllib3
    http = urllib3.PoolManager()
    resp = http.request('GET', 'http://www.ncu.edu.cn/zydt/xyhy.htm')
    print resp.data

urllib3的底层，就是socket（也叫套结字），[一篇简要的关于python的socket编程](http://www.jianshu.com/p/e062b3dd110c)，[廖学峰关于python的socket编程介绍](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832511628f1fe2c65534a46aa86b8e654b6d3567c000)

socket就是TCP/IP协议的封装

### 模拟登陆
目前很多网站的登陆验证是靠cookies，先用requests的post提交表单实现登陆，获得服务器分配的cookies，之后的每个请求带上cookies就相当于模拟登陆。

模拟浏览器请求则通过改变请求的head实现，可以直接在chrome中找到。

模拟登陆建议将一次请求抽象成一个用户，使用面向对象编程。

爬虫模拟登陆的修养：

+ 匿名性： 能不用登陆的页面尽量不用登陆
+ 简洁性： 能不用验证的头部尽量不用添加
+ 健壮性： 能处理请求失败的情况，包括应对反爬虫机制

## 爬虫修养之网页解析

获得网页后的处理基本就是：
 
+ print或logging，手工分析或后期写脚本分析
+ 简单的字符串处理存储到数据库等待用户使用
+ Json 或者XML序列化，做成web接口

### 正则表达式

一个强大而且很有用的东西，各种主流语言多少都有正则表达式支持，虽然规则并不多,但是内容足够写好几本书。

关于python的简单的正则表达式运用，可以看下[Python爬虫入门七之正则表达式](http://cuiqingcai.com/977.html), 和[Python中的正则表达式教程](http://blog.csdn.net/pleasecallmewhy/article/details/8929576)，这些都是比较有名的博客，博主自己也写了很多篇关于爬虫的博客。

爬虫的正则修养：

+ 精准性： 尽量缩小匹配的范围，减少误差和干扰(难点)
+ 高效性： 能用一句正则匹配的就不要拆开分步匹配
+ ~~可读性~~： 扯淡，正则表达式一般比较难懂，如果能写的好看点就更好了

### bs4 和cheerio

[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)是现在比较主流的网页解析方法，内部支持多种解析器(html.parser, lxml, lxml-xml, html5lib)，一般我们用html.parser就可以了。
bs4的解析方式相当好理解，可以快速上手，解析速度也不错(和re还是慢比较多的)

[cheerio](https://github.com/cheeriojs/cheerio) 是为服务器特别定制的，快速、灵活、实施的jQuery核心实现，有jq基础的一看就能用，[一份关于cheerio API的翻译](https://cnodejs.org/topic/5203a71844e76d216a727d2e)

爬虫的解析修养：

+ 简单的提取尽量用正则，提高速度
+ 涉及比较复杂的页面，bs4等文档树解析器也是不错的选择
+ 我的想法，是否把正则匹配模板独立成一个模块，优化代码结构？

## 爬虫修养之高级篇

### 多线程

一只爬虫如果能在同一时间干多件事，效率就提高了。用Thread模块

### 分布式（多进程）

[为什么要分布式?](https://www.zhihu.com/question/27457563)

如何分布式？ [scrapy](https://github.com/scrapy/scrapy)([文档](http://doc.scrapy.org/en/latest/))是一个用python写的强大的爬虫工具，比较高级，还不会，据说能实现分布式。
![scrapy](http://cuiqingcai.com/2433.html)
[Cola](https://github.com/chineking/cola)是一个分布式的爬虫框架,没用过。
![colo](http://img.blog.csdn.net/20141217235604129?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY2hkaHVzdA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
主要思想：设计一个合理的url搜索策略，使用中心主机控制分机对站点没命地爬取和存储。

### 突破动态加载

现在很多网站都是用js把内容加载到页面上的，如果直接用curl请求，你很有可能得到几乎是空白的内容。

方法：

+ 人工分析ajax请求，拟合数据自己请求
+ 用js引擎运行js(这点如果用node会方便许多,[CasperJS](http://casperjs.org/), [PhantomJS](http://phantomjs.org/),)，python 有一些搭建js环境的模块，比如[PyV8](https://github.com/emmetio/pyv8-binaries)，PyV8 是 V8引擎的 Python 胶水层，可实现Python与JavaScript的交互。 [一个使用PyV8的demo](http://xwsoul.com/posts/490)
+ 比较有意思的，使用[seleniumhq](https://github.com/SeleniumHQ/selenium)进行纯粹的浏览器模拟

## 爬虫修养之道德修养

爬虫相比于人，可以由更快的检索速度，它们完全有能力使一个站点瘫痪，高强度的爬虫也容易让网站管理员因高额的宽带费而吃土或让主机一直处于高频运转状态，出现当机

所以一只有修养的爬虫就应该为网站管理员着想，可以用sleep方法来设置延迟时间，时间可以是10s或更多，降低请求频率

爬取的时间可以设在晚上，也就是网站正常流量较少的时候，避免打扰正常用户的使用

同时也要关注[robots.txt](https://zh.wikipedia.org/wiki/Robots.txt)，尽量不要抓取管理员不希望被爬虫访问的页面

# end
希望大家愉快的写出有修养的爬虫。
