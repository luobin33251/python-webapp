from models import User, Blog, Comment
from orm import Model,StringField,IntegerField
from orm import create_pool
import asyncio

async def test_save():
	u=User(id=9,name='luobin5')
	row=await u.save()
	print(row)

async def test_update():
	u=User(id=9,name='luobin9')
	row=await u.update()
	print(row)

async def test_remove():
	u=User(id=9)
	row=await u.remove()
	print(row)

async def test_find():
	u=User(id=9)
	row=await u.remove()
	print(row)

async def test_save_user():
	u=User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
	row=await u.save()
	print(row)

loop = asyncio.get_event_loop()
loop.run_until_complete(create_pool(loop, user="root", password="123456", db="python_blog"))
loop.run_until_complete(test_save_user())