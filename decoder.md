#解决编码问题
***
*   尽早将字符串转为unicode
*   在sublime中默认以utf-8的形式输出，所以要用encode('utf-8')将unicode转成sublime可输出
*   在cmd中默认以gbk的形式输出，所以要用encode('gbk')/encode('gb2312')/encode('gb18030')将unicode转成sublime可输出
*   最后输出时候才将unicode转为相应编码
***  
 old = u'\xe9\xa2\x98\xe5\x90\x8d/\xe8\xb4\xa3\xe4\xbb\xbb\xe8\x80\x85:'

    ''.join([chr(ord(x)) for x in old])

***
s='\u554a\u54c8'
    s.decode('unicode-escape')

or like this:
    u = eval('u\'' + s +'\'')
***
html = '&lt;abc&gt;'
    import HTMLParser
    html_parser = HTMLParser.HTMLParser()
    txt = html_parser.unescape(html)

escape:
    import cgi
    html = cgi.escape(txt)
