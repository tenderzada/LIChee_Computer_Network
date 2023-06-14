#coding:utf-8
from socket import *

# 创建TCP套接字对象tcpSerSock，并指定监听端口为8899。
tcpSerPort = 8899
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# 将TCP服务器套接字绑定到本地地址和指定端口，并开始监听连接请求，最大连接数为5。
# Fill in start.
# Fill in end.

while True:
    # 打印提示信息，表示服务器已准备好接收连接
    print('Ready to serve...')
    # 接受客户端的连接请求，获取客户端的地址信息。
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from: ', addr)
    # 从客户端接收请求报文，最大接收4096字节，并将其解码为字符串。
    message = # Fill in start. # Fill in end.

    # 从请求报文中解析出请求的文件名，将斜杠替换为下划线。
    filename = message.split()[1].partition("//")[2].replace('/', '_')
    fileExist = "false"
    try:
        # 尝试打开缓存中的文件，如果文件存在，则读取文件内容到outputdata列表中，并将fileExist设置为"true"，表示文件存在。
        f = open(filename, "r")
        outputdata = f.readlines()
        fileExist = "true"
        print('File Exists!')

        # 如果文件存在于缓存中，将文件内容逐行发送给客户端。
        for i in range(0, len(outputdata)):
            # Fill in start. # Fill in end.
        print('Read from cache')

    # 缓存中不存在该文件，异常处理
    except IOError:
        print('File Exist: ', fileExist)
        if fileExist == "false":
            # 创建一个新的套接字c，用于与远程服务器通信.
            print('Creating socket on proxyserver')
            c = # Fill in start. # Fill in end.

            # 解析出请求的主机名。
            hostn = message.split()[1].partition("//")[2].partition("/")[0]
            print('Host Name: ', hostn)
            try:
                # 连接到远程服务器80端口
                # Fill in start.
				# Fill in end.
                print('Socket connected to port 80 of the host')

                # 将请求报文发送给远程服务器
                c.sendall(message.encode())
                # 接收响应
                buff =  # Fill in start. # Fill in end.

                # 将响应内容发送给客户端，同时将响应内容写入缓存文件。
                tcpCliSock.sendall(buff)
                tmpFile = open("./" + filename, "w")

                # Fill in start.
				# Fill in end.

            except:
                print("Illegal request")

        else:
            # 如果文件在缓存和远程服务器上都不存在，打印提示信息表示文件未找到。
            print('File Not Found...Stupid Andy')
    # Close the client and the server sockets
    tcpCliSock.close()
# 关闭服务器套接字，结束程序运行。
# Fill in start.
# Fill in end.