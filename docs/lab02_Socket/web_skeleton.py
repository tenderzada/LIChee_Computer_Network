from socket import *
# 创建TCP套接字对象serverSocket
serverSocket = socket(AF_INET, SOCK_STREAM) 
# 将TCP套接字绑定到本地地址和指定端口6789。
# 设置最大连接数为1，开始监听客户端连接请求。
#Fill in start 
#Fill in end

while True:
	print('Ready to serve...')
	# 接收到客户端连接请求后，建立新的TCP连接套接字connectionSocket，同时获取客户端的地址信息addr。
	connectionSocket, addr = #Fill in start  #Fill in end
	print('Received a connection from: ', addr)
	try:
		# 从客户端接收请求报文，提取请求的文件名，打开对应文件，并读取文件内容。
		message = #Fill in start  #Fill in end
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = #Fill in start  #Fill in end
		# 构建HTTP响应头部，包括状态行和其他字段，并发送给客户端   
		#Fill in start         
        #Fill in end  

		# 逐个字符将文件内容发送给客户端。
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		# 关闭与客户端的连接。
		connectionSocket.close()
	except IOError:
		# 如果请求的文件不存在，返回404错误响应。
		#Fill in start
        #Fill in end
		
		# 关闭与客户端的连接。
		#Fill in start
        #Fill in end   
	# 关闭服务器套接字。
	serverSocket.close()