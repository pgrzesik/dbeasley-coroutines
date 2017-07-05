from scheduler import GetTid, NewTask, KillTask, Scheduler


def foo():
    mytid = yield GetTid()
    while True:
        print(f'foo, Tid: {mytid}')
        yield


def main():
    child = yield NewTask(foo())
    for i in range(5):
        yield
    result = yield KillTask(child)
    print(f'main done executing, result: {result}')


sched = Scheduler()
sched.new(main())
sched.mainloop()
