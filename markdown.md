#leran study

><div>#!usr/bin/env python</div>
><div>#coding: utf-8</div>

***
-   try to use markdown
-   try to use github
-   try to use flask
-   try to use MySQL
***
+   try to read tutorial
+   try to find object
+   try to be pythonic
***
>1.  syntax
>2.  semantics
>3.  idioms
>4.  libraries
>5.  tools

---------------------------------------

##python code
***
*   moudle = ['os','sys','math','requests','bs4']
*   decodes = ['utf-8','gbk','ISO-8859-1','gb18030','gb2312']
*   encodes = ['gbk', 'utf-8']
* * *
not good

    def add_end(L=[]):
    L.append('END')
    return L
***
better

    def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
*****
normal codes:

   ` alist = []
    for i in range(10):
        alist.append(i)`
- - -
list comprehension:

    [i for i in range(10)]

---------------------------------------

##for links:

This is [an example][id] reference-style link.

[id]: http://example.com/  "Optional Title Here"

[foo]: http://example.com/  "Optional Title Here"

[foo]: http://example.com/  'Optional Title Here'

[foo]: http://example.com/  (Optional Title Here)

I get 10 times more traffic from [Google][] than from
[Yahoo][] or [MSN][].

  [google]: http://google.com/        "Google"
  [yahoo]:  http://search.yahoo.com/  "Yahoo Search"
  [msn]:    http://search.msn.com/    "MSN Search"

[id]: http://example.com/longish/path/to/resource/here
    "Optional Title Here"

---------------------------------------

##emphasize
*single asterisks*

_single underscores_

**double asterisks**

__double underscores__

\*this text is surrounded by literal asterisks\*

---------------------------------------

##code
Use the `printf()` function.

``There is a literal backtick (`) here.``

A single backtick in a code span: `` ` ``

A backtick-delimited string in a code span: `` `foo` ``

Please don't use any `<blink>` tags.

`&#8212;` is the decimal-encoded equivalent of `&mdash;`.

![Alt text](https://avatars1.githubusercontent.com/u/15816854?v=3&s=460 "Optional title")

---------------------------------------

[markdown text](http://wowubuntu.com/markdown/)

[vibiu's git](https://github.com/vibiu)

See my [Vibiu-s-python](https://github.com/vibiu/vibiu-s-python) page for details.
<div class="footer">
    &copy; 2015 Vibiu Corporation
</div>



