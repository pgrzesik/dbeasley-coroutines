from socket import socket, SOCK_STREAM, AF_INET

from scheduler import ReadWait, WriteWait, NewTask, Scheduler


def handle_client(client, addr):
    print(f'Connection from {addr}')
    while True:
        yield ReadWait(client)
        data = client.recv(65536)
        if not data:
            break
        yield WriteWait(client)
        client.send(data)
    client.close()
    print('Client closed')


def server(port):
    print(f'Server starting on port: {port}')
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(5)
    while True:
        yield ReadWait(sock)
        client, addr = sock.accept()
        yield NewTask(handle_client(client, addr))


if __name__ == '__main__':
    sched = Scheduler()
    sched.new(server(8888))
    sched.mainloop()
