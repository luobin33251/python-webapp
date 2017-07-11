import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web
from jinja2 import Environment, FileSystemLoader
import orm
from coreweb import add_route, add_static

def index(request):
	return web.Response(body=b'<h1>Hello</h1>')

async def response_factory(app,handler):
	async def response(request):
		logging.info('Response handler')
		r=await handler(request)
		if isinstance(r,web.StreamResponse):
			return r
		if isinstance(r,bytes):
			resp=web.Response(body=r)
			resp.content_type='application/octet-stream'
			return resp
		

def datetime_filter(t):
	delta=int(time.time()-t)
	if delta < 60:
		return u'1分钟前'
	if delta < 3600:
		return u'%s分钟前'(delta//60)
	if delta < 86400:
		return u'%s小时前'(delta//3600)
	if delta < 604800:
		return u'%s天前'(delta//86400)
	dt=datetime.fromtimestamp(t)
	return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)

@asyncio.coroutine
async def init(loop):
	await orm.create_pool(loop=loop,host='127.0.0.1',port='3306',user='root',password='123456',ad='python_blog')

	app=web.Application(loop=loop,middlewares=[
		logger_factory,response_factory
	])
	init_jinja2(app,filters=dict(datetime=datetime_filter))
	add_routes(app, 'handlers')
	add_static(app)
	srv=await loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()