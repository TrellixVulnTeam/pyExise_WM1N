#encoding=gbk
"""
����������ϰ
�������Ϊ����õģ��Ҳ�ȡֵ���������Ԫ�رȽ�
"""
def insert_sort(arr):
    #order_arr=arr[0]
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

arr=[2,5,1,7,9,4]
result_list=insert_sort(arr)
print(result_list)

