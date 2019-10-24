#__author: xlu.com
#date : 2018/12/28

from linearalgebra.matrix import Matrix

if __name__ == "__main__":
    matrix = Matrix([[1,2],[3,4]])
    print(matrix)
    #2*2的矩阵
    print(matrix.shapr())
    #获取行数
    print(matrix.row_num())
    #获取列数
    print(matrix.col_num())
    #获取第2行第1列
    print("matrix[1][1]={}".format(matrix[1,1]))
    #矩阵大小（元素个数）
    print("matrix.size={}".format(matrix.size()))


    #矩阵相加
    matrix1 = Matrix([[5,6],[7,8]])
    print("add:{}".format(matrix+matrix1))
    #矩阵相减
    print("sub:{}".format(matrix-matrix1))
    print("sub:{}".format(matrix1-matrix1))
    #矩阵数量乘法
    print("scalar_mut:{}".format(matrix*4))
    print("scalar_mut:{}".format(3*matrix))
    #矩阵数量除法
    print("true_div:{}".format(matrix/3))
    #初始化一个0矩阵
    print("zero:{}".format(Matrix.zero(3,3)))
    print([2]*3)

    #矩阵和向量的运算

    #单位矩阵
    I = Matrix.identity(5)
    print("I:{}".format(I))
