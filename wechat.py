from wxpy import *
import datetime

start = "2017/6/7"

date = start.split('/')
year = date[0]
month = date[1]
day = date[2]

d0 = datetime.datetime(int(year),int(month),int(day))
d1 = datetime.datetime.now()


bot = Bot(cache_path=True)

me = bot.self

bot.file_helper.send('login')

group = ensure_one(bot.groups(contact_only=True).search("502"))

name = '502宿舍信誉强-基佬叶的第'+str((d1-d0).days)+'天'
group.rename_group(name)

group.send('成功修改群名为'+name)

