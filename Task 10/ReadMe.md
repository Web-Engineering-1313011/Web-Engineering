# 介绍

## 如何工作

code.py 主要用于启动，绝大部分时候它是没有用的。

/static 这个是静态文件目录，在内置的开发服务器上不可以修改，如果你使用其他 web server 来配置的是可以改的。

/controllers 控制层的代码，或者实际工作的代码就在这里。

__init__.py 这是用来做什么的？看起来像初始化？嗯… 如果你希望某个目录可以被引用，加上这个一样空白文件就好了，表示当前是一个模块可以被引用。这是给新手做的说明。

/config 一些常用配置，我把 url 的配置独立出来了，因为项目做大了，url 很长。

我取消了 model 层，不要问我为什么，这是一个很纠结的话题，如果你需要，你可以独立出一个 model 层。

其他的应该不用解释了。

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