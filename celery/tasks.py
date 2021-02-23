from celery import Celery

# 第一个参数 是当前脚本的名称，第二个参数 是 broker 服务地址
app = Celery('tasks', backend='redis://:021808..@123.207.147.235/3', broker='redis://:021808..@123.207.147.235/3')


@app.task
def add(x, y):
    return x + y
