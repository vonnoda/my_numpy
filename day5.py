#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
#求解方程组
#求解向量方程

# a = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
# b = np.transpose(np.array([[-3,5,-2]]))
#求ax=b方程中的x
x = np.linalg.solve(a,b)    #求解向量方程
print(x)
'''[[ 1.]
    [-1.]
    [ 2.]]'''

#数组分裂和变形补充

def f(x,y):
    return 10*x+y
b = np.fromfunction(f,(2,2),dtype=int)
print(b)
'''[[ 0  1]
    [10 11]]'''
for ele in b.flat:  #对数组中的每个元素执行操作
    print(ele)
'''0
    1
    10
    11'''
np.random.seed(0)
a = np.floor(10*np.random.random((3,4)))
print(a)
'''[[5. 7. 6. 5.]
    [4. 6. 4. 8.]
    [9. 3. 7. 5.]]'''
print(a.ravel())    #[5. 7. 6. 5. 4. 6. 4. 8. 9. 3. 7. 5.]  将数组扁平化(一维化),但不修改原数组,等同于flatten
print(a.ravel('f'))     #[5. 4. 9. 7. 6. 3. 6. 4. 7. 5. 8. 5.]  f参数按列展开
print(a.flatten())      #[5. 7. 6. 5. 4. 6. 4. 8. 9. 3. 7. 5.]
print(a.flatten('F'))   #[5. 4. 9. 7. 6. 3. 6. 4. 7. 5. 8. 5.]  F参数按列展开，同上
print(a.reshape(6,2).shape)     #(6, 2)  reshape不修改原数组，修改原数组有resize
print(a.T.shape)    #(4,3)  转置也不修改原数组
print(a.shape)  #(3,4)
print(a)
print(a.resize(2,6))  #resize修改原数组
'''[[5. 7. 6. 5. 4. 6.]
    [4. 8. 9. 3. 7. 5.]]'''
print(a.shape)      #(2, 6)
