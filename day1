#!/usr/bin/env python
#-*- coding:utf-8 -*-
from numpy import *
import numpy as np

#创建数组

a = np.array([0,1,2,3,4])
b = np.array((0,1,2,3,4))
c = np.arange(5)    #numpy.arange(start(默认为0),stop,step(默认为1),dtype(默认为输入的数据类型))
d = np.linspace(0,2,5)      #从0到2，数量为5
e = np.array([0,1,2,3.14,4])    #数据类型不一致，numpy会自动向上转换
f = np.array([1,2,3,4],dtype=float32)     #可以用dtype关键字设置数据类型
g = np.array([range(i,i+3) for i in [2,4,6]])   #可以初始化多维数组
h = np.logspace(1,5,3,base=2,dtype=int)   #创建等比数列数组，q为2，数量为3，指数从1到5
i = np.frombuffer(b'HelloWorld',dtype='S1') #py3中str是Unicode类型，需要转成bytestring，所以加b
j = np.full((2,2),7)    #创建常量数组
k = np.eye(2)       #创建单位矩阵
l = np.random.random((2,2))     #创建随机数数组
m = np.random.randint(0,10,(3,3))   #创建随机整数数组，0到10为区间
n = np.random.normal(0,1,(2,2))     #创建2*2的，均值为0，标准差为1的正态分布随机数数组



print(a)    #[0 1 2 3 4]
print(b)    #[0 1 2 3 4]
print(c)    #[0 1 2 3 4]
print(d)    #[0.  0.5 1.  1.5 2. ]
print(e)    #[0.   1.   2.   3.14 4.  ]
print(f)    #[1. 2. 3. 4.]
print(g)    #[[2 3 4]
            # [4 5 6]
            # [6 7 8]]
print(h)    #[2 8 32]
print(i)    #[b'H' b'e' b'l' b'l' b'o' b'W' b'o' b'r' b'l' b'd']
print(j)    #[[7 7]
            # [7 7]]
print(k)    #[[1. 0.]
            # [0. 1.]]
print(l)    #[[0.95197746 0.05771651]
            # [0.2388137  0.07046096]]
print(m)    #[[3 4 0]
            # [8 0 9]
            # [7 8 0]]
print(n)    #[[-0.80120947 -0.02532736]
            # [-1.65677338 -0.15691605]]

#从头创建数组

x1 = np.zeros(10,dtype=int)     #创建指定大小的数组，元素用0来填充
x2 = np.ones((2,5),dtype=float)     #创建指定形状的数组。元素用1来填充
x3 = np.empty([3,2],dtype=int,order='C')    #创建指定形状，数据类型，未初始化的数据(元素为随机值)。
                                         #有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内                                           存中的存储元素的顺序。

print(x1)   #[0 0 0 0 0 0 0 0 0 0]
print(x2)   #[[1. 1. 1. 1. 1.]
            # [1. 1. 1. 1. 1.]]
print(x3)   #[[2111834192      32760]
            #[2111838784      32760]
            #[1935740122 1953654131]]

#数组属性

s1 = np.linspace(11,35,25,dtype=int).reshape([5,5])     #s1和s2和s3是同一个数组的不同创建方式
s2 = np.array([range(i,i+5) for i in [11,16,21,26,31]])
s3 = np.arange(11,36).reshape(5,5)
print(type(s1))         #<class 'numpy.ndarray'>
print(s1.dtype)         #int32
print(s1.size)          #25
print(s1.shape)         #(5,5)   5行5列
print(s1.itemsize)      #4  每个项占用的字节数
print(s1.ndim)          #2  数组的维数
print(s1.nbytes)        #100    数组中所有的数据消耗的字节数

a1 = np.arange(10)
print(a1.sum())      #45
print(a1.min())      #0
print(a1.max())      #9
print(a1.cumsum())   #[ 0  1  3  6 10 15 21 28 36 45]  首先将第一个元素和第二个元素相加，并将计算结果存储在一个列表中，然后将该结果添加到第三个元素中，然后再将该结果存储在一个列表中。这将对数组中的所有元素执行此操作，并返回作为列表的数组之和的运行总数。

#索引

b1 = np.arange(11,36).reshape(5,5)
print(b1[0,1:4])        #[12 13 14]     第0行，第1到3列
print(b1[1:4,0])        #[16 21 26]     第1到3行，第0列
print(b1[::2,::2])      #[[11 13 15]    每行每列，步进为2
                        # [21 23 25]
                        # [31 33 35]]
print(b1[:,1])          #[12 17 22 27 32]   每行，第一列

#花式索引
c1 = np.arange(0,100,10)
c1temp = [1,5,-1]
d1 = c1[c1temp]
print(d1)           #[10 50 90]     一次索引多个指定的数值

#布尔屏蔽
import matplotlib.pyplot as plt
e1 = np.linspace(0,2*np.pi,50)
f1 = np.sin(e1)
plt.plot(e1,f1)
mask = f1 >= 0
plt.plot(e1[mask],f1[mask],'bo')
mask = (f1>=0) & (e1<=np.pi/2)
plt.plot(e1[mask],f1[mask],'go')
plt.show()

#缺省索引
g1 = np.arange(0,100,10)
g2 = g1[g1>=50]
print(g2)           #[50 60 70 80 90]
g3 = np.where(g1<50)
g4 = np.where(g1>=50)[0]
print(g3)       #(array([0, 1, 2, 3, 4], dtype=int64),)   返回值表示前5个元素为真值，类型为列表
print(g4)       #[5 6 7 8 9]    返回值表示后5个元素为真值，返回值类型为列表
