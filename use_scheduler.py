from scheduler import Scheduler


def foo():
    while True:
        print('Foo')
        yield


def bar():
    while True:
        print('bar')
        yield


sched = Scheduler()
sched.new(foo())
sched.new(bar())
sched.mainloop()
