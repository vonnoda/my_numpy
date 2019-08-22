#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import time

# 转置矩阵
x = np.array([[1,2],[3,4]])
print(x)
'''[[1 2]
    [3 4]]'''
print(x.T)  #数组对象的T属性是用来转置矩阵
'''[[1 3]
    [2 4]]'''

# #数组的变形
x1 = np.array([1,2,3])
print(x1.reshape(1,3))      #[[1 2 3]]
print(x1[np.newaxis,:])     #通过newaxis获得行向量 [[1 2 3]]
print(x1[:,np.newaxis])     #通过newaxis获得列向量
'''[[1]
    [2]
    [3]]'''

# #数组的拼接和分裂

# #数组的拼接可以通过concatenate函数和stack函数实现
a = np.array([1,2,3])
b = np.array([3,2,1])
print(np.concatenate([a,b]))    #数组的拼接用concatenate属性完成，可拼接多个数组
                                #[1 2 3 3 2 1]
a1 = np.array([[1,2,3],[4,5,6]])
print(np.concatenate([a1,a1],axis=0))  #拼接多维数组，沿着第一个轴(默认索引为0时可以不写)拼接
'''[[1 2 3]
    [4 5 6]
    [1 2 3]
    [4 5 6]]'''
print(np.concatenate([a1,a1],axis=1))   #沿着第二个轴(索引为1)
'''[[1 2 3 1 2 3]
    [4 5 6 4 5 6]]'''
a1 = np.array([1,2,3])
b2 = np.array([[9,8,7],[6,5,4]])
c2 = np.array([[11],[11]])
print(np.vstack([a1,b2]))       #沿着固定维度处理数组时，可用np.vstack(垂直)和                                    np.hstack(水平)和np.dstack(第三维度)方法
'''[[1 2 3]
    [9 8 7]
    [6 5 4]]'''
print(np.hstack([b2,c2]))
'''[[ 9  8  7 11]
    [ 6  5  4 11]]'''
a3 = np.array([[1],[2],[3]])
c3 = np.array([[7],[8],[9]])
print(np.dstack([a3,c3]))
'''[[[1 7]]

    [[2 8]]

    [[3 9]]]'''

#数组的分裂可以通过np.split,np.hsplit和np.vsplit函数实现
d = [1,2,3,99,99,3,2,1]
d1,d2,d3 = np.split(d,[3,5])    #函数的参数列表不是维度，而是索引
print(d1,d2,d3)     #[1 2 3] [99 99] [3 2 1]
e = np.arange(16).reshape((4,4))
print(e)
'''[[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]
    [12 13 14 15]]'''
e_upper,e_lower = np.vsplit(e,[2])    #按行来分
print(e_upper)
'''[[0 1 2 3]
    [4 5 6 7]]'''
print(e_lower)
'''[[ 8  9 10 11]
    [12 13 14 15]]'''
e_left,e_right = np.hsplit(e,[2])       #按列来分
print(e_left)
'''[[ 0  1]
    [ 4  5]
    [ 8  9]
    [12 13]]'''
print(e_right)
'''[[ 2  3]
    [ 6  7]
    [10 11]
    [14 15]]'''

#通用函数
f1 = np.arange(5)/np.arange(1,6)
print(f1)   #[0.  0.5   0.66666667   0.75   0.8  ]  对数组的值进行操作
f2 = np.arange(4).reshape((2,2))
print(f2**2)    #对值进行运算
'''[[0 1]
    [4 9]]'''
f3 = np.arange(4)
print(f3+2)     #[2 3 4 5]  加减乘除和乘方都可以
f4 = np.array([-2,-1,0,1,2])
print(np.abs(f4))   #[2 1 0 1 2]    绝对值运算
print(np.power(f4,2))   #[4 1 0 1 4]    指数运算
print(np.log2(np.array([1,2,3])))  #[0.  1.  1.5849625]  对数运算

#指定输出
g = np.arange(5)
h = np.empty(5)
np.multiply(g,10,out=h)     #out参数指定输出位置
print(h)    #[ 0. 10. 20. 30. 40.]
g1 = np.zeros(10)
h1 = np.power(2,g,out=g1[::2])
print(h1)   #[ 1.  2.  4.  8. 16.]

#聚合
#reduce方法会对给定的元素和操作重复执行，直至得到单个的结果
i = np.arange(1,6)
print(np.add.reduce(i))     #15 执行add累加   等同于sum方法
print(np.multiply.reduce(i))    #120 执行multiply累乘     等同于prod方法
#如果要储存每次计算的中间结果，可以用accumulate方法
print(np.add.accumulate(i))     #[ 1  3  6 10 15]   等同于cumsum方法
print(np.multiply.accumulate(i))    #[  1   2   6  24 120]    等同于cumprod方法

#外积
#任何通用函数都可以通过outer方法获得两个不同输入数组所有元素对的函数运算结果
j = np.arange(1,6)
print(np.multiply.outer(j,j))
'''[[ 1  2  3  4  5]
    [ 2  4  6  8 10]
    [ 3  6  9 12 15]
    [ 4  8 12 16 20]
    [ 5 10 15 20 25]]'''

#多维度聚合
#不同维度的最大/小值
np.random.seed(0)
k = np.random.random((3,4))
print(np.min(k,axis=0))  #每一列的最小值 [0.4236548  0.38344152 0.43758721 0.52889492]
print(k.min(axis=0))    #两种写法都行 [0.4236548  0.38344152 0.43758721 0.52889492]
print(k.min())  #0.3834415188257777    不指定维度只输出最小值
print(k.max(axis=1))    #每一行的最大值 [0.71518937 0.891773   0.96366276]

#其他聚合函数

m = np.arange(1, 6)
print(np.sum(m))        #求和      15
print(np.prod(m))       #求乘积    120
print(m.mean())         #求平均值   3.0
print(m.std())          #求标准差   1.4142135623730951
print(m.var())          #求方差    2.0
print(m.min())          #求最小值   1
print(m.max())          #求最大值   5
print(m.argmin())       #找出最小值索引    0
print(m.argmax())       #找出最大值索引    4
print(np.median(m))     #求中位数   3.0
print(m.any())          #判断是否存在元素为真 True
print(m.all())          #判断所有元素是否为真 True
print(np.percentile(m,25))  #求分位数，25是上四分位，75是下四分位  2.0

