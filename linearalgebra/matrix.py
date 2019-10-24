#__author: xlu.com
#date : 2018/12/28
import numpy

class Matrix:
    def __init__(self,list2d):
        self._values = [row[:] for row in list2d]

    @classmethod
    def zero(cls,r,c):
        return cls([[0] * c for i in range(r)])

    @classmethod
    def identity(cls,n):
        """实现单位矩阵（方阵）"""
        m = [[0]* n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)

    def __repr__(self):
        """自定义输出对象"""
        return "matrix=({})".format(self._values)
    __str__ = __repr__

    def shapr(self):
        """获取矩阵的形状(行数和列数)"""
        return (len(self._values),len(self._values))

    def row_num(self):
        """获取矩阵的行数"""
        return self.shapr()[0]

    def col_num(self):
        """获取矩阵的列数"""
        return  self.shapr()[1]
    def size(self):
        return self.row_num()*self.col_num();
    def __getitem__(self, pos):
        """获取某一个元素"""
        r,c = pos
        print(r,c)
        return self._values[r][c]

    def __add__(self, other):
        """实现矩阵加法"""
        assert self.shapr() == other.shapr(),"不同形状的矩阵"
        # lst = []
        # for i in range(self.row_num()):
        #     sub_it = [];
        #     for a,b in zip(self._values[i],other._values[i]):
        #         sub_it.append(a+b);
        #     lst.append(sub_it)
        # return Matrix(lst)
        #简写
        return Matrix([[a+b for a,b in zip(self._values[i],other._values[i])]for i in range(self.row_num())])

    def __sub__(self, other):
        assert self.shapr() == other.shapr(),"不同形状的矩阵"
        return  Matrix([[a-b for a,b in zip(self._values[i],other._values[i])]for i in range(self.row_num())])
    def __mul__(self, idx):
        #实现矩阵数量乘法
        return Matrix([[a*idx for a in self._values[i]]for i in range(self.row_num())])
    def __rmul__(self, idx):
        return self * idx

    def __truediv__(self, idx):
        #实现矩阵数量除法
        return (1 / idx) * self
    def __pos__(self):
        #实现矩阵取正
        return 1*self;
    def __neg__(self):
        #实现矩阵取负
        return  -1*self;
