#encoding=gbk
"""
https://blog.csdn.net/lm_is_dc/article/details/81098805
2.1 һ��ð��:������Ƭ
ͨ��ð������Ƭ��ͨ������������ά�ȡ�һά���б���ȫһ�� ��άʱͬ�� ��
"""
import numpy as np

np.random.seed(10)
arr=np.random.randint(10,50,size=(3,4))
print(arr)
#��ȡǰ��������
print(arr[0:2])
print("///////////////////")
#��ȡǰ���е�ǰ��������
print(arr[0:2,0:2])
print("///////////////////")
#��������е��ǵ�һ��ά�ȣ��У��������ұ��е��ǵڶ���ά�ȣ��У�
#��ȡ��ά����ǰ��������
print(arr[:,0:2])
print("///////////////////")
"""
����ð��::������Ƭ
һά

�����ݷ�ת������[1,2,3]��->[3,2,1
"""
#����һά����
arr=np.arange(0,10)
print(arr)

print(arr[::-1])
#����һ��3��3�еĶ�ά����
arr=np.linspace(0,9,num=9,endpoint=False).reshape((3,3))
print(arr)
#��ת��
print(arr[::-1])
#��ת��
print(arr[:,::-1])
#ȫ��ת
print(arr[::-1,::-1])