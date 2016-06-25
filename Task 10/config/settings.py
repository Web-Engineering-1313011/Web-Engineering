#!/usr/bin/env python
# coding: utf-8
import web

db = web.database(dbn='mysql', db='todo', user='root', pw='157003')

render = web.template.render('templates/', cache=False)

web.config.debug = True

config = web.storage(
    email='gaohs7815@icloud.com',
    site_name = 'TODO',
    site_desc = '',
    static = '/static',
)


web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
