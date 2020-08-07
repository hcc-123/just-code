#查找
#1.顺序查找，也叫线性查找
from cal_time import cal_time

@cal_time
def liner_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None

#2.二分查找
@cal_time
def binary_search(li, val, l = 0):
    l = 0
    r = len(li) - 1
    while l <= r:   #候选区有值
        mid = (l + r) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: #待查找的值在mid左边
            r = mid - 1
        else: #li[mid] < val 待查找的值在mid右侧
            l = mid + 1
    else:
        return None

