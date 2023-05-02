# NS-3 数据通信与简单的网络拓扑

### 1 介绍

NS-3（Network Simulator-3）是一个开源的用于互联网系统的离散事件网络模拟器、使用C++或Python构建、它主要用于研究和教育，在GNU GPLv2许可证下公开使用。NS-3以源码形式发布，这意味着目标系统需要有软件开发环境能够首先构建所需的库，然后构建用户程序。

NS-3也是一个常用的科研工具，研究人员基于ns-3 仿真，仿真许多用于优化无线网络的 AI 算法，比如，Darago等人基于ns-3实现了车联网（Vehicle-To-Everything, V2X）仿真，可以进行交通流量和拥堵控制、定位、自动驾驶等应用[^1]：

![image-20230502093425470](images/image-20230502093425470.png)

### 2 目标

本实验的两个目标：

- 在NS-3中建立并分析一个简单的点对点链接拓扑结构。

- 使用路由在 NS-3 中构建和分析小型点对点链路。

### 3 实验步骤

本实验在Ubuntu 18.04 LTS发行版的Linux机器上进行（或18.04以上）。

Windows用户：Windows用户在下载ns-3之前需要安装虚拟机（如ubuntu 20.04）。

#### 3.1 安装和构建 NS-3

访问[ns-3官网](https://www.nsnam.org/)，下载最新版本的ns-3。浏览[ns-3教程](https://www.nsnam.org/docs/release/3.38/tutorial/singlehtml/index.html)第4-7章。第4章讲解下载和安装ns-3的过程。第5-7章介绍ns-3所需的基本概念。

![image-20230502093443121](images/image-20230502093443121.png)

#### 3.2 构建和使用脚本

在建立了NS-3之后，复制`examples/tutorials`中的`first.cc`文件，并将其粘贴在 `scratch`目录中。`first.cc`是一个脚本，它在两个节点之间创建一个简单的点对点链接，并在节点之间回传一个数据包。导航到`ns-3.37`目录下并执行`./ns3 --run scratch/first`命令，在`ns-3.37`目录下构建并运行`first.cc`脚本。

![image-20230502093458298](images/image-20230502093458298.png)

第一个NS-3脚本运行，详见：[first-ns-3-script](https://www.nsnam.org/docs/release/3.38/tutorial/singlehtml/index.html#a-first-ns-3-script)

要运行你自己的脚本，请在`scratch`目录下编写，并按照上述剩余程序进行。在执行完`./ns3 --run scratch/first`后，你应该在终端看到以下输出。

![image-20230502093509203](images/image-20230502093509203.png)

first.cc表明客户端通过向服务器发送一个数据包来启动通信，然后服务器收到上述数据包，再向客户端发送自己的数据包，确认原始数据包被它成功接收。  

#### 3.3 实验任务1

修改上述代码，以改变数据包大小、数据率、传输延迟、节点的IP地址和服务器端口。给出实验（源码）代码和输出（图片）。

如：

![image-20230502093519182](images/image-20230502093519182.png)

#### 3.4 NS-3中的简单拓扑

每当数据在计算机网络上传输时，构成数据的数据包都要经过被称为Routers的东西。这些路由器读取这些数据包上的目的地IP，并使用路由表来确定数据包到达目的地的最有效路线。我们在这个实验中要探索的正是这种Routing的现象。

在3.2节，我们在客户和服务器节点之间建立一个点对点的链接。本节中要求有一个作为路由器的中间节点的存在，有关的拓扑结构可以通过下面的图示简要地概括

![image-20230502093531011](images/image-20230502093531011.png)

我们首先创建一个单一的节点容器来容纳我们的拓扑结构所需的三个节点，然后我们将上述三个节点隔离成两个节点容器，一个用于客户端，一个用于服务器，它们之间共享路由器。 接下来是NS-3的一般程序，即指定点对点链接、安装网卡、协议栈以及在适当的节点上安装客户端和服务器应用程序。最后，加入了`Ipv4GlobalRoutingHelper::PopulateRoutingTables()`行，以允许对数据包进行路由。给出为模拟上述拓扑的行为而编写的代码，以及控制台的输出结果。

![image-20230502093544934](images/image-20230502093544934.png)

额外加分：构建如下的拓扑结构

![image-20230502093555356](images/image-20230502093555356.png)

### 参考文献

[^1]:Drago M, Zugno T, Mason F, et al. Artificial Intelligence in Vehicular Wireless Networks: A Case Study Using ns-3[C]//Proceedings of the 2022 Workshop on ns-3. 2022: 112-119.

本实验在设计过程中，内容参考了以下文档：

[Ubuntu20.04安装NS3](https://blog.csdn.net/qq_53273581/article/details/124848777)