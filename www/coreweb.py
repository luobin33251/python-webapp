import asyncio,os,inspect,logging,functools

from urllib import parse

from aiohttp import web

from apis import APIError

#get的装饰器，通过@get使用
def get(path):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			return func(*args,**kw)
		wrapper.__method__='GET'
		wrapper.__route__=path
		return wrapper
	return decorator

#post的装饰器，通过@post使用
def post(path):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			return func(*args,**kw)
		wrapper.__method__='POST'
		wrapper.__route__=path
		return wrapper
	return decorator

#URL请求处理类
class RequestHandler(object):
	def __init__(self,app,fn):
		self._app=app
		self._func=fn
		self._has_request_arg=app
		self._has_var_kw_arg=app
		self._has_named_kw_args=app
		self._named_kw_args=app
		self._required_kw_args=app

