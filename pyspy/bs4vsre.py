import requests
import time
from functools import wraps
import re
from bs4 import BeautifulSoup

def timer(func):
    @wraps(func)
    def wrapper(*kw,**kwargs):
        before = time.time()
        func(*kw,**kwargs)
        after = time.time()
        print 'use', after-before
    return wrapper


@timer
def bs4parse(resp):
    soup = BeautifulSoup(resp, 'lxml')
    print soup.title

@timer
def reparse(resp):
    mat = re.search('<title>(.+?)</title>',resp)
    print mat.groups()[0]



if __name__ == '__main__':
    url = 'http://www.ncu.edu.cn/zydt/xyhy.htm'
    resp = requests.get(url)
    # print resp.content
    reparse(resp.content)
    bs4parse(resp.content)
