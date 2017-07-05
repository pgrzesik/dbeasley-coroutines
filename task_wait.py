from scheduler import NewTask, Scheduler, WaitTask


def foo():
    for x in range(5):
        print('foo')
        yield


def main():
    child = yield NewTask(foo())
    print('waiting for child')
    result = yield WaitTask(child)
    print(f'child done, result: {result}')


sched = Scheduler()
sched.new(main())
sched.mainloop()
