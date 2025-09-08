# -*- coding: utf-8 -*-
"""
二分查找算法实例代码
适用场景：在有序数组中快速查找特定元素
难度：2-5级（根据具体问题复杂度而定）
"""


def binary_search(arr, target):
    """
    二分查找基本实现
    原理：每次将查找范围缩小为原来的一半
    时间复杂度：O(log n)
    
    参数：
        arr: 已排序的数组（升序）
        target: 要查找的目标值
    返回：
        目标值在数组中的索引，如果不存在则返回-1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # 避免整数溢出的写法
        
        if arr[mid] == target:
            return mid  # 找到目标值，返回索引
        elif arr[mid] < target:
            left = mid + 1  # 目标在右半部分
        else:
            right = mid - 1  # 目标在左半部分
    
    return -1  # 未找到目标值


def binary_search_left_bound(arr, target):
    """
    二分查找左边界
    寻找第一个大于等于target的元素的索引
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] >= target:
            result = mid
            right = mid - 1  # 继续向左查找
        else:
            left = mid + 1
    
    return result


def binary_search_right_bound(arr, target):
    """
    二分查找右边界
    寻找最后一个小于等于target的元素的索引
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= target:
            result = mid
            left = mid + 1  # 继续向右查找
        else:
            right = mid - 1
    
    return result


def binary_search_with_steps(arr, target):
    """
    带步骤展示的二分查找
    用于演示二分查找的每一步操作
    """
    left, right = 0, len(arr) - 1
    step = 1
    
    print(f"查找目标{target}在数组{arr}中的位置")
    
    while left <= right:
        mid = left + (right - left) // 2
        print(f"步骤{step}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"找到目标{target}，索引为{mid}")
            return mid
        elif arr[mid] < target:
            print(f"{arr[mid]} < {target}，目标在右半部分")
            left = mid + 1
        else:
            print(f"{arr[mid]} > {target}，目标在左半部分")
            right = mid - 1
        
        step += 1
    
    print(f"未找到目标{target}")
    return -1


def lanqiao_binary_search_example():
    """
    蓝桥杯风格例题：木材加工
    题目：给定n根木材，长度分别为L[i]，现在需要将它们锯成k段长度相同的小木材，
         求小木材的最大可能长度。
    例如：n=3，L=[232, 124, 456]，k=7，最大长度为114
    """
    L = [232, 124, 456]  # 木材长度
    k = 7  # 需要锯成的段数
    
    # 计算可以锯成的段数
    def count_pieces(length):
        if length == 0:
            return 0
        return sum(wood // length for wood in L)
    
    print(f"木材长度: {L}")
    print(f"需要锯成{k}段")
    
    # 二分查找最大可能长度
    left, right = 1, max(L)
    result = 0
    
    while left <= right:
        mid = left + (right - left) // 2
        pieces = count_pieces(mid)
        
        print(f"尝试长度{mid}，可以锯成{pieces}段")
        
        if pieces >= k:
            # 可以锯成k段或更多，尝试更长的长度
            result = mid
            left = mid + 1
        else:
            # 锯成的段数不足k，尝试更短的长度
            right = mid - 1
    
    print(f"最大可能长度: {result}")
    
    return result


def sqrt_calculation(x):
    """
    二分查找应用：计算平方根
    使用二分查找计算x的平方根，精确到小数点后6位
    """
    if x < 0:
        raise ValueError("不能计算负数的平方根")
    if x == 0 or x == 1:
        return x
    
    # 设置精度
    precision = 1e-6
    left, right = 0, max(1, x)  # 确保右边界不小于1
    
    print(f"计算{x}的平方根，精度{precision}")
    
    while right - left > precision:
        mid = left + (right - left) / 2
        mid_square = mid * mid
        
        if abs(mid_square - x) < precision:
            break
        elif mid_square < x:
            left = mid
        else:
            right = mid
    
    result = (left + right) / 2
    print(f"{x}的平方根约为{result:.6f}")
    print(f"验证: {result}^2 = {result*result:.6f}")
    
    return result


def main():
    print("===== 二分查找基本实现 =====")
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    index = binary_search(arr, target)
    print(f"在数组{arr}中查找{target}，索引为{index}")
    
    print("\n===== 带步骤展示的二分查找 =====")
    binary_search_with_steps(arr, target)
    
    print("\n===== 二分查找左边界 =====")
    arr = [1, 3, 5, 5, 5, 7, 9]
    target = 5
    left_bound = binary_search_left_bound(arr, target)
    print(f"在数组{arr}中查找{target}的左边界，索引为{left_bound}")
    
    print("\n===== 二分查找右边界 =====")
    right_bound = binary_search_right_bound(arr, target)
    print(f"在数组{arr}中查找{target}的右边界，索引为{right_bound}")
    
    print("\n===== 蓝桥杯风格例题：木材加工 =====")
    lanqiao_binary_search_example()
    
    print("\n===== 二分查找应用：计算平方根 =====")
    sqrt_calculation(2)


# 让代码可以直接运行
if __name__ == "__main__":
    main()