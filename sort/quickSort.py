#encoding=gbk
"""
����������ϰ
���������б��Ϊ����2���֣�ÿ���ּ���ʹ�ÿ��������㷨������õݹ�ʵ��
"""
def quick_sort(arr):
    if arr==[]:
        return []
    else:
        first = arr[0]
        left=quick_sort([l for l in arr[1:] if l<first])
        right=quick_sort([r for r in arr[1:] if r>=first])
        return left + [first] + right

arr=[2,5,1,7,9,4]
result_list=quick_sort(arr)
print(result_list)
