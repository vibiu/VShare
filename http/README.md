# HTTP协议
HTTP 是基于 TCP/IP 协议的应用层协议, 主要规定了客户端和服务器之间的通信格式，默认使用80端口。
see more:

[HTTP协议详解](http://www.cnblogs.com/li0803/archive/2008/11/03/1324746.html)

[阮一峰 - HTTP 协议入门](http://www.ruanyifeng.com/blog/2016/08/http.html)

[简书 - Http协议详解](http://www.jianshu.com/p/e83d323c6bcc)

## URL
包括协议名称, 主机地址, 资源地址, 端口(HTTP 默认端口 80)

基本形式:

    http://host[":"port][abs_path]
    https://host[":"port][abs_path]

正则表达式:

    ((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?

例子:

    http://us.ncuos.com/api/500

## 请求(request)

### GET 请求

curl命令:

    curl -v http://us.ncuos.com/api/test/500

请求内容:

    GET /api/test/500 HTTP/1.1
    HOST: us.ncuos.com
    User-Agent: curl/7.51.0

解释:

    // 请求方式 | 资源地址 | HTTP协议版本
    // 远程服务地址
    // 客户端代理

我们写的爬虫就是模拟了一个真实的请求过程, 发送的信息和上面差别不大, 但是 requests 库为自动封装好了请求.

    request.get('http://us.ncuos.com/api/500', headers={'User-Agent': 'curl/7.51.0'})

    // 请求方式 | URL | 头部

### POST 请求

curl命令:

    curl -v --header "Content-Type:application/json" \
        --data '{"username": "test", "password": "test"}' \
        http://us.ncuos.com/api/user/login

请求内容:

    POST /api/user/login HTTP/1.1
    HOST: us.ncuos.com
    User-Agent: curl/7.51.0
    Accept: */*
    Content-Type: application/json
    Content-Length: 47

    {"username": "test", "password": "test"}

解释:

    // 请求方式 | 资源地址 | HTTP协议版本
    // 远程服务地址
    // 客户端代理
    // 客户端允许接受的 MIME 类型
    // 请求体格式
    // 请求体长度

    // 请求体内容

see more:

(阮一峰 - curl网站开发指南)[http://www.ruanyifeng.com/blog/2011/09/curl.html]

## response(响应)

响应内容:

    HTTP/1.1 403 FORBIDDEN
    Server: nginx/1.4.6 (Ubuntu)
    Date: Wed, 16 Nov 2016 11:11:11 GMT
    Content-Type: application/json, charset=utf-8
    Content-length: 74
    Connection: keep-alive
    Vary: Accept-Encoding

    {"error": "UserNotExists", "status": 403, "mssage": "该用户不存在"}

响应解释:

    // 请求方式 | 资源地址 | HTTP协议版本
    // 远程服务应用签名
    // 响应时间
    // 响应格式
    // 响应长度
    // 保持链接
    // 告知缓存服务器按照 Accept-Encoding 字段的内容，分别缓存不同的版本

    // 响应体内容

flask 框架提供的服务就是对请求体和响应体的封装

    import json
    from flask import Flask, Response


    app = Flask(__name__)

    @app.route('/api', methods=['GET'])
    def get_api():

        data = json.dumps({
            "error": "UserNotExists",
            "status": 403,
            "mssage": "该用户不存在"
        })
        resp = Response(response=data,
            status=500,
            mimetype="application/json")
        return resp

see more:
(Jerry Qu - HTTP 协议中 Vary 的一些研究)[https://imququ.com/post/vary-header-in-http.html]

(List of HTTP header fields)[https://en.wikipedia.org/wiki/List_of_HTTP_header_fields]
