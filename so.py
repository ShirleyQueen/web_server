# TCP Socket服务器
socket = socket.socket()
socket.bind()
socket.listen()
cli_socket = socket.accpet()
while True:
    # 多进程
    p = Process(target=fun, agrs=())
    p.start()
    cli_socket.close()


def fun(cli_socket):
    # 接收数据
    # request_data=recv()
    # print(request_data)
    # 解析HTTP报文数据request_data
    # 提取请求方式
    # 提取请求路径path
    HTML_ROOT_DIR = "./html"
    path = / index.html
    try:
        file = open(HTML_ROOT_DIR + "index.html")
    data = file.read()
    file.close()
    except IOError:

    # 返回响应数据
    """
    HTTP1.1 200 OK\r\n
    \r\n
    hello world
    """
    # send()
    # close()
