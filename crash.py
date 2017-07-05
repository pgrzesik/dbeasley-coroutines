from scheduler import Scheduler, GetTid


def foo():
    mytid = yield GetTid()
    for i in range(10):
        print(f'foo, Tid: {mytid}')
        yield


def bar():
    mytid = yield GetTid()
    for i in range(5):
        print(f'bar, Tid: {mytid}')
        yield


sched = Scheduler()
sched.new(foo())
sched.new(bar())
sched.mainloop()
