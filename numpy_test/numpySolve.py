#encoding=gbk
"""
https://blog.csdn.net/jayloncheng/article/details/80003182
1�������Է�����
example��
     2x + 3y = 5
     x   + 3y = 3
  �����뼰������� ��
        ��� x=2,y=1/3.
"""
import numpy as np
from numpy.linalg import solve
a=np.mat([[2,3],[1,3]])#ϵ������
b=np.mat([5,3]).T    #�������о���
x=solve(a,b)        #������Ľ�
print(x)

"""
2��������Է�����
example:
    x*x + 2y = 5
    x + y  =  1
�����뼰������£�
         x=3,y=-2 ;
         x=-1,y=2.
"""

from scipy.optimize import fsolve
def func(paramlist):
    x,y=paramlist[0],paramlist[1]
    return [ x**2+2*y-5,
            x+y-1 ]
s=fsolve(func,[0,0])
print(s)