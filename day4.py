#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np

#广播(broadcasting)
#广播可以理解为用于不同形状的数组进行算术运算的规则

a = np.array([0,1,2])
b = np.ones((3,3))
print(a+b)          #一位数组沿着第二个维度扩展了，扩展到匹配高维数组的shape
'''[[1. 2. 3.]
    [1. 2. 3.]
    [1. 2. 3.]]'''
a1 = np.arange(3)
b1 = np.arange(3)[:,np.newaxis]
print(a1+b1)    #相当于两个数组都进行扩展来匹配一个公共的相同的形状
'''[[0 1 2]
    [1 2 3]
    [2 3 4]]'''
a2 = np.ones((3,2))
b2 = np.arange(3)
c2 = b2[:,np.newaxis]   #通过变形数组的方式，使两个数组维度兼容
print(a2+c2)
'''[[1. 1.]
    [2. 2.]
    [3. 3.]]'''
#广播的应用
#例一 实现数据的归一化
np.random.seed(0)
x = np.random.random((10,3))
xmean = np.mean(x,axis=0)   #求第一个维度(行)上的均值，也可以写成x.mean(0)
print(xmean)    #[0.52101579 0.62614181 0.59620338]
x_centered = x-xmean    #x中的每一个元素减去均值实现归一化
print(x_centered)

#例二 二维数值可视化
import matplotlib.pyplot as plt
x = np.linspace(0,5,50)
y = np.linspace(0,5,50)[:,np.newaxis]
z = np.sin(x)**10+np.cos(10+y*x)*np.cos(x)
plt.imshow(z,origin='lower',extent=[0,5,0,5],cmap='viridis')
plt.colorbar()
plt.show()
