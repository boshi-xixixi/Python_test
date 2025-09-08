# -*- coding: utf-8 -*-
"""
贪心算法实例代码
适用场景：问题具有贪心选择性质和最优子结构性质的情况
难度：1-5级（根据具体问题复杂度而定）
"""


def fractional_knapsack():
    """
    分数背包问题
    原理：每次选择性价比（价值/重量）最高的物品放入背包
    这是一个典型的可以用贪心算法解决的问题
    """
    # 物品列表：(价值, 重量)
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50  # 背包容量
    
    # 计算每个物品的性价比（价值/重量），并按降序排序
    # 这里使用负号是为了让sorted函数按降序排列
    items_with_ratio = [(value, weight, value/weight) for value, weight in items]
    items_sorted = sorted(items_with_ratio, key=lambda x: x[2], reverse=True)
    
    total_value = 0  # 总价值
    remaining_capacity = capacity  # 剩余容量
    selected_items = []  # 选择的物品
    
    print(f"背包容量: {capacity}")
    print(f"物品列表: {items}")
    print(f"按性价比排序后的物品: {items_sorted}")
    
    # 贪心选择
    for value, weight, ratio in items_sorted:
        if weight <= remaining_capacity:
            # 可以放入整个物品
            total_value += value
            remaining_capacity -= weight
            selected_items.append((value, weight, 1.0))  # 1.0表示放入整个物品
            print(f"放入整个物品: 价值={value}, 重量={weight}, 剩余容量={remaining_capacity}")
        else:
            # 只能放入部分物品
            fraction = remaining_capacity / weight
            total_value += value * fraction
            selected_items.append((value, weight, fraction))  # fraction表示放入的比例
            print(f"放入物品的一部分: 价值={value*fraction:.2f}, 重量={remaining_capacity}, 比例={fraction:.2f}")
            remaining_capacity = 0
            break  # 背包已满
    
    print(f"\n总价值: {total_value}")
    print(f"选择的物品及比例: {selected_items}")
    
    return total_value


def activity_selection():
    """
    活动选择问题
    原理：每次选择结束时间最早的活动，为后续活动留出更多时间
    """
    # 活动列表：(开始时间, 结束时间)
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    
    # 按结束时间排序
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    selected_activities = []  # 选择的活动
    last_end_time = 0  # 上一个选择的活动的结束时间
    
    print(f"活动列表: {activities}")
    print(f"按结束时间排序后的活动: {sorted_activities}")
    
    # 贪心选择
    for start, end in sorted_activities:
        if start >= last_end_time:
            # 可以选择当前活动，不会与已选活动冲突
            selected_activities.append((start, end))
            last_end_time = end
    
    print(f"\n选择的活动数量: {len(selected_activities)}")
    print(f"选择的活动: {selected_activities}")
    
    return selected_activities


def coin_change():
    """
    硬币找零问题
    原理：每次选择面值最大的硬币，但该算法仅适用于某些特定的硬币体系（如人民币）
    """
    # 硬币面额（按降序排列）
    coins = [100, 50, 20, 10, 5, 1]
    # 需要找零的金额
    amount = 376
    
    change = {}  # 存储每种硬币的数量
    remaining_amount = amount
    
    print(f"需要找零的金额: {amount}")
    print(f"硬币面额: {coins}")
    
    # 贪心选择
    for coin in coins:
        if remaining_amount >= coin:
            count = remaining_amount // coin  # 计算当前面额的硬币数量
            change[coin] = count
            remaining_amount -= coin * count
            print(f"使用{count}个{coin}元硬币，剩余金额: {remaining_amount}")
        
        if remaining_amount == 0:
            break
    
    total_coins = sum(change.values())  # 总硬币数
    print(f"\n最少硬币数量: {total_coins}")
    print(f"找零方案: {change}")
    
    return change


def lanqiao_greedy_example():
    """
    蓝桥杯风格例题：最大数问题
    题目：给定一个正整数n，移除其中的k个数字，使得剩下的数字组成的新数最大
    例如：n=12345，k=2，移除2和1，得到最大数345
    """
    n = "12345"  # 注意：这里用字符串表示，方便处理每一位数字
    k = 2
    
    print(f"原始数字: {n}")
    print(f"需要移除的数字个数: {k}")
    
    stack = []  # 使用栈来存储选择的数字
    remove_count = 0  # 已移除的数字个数
    
    # 遍历每一位数字
    for digit in n:
        # 当栈不为空，且当前数字大于栈顶数字，且还可以移除数字时，弹出栈顶数字
        while stack and digit > stack[-1] and remove_count < k:
            stack.pop()
            remove_count += 1
        stack.append(digit)
    
    # 如果还需要移除更多数字，从栈顶移除
    while remove_count < k and stack:
        stack.pop()
        remove_count += 1
    
    # 构建结果
    result = ''.join(stack)
    
    print(f"移除{k}个数字后得到的最大数: {result}")
    
    return result


def interval_scheduling():
    """
    区间调度问题
    原理：选择尽可能多的不重叠区间
    这是活动选择问题的一个变种
    """
    # 区间列表：(开始时间, 结束时间)
    intervals = [(1, 3), (2, 5), (3, 8), (4, 7), (6, 10), (9, 12)]
    
    # 按结束时间排序
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    selected_intervals = []  # 选择的区间
    last_end_time = 0  # 上一个选择的区间的结束时间
    
    print(f"区间列表: {intervals}")
    print(f"按结束时间排序后的区间: {sorted_intervals}")
    
    # 贪心选择
    for start, end in sorted_intervals:
        if start >= last_end_time:
            # 可以选择当前区间，不会与已选区间冲突
            selected_intervals.append((start, end))
            last_end_time = end
    
    print(f"\n选择的区间数量: {len(selected_intervals)}")
    print(f"选择的区间: {selected_intervals}")
    
    return selected_intervals


def main():
    print("===== 分数背包问题 =====")
    fractional_knapsack()
    
    print("\n===== 活动选择问题 =====")
    activity_selection()
    
    print("\n===== 硬币找零问题 =====")
    coin_change()
    
    print("\n===== 蓝桥杯风格例题：最大数问题 =====")
    lanqiao_greedy_example()
    
    print("\n===== 区间调度问题 =====")
    interval_scheduling()


# 让代码可以直接运行
if __name__ == "__main__":
    main()