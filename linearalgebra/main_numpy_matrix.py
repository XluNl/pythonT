#__author: xlu.com
#date : 2018/12/28
import numpy as np

if __name__ == "__main__":

    A = np.array([[1,2],[3,4]])
    print(A)
    #矩阵的属性(形状)
    print(A.shape)
    # print(A.T) #转置

    #矩阵的元素
    print(A[1,1])
    print(A[0])#获取一行
    print(A[:,0])#获取一列
    print(A[1,:])#获取指定列

    #矩阵的运算
    B = np.array([[3,4],[5,6]])
    print(A+B)
    print(A-B)
    print(A*2)
    print(A/2)
    #这两种相乘有区别
    print(A*B)
    print(A.dot(B))

    #矩阵和向量的操作
    p = np.array([7,8])
    print(A+p)#矩阵加上一个向量
    print(A+1)
    print(A.dot(p))
