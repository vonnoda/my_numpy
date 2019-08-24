#!/usr/bin/env python
#-*- coding:utf-8 -*-
#深拷贝和浅拷贝
import numpy as np
a = np.arange(12)
b = a.view()
b.reshape((3,4))
print(a)    #[ 0  1  2  3  4  5  6  7  8  9 10 11]
print(b)    #[ 0  1  2  3  4  5  6  7  8  9 10 11]
c = a.copy
print(c is a )  #False

#利用布尔统计个数
r = np.random.RandomState(0)
x = r.randint(10,size=(3,4))    #随机生成一个数组
print(x)
'''[[5 0 3 3]
    [7 9 3 5]
    [2 4 7 6]]'''
print(x<6)
'''[[ True  True  True  True]
    [False False  True  True]
    [ True  True False False]]'''
print(np.count_nonzero(x<6))    #8 有8个元素是符合条件的，也可以用下面的式子表达
print(np.sum(x<6))  #8  True会被记录为1，False会被记录为0
print(np.sum((x>3)&(x<6)))  #3  原理同上
print(x[x<6])   #[5 0 3 3 3 5 2 4]  返回的一维数组，是所有对应位置为True的值

#利用索引修改数值
y = np.arange(10)
i = np.array([2,1,8,4])
y[i]=99
print(y)    #[ 0 99 99  3 99  5  6  7 99  9]    第i位置的元素被修改了
y2 = np.copy(y)
y2[i] -= 10
print(y2)   #[ 0 89 89  3 89  5  6  7 89  9]    同理
