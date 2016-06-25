# 介绍

## 如何工作

code.py 主要用于启动。

/static 这个是静态文件目录，在内置的开发服务器上不可以修改，如果你使用其他 web server 来配置的是可以改的。

/controllers 控制层的代码，或者实际工作的代码就在这里。

__init__.py 作用是如果你希望某个目录可以被引用，加上这个一样空白文件就好了，表示当前是一个模块可以被引用。

/config 一些常用配置。

开发使用了python 2.7.10 with web.py & MySQLdb.py，数据库用的 mySQL，你们可以自己建todo库，建todo表。

## URL 配置

```python
pre_fix = 'controllers.'

urls = (
    '/',                    pre_fix + 'todo.Index',
    '/todo/new',            pre_fix + 'todo.New',
    '/todo/(\d+)',          pre_fix + 'todo.View',
    '/todo/(\d+)/edit',     pre_fix + 'todo.Edit',
    '/todo/(\d+)/delete',   pre_fix + 'todo.Delete',

)
```

前面的访问地址对应后面的方法路径。好多重复的字符串，所以我就把前面的弄成一个变量了。

大部分时候简单的正则可以适用你的常规应用了，数字用 (\d+)，字符串用 (.*) 。