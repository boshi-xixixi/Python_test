# -*- coding: utf-8 -*-
"""
插入排序算法实例代码
适用场景：小规模数据排序，几乎已排序的数据，需要稳定排序的场景
难度：3级
"""


def insertion_sort(arr):
    """
    插入排序实现
    原理：将数组分为已排序部分和未排序部分，每次从未排序部分取出一个元素插入到已排序部分的正确位置
    时间复杂度：O(n²)，空间复杂度：O(1)
    
    参数：
        arr: 待排序的列表
    返回：
        排序后的列表
    """
    # 创建数组副本，避免修改原数组
    result = arr.copy()
    n = len(result)
    
    # 外循环：遍历未排序部分的元素
    # 从第二个元素开始，因为第一个元素被视为已排序
    for i in range(1, n):
        # 保存当前要插入的元素
        key = result[i]
        # j指向已排序部分的最后一个元素
        j = i - 1
        
        # 内循环：在已排序部分寻找正确的插入位置
        # 将所有大于key的元素向后移动一位
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        
        # 插入元素到正确位置
        result[j + 1] = key
    
    return result


def insertion_sort_with_steps(arr):
    """
    带步骤展示的插入排序
    用于演示插入排序的每一步操作
    """
    # 创建副本
    result = arr.copy()
    n = len(result)
    
    print(f"原始数组: {result}")
    
    for i in range(1, n):
        key = result[i]
        j = i - 1
        
        print(f"\n第{i}轮：插入元素 {key}")
        print(f"  插入前: {result}")
        
        # 寻找插入位置并移动元素
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            print(f"  移动: result[{j+1}] = result[{j}] = {result[j]}")
            j -= 1
        
        # 插入元素
        result[j + 1] = key
        print(f"  插入: result[{j+1}] = {key}")
        print(f"  本轮排序后: {result}")
    
    print(f"\n最终排序结果: {result}")
    return result


def optimized_insertion_sort(arr):
    """
    优化的插入排序
    使用二分查找来寻找插入位置，减少比较次数
    注意：这不会改变时间复杂度的阶，因为元素移动的次数仍然是O(n²)
    """
    result = arr.copy()
    n = len(result)
    
    for i in range(1, n):
        key = result[i]
        # 使用二分查找寻找插入位置
        left, right = 0, i
        
        while left < right:
            mid = (left + right) // 2
            if result[mid] > key:
                right = mid
            else:
                left = mid + 1
        
        # 移动元素并插入
        # 注意：这里我们需要将从left到i-1的元素都向后移动一位
        for j in range(i, left, -1):
            result[j] = result[j - 1]
        
        result[left] = key
    
    return result


def lanqiao_style_problem():
    """
    蓝桥杯风格例题：纸牌排序
    题目：有一堆纸牌，每次只能将一张牌插入到已整理好的牌堆中的正确位置
    要求使用插入排序模拟这个过程，并计算最少需要多少次插入操作
    """
    # 示例数据：表示纸牌的数字
    cards = [5, 2, 4, 6, 1, 3]
    print(f"原始牌堆: {cards}")
    
    # 创建副本
    result = cards.copy()
    n = len(result)
    insert_count = 0
    
    # 模拟插入排序过程
    for i in range(1, n):
        key = result[i]
        j = i - 1
        
        # 检查是否需要移动（即是否需要插入操作）
        need_insert = False
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
            need_insert = True
        
        result[j + 1] = key
        
        # 如果发生了移动，则插入计数加1
        if need_insert:
            insert_count += 1
            print(f"插入第{i+1}张牌 {key}，当前牌堆: {result}")
        else:
            print(f"第{i+1}张牌 {key} 已在正确位置")
    
    print(f"\n排序后牌堆: {result}")
    print(f"最少需要{insert_count}次插入操作")
    return insert_count


def performance_comparison():
    """
    性能比较：比较插入排序在不同数据分布下的性能
    """
    import random
    import time
    
    # 生成不同类型的数据
    size = 1000
    
    # 随机数据
    random_arr = [random.randint(0, 10000) for _ in range(size)]
    
    # 已排序数据
    sorted_arr = list(range(size))
    
    # 逆序数据
    reversed_arr = list(range(size, 0, -1))
    
    # 接近排序的数据（只有10%的数据是随机的）
    nearly_sorted = list(range(size))
    for _ in range(size // 10):
        i, j = random.randint(0, size-1), random.randint(0, size-1)
        nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]
    
    # 测试并比较性能
    data_types = [
        ("随机数据", random_arr),
        ("已排序数据", sorted_arr),
        ("逆序数据", reversed_arr),
        ("接近排序数据", nearly_sorted)
    ]
    
    for name, arr in data_types:
        start_time = time.time()
        sorted_result = insertion_sort(arr)
        elapsed_time = time.time() - start_time
        print(f"{name} - 排序耗时: {elapsed_time:.6f}秒")


# 主函数：运行所有示例
def main():
    print("===== 插入排序基本实现 =====")
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始数组: {test_arr}")
    sorted_arr = insertion_sort(test_arr)
    print(f"排序后数组: {sorted_arr}")
    print(f"原数组保持不变: {test_arr}")
    
    print("\n===== 带步骤展示的插入排序 =====")
    insertion_sort_with_steps([64, 34, 25, 12, 22, 11, 90])
    
    print("\n===== 优化的插入排序（二分查找）=====")
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    optimized_sorted = optimized_insertion_sort(test_arr)
    print(f"原始数组: {test_arr}")
    print(f"优化排序后: {optimized_sorted}")
    
    print("\n===== 蓝桥杯风格例题：纸牌排序 =====")
    lanqiao_style_problem()
    
    print("\n===== 性能比较 =====")
    performance_comparison()


# 让代码可以直接运行
if __name__ == "__main__":
    main()