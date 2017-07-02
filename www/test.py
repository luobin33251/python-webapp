from orm import Model,StringField,IntegerField
from orm import create_pool
import asyncio

class User(Model):
	__table__='user'
	id=IntegerField(primary_key=True)
	name=StringField()

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
loop = asyncio.get_event_loop()
loop.run_until_complete(create_pool(loop, user="root", password="123456", db="test"))
loop.run_until_complete(test_remove())