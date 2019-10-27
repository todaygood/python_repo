#!/bin/python3
#coding:utf-8

import time
from celery import Celery
 
app = Celery('tasks',backend='redis://localhost:6379/0',broker='redis://localhost:6379/0') 

@app.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')

if __name__ == '__main__':
    sendmail.delay(dict(to='jhu_com@qq.com'))
