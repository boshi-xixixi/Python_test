# -*- coding: utf-8 -*-
"""
选择排序算法实例代码
适用场景：小规模数据排序，需要最小化交换操作的场景
难度：3级
"""


def selection_sort(arr):
    """
    选择排序实现
    原理：每次从未排序部分选出最小（或最大）的元素，放到已排序部分的末尾
    时间复杂度：O(n²)，空间复杂度：O(1)
    
    参数：
        arr: 待排序的列表
    返回：
        排序后的列表
    """
    # 创建数组副本，避免修改原数组
    result = arr.copy()
    n = len(result)
    
    # 外循环：控制已排序部分的末尾位置
    for i in range(n):
        # 假设当前位置的元素是未排序部分中的最小值
        min_idx = i
        
        # 内循环：在未排序部分寻找最小值
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        
        # 将找到的最小值与未排序部分的第一个元素交换
        if min_idx != i:
            result[i], result[min_idx] = result[min_idx], result[i]
    
    return result


def selection_sort_with_steps(arr):
    """
    带步骤展示的选择排序
    用于演示选择排序的每一步操作
    """
    # 创建副本
    result = arr.copy()
    n = len(result)
    
    print(f"原始数组: {result}")
    
    for i in range(n):
        min_idx = i
        print(f"\n第{i+1}轮：寻找位置{i}之后的最小值")
        
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
                print(f"  发现更小值 {result[min_idx]} 在位置 {min_idx}")
        
        if min_idx != i:
            print(f"  交换位置 {i} 和 {min_idx}: {result[i]} <-> {result[min_idx]}")
            result[i], result[min_idx] = result[min_idx], result[i]
        else:
            print(f"  位置 {i} 已是最小值，无需交换")
        
        print(f"  本轮排序后: {result}")
    
    print(f"\n最终排序结果: {result}")
    return result


def selection_sort_descending(arr):
    """
    降序选择排序
    每次选择未排序部分中的最大值
    """
    # 创建数组副本
    result = arr.copy()
    n = len(result)
    
    for i in range(n):
        # 寻找未排序部分中的最大值
        max_idx = i
        for j in range(i + 1, n):
            if result[j] > result[max_idx]:
                max_idx = j
        
        # 交换
        if max_idx != i:
            result[i], result[max_idx] = result[max_idx], result[i]
    
    return result


def lanqiao_style_problem():
    """
    蓝桥杯风格例题：寻找第k小的元素
    题目：给定一个数组和一个整数k，使用选择排序的思想找出数组中第k小的元素
    例如：数组[7, 10, 4, 3, 20, 15]，k=3，则第3小的元素是7
    """
    # 示例数据
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    print(f"原始数组: {arr}")
    print(f"寻找第{k}小的元素")
    
    # 创建副本
    result = arr.copy()
    n = len(result)
    
    # 只需要进行k轮选择排序
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        
        # 交换
        result[i], result[min_idx] = result[min_idx], result[i]
        print(f"第{i+1}轮排序后: {result}")
    
    # 第k小的元素就是result[k-1]
    kth_smallest = result[k - 1]
    print(f"第{k}小的元素是: {kth_smallest}")
    
    return kth_smallest


def performance_comparison():
    """
    性能比较：比较选择排序与冒泡排序在不同数据规模下的性能
    """
    import random
    import time
    
    # 生成不同规模的随机数据
    sizes = [100, 1000]
    
    for size in sizes:
        # 生成随机数组
        random_arr = [random.randint(0, 10000) for _ in range(size)]
        
        # 测试选择排序
        start_time = time.time()
        sorted_arr = selection_sort(random_arr)
        selection_time = time.time() - start_time
        
        print(f"\n数据规模: {size}")
        print(f"选择排序耗时: {selection_time:.6f}秒")


# 主函数：运行所有示例
def main():
    print("===== 选择排序基本实现 =====")
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始数组: {test_arr}")
    sorted_arr = selection_sort(test_arr)
    print(f"排序后数组: {sorted_arr}")
    print(f"原数组保持不变: {test_arr}")
    
    print("\n===== 带步骤展示的选择排序 =====")
    selection_sort_with_steps([64, 34, 25, 12, 22, 11, 90])
    
    print("\n===== 降序选择排序 =====")
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_desc = selection_sort_descending(test_arr)
    print(f"原始数组: {test_arr}")
    print(f"降序排序后: {sorted_desc}")
    
    print("\n===== 蓝桥杯风格例题：寻找第k小的元素 =====")
    lanqiao_style_problem()
    
    print("\n===== 性能比较 =====")
    performance_comparison()


# 让代码可以直接运行
if __name__ == "__main__":
    main()