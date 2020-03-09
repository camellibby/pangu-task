import time

from pangu_task import task


def init():
    print('init event!')


def callback(result):
    print('callback event!')
    print("return value {0}".format(result))


@task(init=init, callback=callback)
def click1(a, b):
    print("click1 function with ({0},{1}) start".format(a, b))
    i = 0
    while i < 10:
        print("click1 is running: {0}".format(i))
        i = i + 1
        time.sleep(1)
    print("click1 function with ({0},{1}) finished".format(a, b))
    return 1


@task(init=init, callback=callback)
def click2(a, b):
    print("click2 function with ({0},{1}) start".format(a, b))
    i = 0
    while i < 3:
        print("click2 is running: {0}".format(i))
        i = i + 1
        time.sleep(1)
    print("click2 function with ({0},{1}) finished".format(a, b))
    return 1


print("click1 is starting")
x1 = click1.delay(1, 2)
print("click1 return value {0}".format(x1))
print("click2 is starting")
x2 = click2(3, 4)
print("click2 return value {0}".format(x2))
print("all done")
