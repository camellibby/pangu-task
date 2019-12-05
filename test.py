import time

from pangu_task import task


def init():
    print('init event!')


def callback():
    print('callback event!')


@task(init=init, callback=callback)
def click1(a, b):
    print("click1 function with ({0},{1}) start".format(a, b))
    i = 0
    while i < 10:
        print("click1 is running: {0}".format(i))
        i = i + 1
        time.sleep(1)
    print("click1 function with ({0},{1}) finished".format(a, b))


@task(init=init, callback=callback)
def click2(a, b):
    print("click2 function with ({0},{1}) start".format(a, b))
    i = 0
    while i < 3:
        print("click2 is running: {0}".format(i))
        i = i + 1
        time.sleep(1)
    print("click2 function with ({0},{1}) finished".format(a, b))


print("click1 is starting")
click1.delay(1, 2)
print("click2 is starting")
click2(3, 4)
print("all done")
