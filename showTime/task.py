# -*- coding:utf8 -*-
import time
import celery
from celery import task
from celery.schedules import crontab

app = celery.Celery('cele', broker='redis://localhost:6379')


@task
def sayHello():
    print ("hello...")
    time.sleep(3)
    print ('world...')


'''
设置执行的时间
 '''
# 每分钟执行一次
c1 = crontab()

# 每天凌晨十二点执行
c2 = crontab(minute=0, hour=0)

# 每十五分钟执行一次
crontab(minute='*/15')

# 每周日的每一分钟执行一次
crontab(minute='*', hour='*', day_of_week='sun')

# 每周三，五的三点，七点和二十二点没十分钟执行一次
crontab(minute='*/10', hour='3,17,22', day_of_week='thu,fri')

app.conf.beat_schedule = {
    'send-every-10-seconds': {
        'task': 'task.sayHello',  # 调用要定时执行的函数
        'schedule': 10.0,  # 定时执行的时间
        'args': ()  # 定时执行的函数的参数
    },
}