#encoding=gbk
"""
ѡ��������ϰ
���������Ϊ��Сֵ���Ҳ�ʵ����Сֵ�ҳ����������Сֵ����
"""
def selectiveSort(arr):
    for i in range(len(arr)):
        minIndex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex=j
        if minIndex!=i:
           arr[i],arr[minIndex]=arr[minIndex],arr[i]

    return arr

arr=[2,5,1,7,9,4]
result_list=selectiveSort(arr)
print(result_list)