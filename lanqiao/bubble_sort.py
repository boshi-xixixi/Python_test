# -*- coding: utf-8 -*-
"""
冒泡排序算法实例代码
适用场景：小规模数据排序，教学演示
难度：2级
"""


def bubble_sort(arr):
    """
    冒泡排序实现
    原理：重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来
    时间复杂度：O(n²)，空间复杂度：O(1)
    
    参数：
        arr: 待排序的列表
    返回：
        排序后的列表
    """
    # 创建数组副本，避免修改原数组
    result = arr.copy()
    n = len(result)
    
    # 外循环：控制排序轮数
    for i in range(n):
        # 标记本轮是否发生交换
        swapped = False
        
        # 内循环：比较相邻元素并交换
        # 每轮结束后，最大的元素会冒泡到末尾，因此每轮可以减少比较次数
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换它们
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        
        # 如果本轮没有发生交换，说明数组已经有序，提前退出
        if not swapped:
            break
    
    return result


def optimized_bubble_sort_example():
    """
    优化版冒泡排序示例
    优化点1：添加交换标记，提前结束
    优化点2：记录最后一次交换的位置，减少比较范围
    """
    # 测试数据
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始数组: {test_arr}")
    
    # 创建数组副本
    arr = test_arr.copy()
    n = len(arr)
    
    # 最后一次交换的位置
    last_swap_pos = n - 1
    
    for i in range(n):
        swapped = False
        # 记录本轮交换的位置
        current_swap_pos = 0
        
        for j in range(0, last_swap_pos):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                current_swap_pos = j
        
        # 更新最后一次交换的位置
        last_swap_pos = current_swap_pos
        
        print(f"第{i+1}轮排序后: {arr}")
        
        if not swapped:
            break
    
    print(f"最终排序结果: {arr}")
    return arr


def lanqiao_style_problem():
    """
    蓝桥杯风格例题：成绩排序
    题目：给定一组学生的成绩，要求使用冒泡排序按成绩从高到低排序
    如果成绩相同，则按姓名的字典序排序
    """
    # 示例数据：列表中的元素是(姓名, 成绩)的元组
    students = [("张三", 85), ("李四", 92), ("王五", 78), ("赵六", 92), ("钱七", 85)]
    print(f"原始学生列表: {students}")
    
    # 创建副本
    arr = students.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # 按成绩从高到低排序，成绩相同时按姓名字典序
            if (arr[j][1] < arr[j + 1][1]) or \
               (arr[j][1] == arr[j + 1][1] and arr[j][0] > arr[j + 1][0]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    print(f"排序后学生列表: {arr}")
    return arr


def performance_comparison():
    """
    性能比较：比较普通冒泡排序与优化版冒泡排序在不同数据规模下的性能
    注意：对于大规模数据，冒泡排序效率较低，实际应用中应选择更高效的排序算法
    """
    import random
    import time
    
    # 生成不同规模的随机数据
    sizes = [100, 1000]
    
    for size in sizes:
        # 生成随机数组
        random_arr = [random.randint(0, 10000) for _ in range(size)]
        
        # 测试标准冒泡排序
        start_time = time.time()
        sorted_arr = bubble_sort(random_arr)
        standard_time = time.time() - start_time
        
        print(f"\n数据规模: {size}")
        print(f"标准冒泡排序耗时: {standard_time:.6f}秒")


# 主函数：运行所有示例
def main():
    print("===== 冒泡排序基本实现 =====")
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始数组: {test_arr}")
    sorted_arr = bubble_sort(test_arr)
    print(f"排序后数组: {sorted_arr}")
    print(f"原数组保持不变: {test_arr}")
    
    print("\n===== 优化版冒泡排序示例 =====")
    optimized_bubble_sort_example()
    
    print("\n===== 蓝桥杯风格例题：成绩排序 =====")
    lanqiao_style_problem()
    
    print("\n===== 性能比较 =====")
    performance_comparison()


# 让代码可以直接运行
if __name__ == "__main__":
    main()