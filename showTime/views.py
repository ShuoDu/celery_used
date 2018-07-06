from django.shortcuts import render
from django.http import HttpResponse
from task import *

'''
@task 多线程任务
sudo redis-server /etc/redis/redis.conf 启用redis负责任务与执行之间的消息传输
python manage.py celery worker 启用worker执行task任务

'''


def sayhello(request):
    # print('hello ...')
    # import time
    # time.sleep(10)
    # print('world ...')

    sayHello.delay()  # 调用

    return HttpResponse("hello world")

