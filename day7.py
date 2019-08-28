#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np

#选择排序
def selection_sort(x):
    for i in range(len(x)):
        swap = i+np.argmin(x[i:])
        (x[i],x[swap])=(x[swap],x[i])
    return x

x = np.array([2,1,4,3,5])
print(selection_sort(x))   #[1 2 3 4 5]

#快速排序
x = np.array([2,1,4,3,5])
print(np.sort(x))   #[1 2 3 4 5]
print(x)    #[2 1 4 3 5]    不改变原数组，只是用这个方法排序
i = np.argsort(x)
print(i)    #[1 0 3 2 4]    返回的是原始数组排好序的索引值
print(x[i]) #[1 2 3 4 5]    通过花式索引创建有序数组

x1 = np.random.RandomState(42)
y = x1.randint(0,10,(3,4))
print(y)
'''[[6 3 7 4]
    [6 9 2 6]
    [7 4 3 7]]'''
print(np.sort(y,axis=0))    #对每一列进行排序
'''[[6 3 2 4]
    [6 4 3 6]
    [7 9 7 7]]'''
print(np.sort(y,axis=1))    #对每一行进行排序
'''[[3 4 6 7]
    [2 6 6 9]
    [3 4 7 7]]'''

#分隔
x2 = np.array([7,2,3,1,6,5,4])
print(np.partition(x2,3))    #[2 1 3 4 6 5 7]    前三个值是数组中最小的三个值,剩下的位置是其他元素，两个区域都是各自任意排列，相当于隔板法
print(np.partition(y,2,axis=1))     #沿着多维数组的任意轴进行分隔
'''[[3 4 6 7]
    [2 6 6 9]
    [3 4 7 7]]'''
print(np.argpartition(y,2,axis=1))      #同理，是分隔对应要求的索引值
'''[[1 3 0 2]
    [2 0 3 1]
    [2 1 0 3]]'''

#案例：K个最邻值
a = x1.rand(10,2)
import matplotlib.pyplot as plt
import seaborn;seaborn.set()    #设置画图风格
plt.scatter(a[:,0],a[:,1],s=100)
dist_sq = np.sum((a[:,np.newaxis,:] - a[np.newaxis,:,:])**2,axis=-1)#矩阵的平方距离
print(dist_sq.diagonal())   #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
nearest = np.argsort(dist_sq,axis=1)
print(nearest)
'''[[0 3 4 5 8 1 9 7 2 6]
    [1 4 6 9 8 0 7 3 2 5]
    [2 7 9 8 6 4 3 1 0 5]
    [3 5 0 8 4 9 7 2 1 6]
    [4 1 0 8 9 6 3 5 7 2]
    [5 3 0 8 4 9 1 7 2 6]
    [6 1 9 4 8 7 2 0 3 5]
    [7 2 9 8 6 4 1 3 0 5]
    [8 9 4 7 2 3 0 1 5 6]
    [9 8 7 2 6 1 4 0 3 5]]'''
k = 2
nearest_partition = np.argpartition(dist_sq,k+1,axis=1)
for i in range(a.shape[0]):
    for j in nearest_partition[i,:k+1]:
        plt.plot(*zip(a[j],a[i]),color='black')

plt.show()
        
