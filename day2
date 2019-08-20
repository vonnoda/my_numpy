#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np

#数组索引
a = np.array([[1,2], [3, 4], [5, 6]])

print(a[[0,1,2],[0,1,0]])       #这行和下面一行等价     [1 4 5]
print(np.array([a[0,0], a[1,1], a[2,0]]))           #[1 4 5]
print(a[[0, 0], [1, 1]])    #[2 2]
print(np.array([a[0, 1], a[0, 1]]))     #[2 2]  这行和上面一行等价

b = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
c = np.array([0,2,0,1])
print(b[np.arange(4),c])        #[ 1  6  7 11]
b[np.arange(4),c] += 10     #只是对应的元素进行了运算
print(b)        #[[11  2  3]
                # [ 4  5 16]
                # [17  8  9]
                # [10 21 12]]

#布尔索引
d = np.array([[1,2], [3, 4], [5, 6]])
bool_x1 = (d>2)
print(bool_x1)
'''[[False False]
 [ True  True]
 [ True  True]]'''

print(d[bool_x1])   #[3 4 5 6]    等价于下面的表达式
print(d[d>2])       #[3 4 5 6]

#数组运算
x = np.array([[1,2],[3,4]],dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x+y) #等价于下面的表达式,后面的其他运算也是一样
'''[[ 6.  8.]
    [10. 12.]]'''
print(np.add(x,y))
'''[[ 6.  8.]
    [10. 12.]]'''
print(x-y)
'''[[-4. -4.]
    [-4. -4.]]'''
print(np.subtract(x,y))
'''[[-4. -4.]
    [-4. -4.]]'''
print(x*y)        #*是元素乘法，不是矩阵乘法
'''[[ 5. 12.]
    [21. 32.]]'''
print(np.multiply(x,y))
'''[[ 5. 12.]
    [21. 32.]]'''
print(x/y)
'''[[0.2        0.33333333]
    [0.42857143 0.5       ]]'''
print(np.divide(x,y))
'''[[0.2        0.33333333]
    [0.42857143 0.5       ]]'''

v = np.array([9,10])
w = np.array([11, 12])

print(v.dot(w)) #dot函数计算向量内积，将向量乘以矩阵，并乘以矩阵。等同于下面的表达式
print(np.dot(v,w))  #dot函数可以作为numpy模块中的函数，也可以作为数组对象的实例方法

x2 = np.array([[1,2],[3,4]])
print(np.sum(x2))           #10
print(np.sum(x2,axis=0))    #[4 6]  列计算
print(np.sum(x2,axis=1))    #[3 7]  行计算
