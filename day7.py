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
