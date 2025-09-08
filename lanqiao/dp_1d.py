# -*- coding: utf-8 -*-
"""
普通一维动态规划(DP)算法实例代码
适用场景：具有最优子结构和重叠子问题性质的问题
难度：3-5级（根据具体问题复杂度而定）
"""


def fibonacci_dp():
    """
    斐波那契数列的DP解法
    原理：使用数组存储中间结果，避免重复计算
    时间复杂度：O(n)，空间复杂度：O(n)
    """
    n = 10  # 计算第10个斐波那契数
    
    # 边界条件：F(0)=0, F(1)=1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # 创建DP数组
    dp = [0] * (n + 1)
    dp[1] = 1  # F(1)=1
    
    print(f"计算斐波那契数列的前{n+1}项")
    print(f"dp[0] = {dp[0]}")
    print(f"dp[1] = {dp[1]}")
    
    # 填充DP数组
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        print(f"dp[{i}] = dp[{i-1}] + dp[{i-2}] = {dp[i-1]} + {dp[i-2]} = {dp[i]}")
    
    print(f"第{n}个斐波那契数是: {dp[n]}")
    
    # 空间优化版本（空间复杂度O(1)）
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    print(f"空间优化后，第{n}个斐波那契数是: {b}")
    
    return dp[n]


def coin_change_dp():
    """
    硬币找零问题的DP解法
    题目：给定不同面额的硬币和一个总金额，计算可以凑成总金额所需的最少的硬币个数
    时间复杂度：O(amount * n)，空间复杂度：O(amount)
    """
    coins = [1, 2, 5]  # 硬币面额
    amount = 11  # 总金额
    
    # 创建DP数组，dp[i]表示凑成金额i所需的最少硬币个数
    # 初始值设为amount+1，表示一个不可能达到的值
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # 凑成金额0不需要任何硬币
    
    print(f"硬币面额: {coins}")
    print(f"总金额: {amount}")
    print(f"初始dp数组: {dp}")
    
    # 填充DP数组
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
        print(f"dp[{i}] = {dp[i]}")
    
    result = dp[amount] if dp[amount] != amount + 1 else -1
    print(f"凑成金额{amount}所需的最少硬币个数: {result}")
    
    return result


def climb_stairs():
    """
    爬楼梯问题的DP解法
    题目：爬n级楼梯，每次可以爬1或2级，有多少种不同的方法？
    时间复杂度：O(n)，空间复杂度：O(n)
    """
    n = 10  # 楼梯级数
    
    # 边界条件
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # 创建DP数组，dp[i]表示爬i级楼梯的不同方法数
    dp = [0] * (n + 1)
    dp[1] = 1  # 爬1级楼梯只有1种方法
    dp[2] = 2  # 爬2级楼梯有2种方法
    
    print(f"计算爬{n}级楼梯的不同方法数")
    print(f"dp[1] = {dp[1]}")
    print(f"dp[2] = {dp[2]}")
    
    # 填充DP数组
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # 状态转移方程
        print(f"dp[{i}] = dp[{i-1}] + dp[{i-2}] = {dp[i-1]} + {dp[i-2]} = {dp[i]}")
    
    print(f"爬{n}级楼梯共有{dp[n]}种不同的方法")
    
    # 空间优化版本
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    
    print(f"空间优化后，爬{n}级楼梯共有{b}种不同的方法")
    
    return dp[n]


def maximum_subarray():
    """
    最大子数组和问题的DP解法（Kadane算法）
    题目：给定一个整数数组，找到一个具有最大和的连续子数组
    时间复杂度：O(n)，空间复杂度：O(n)
    """
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # 示例数组
    
    # 创建DP数组，dp[i]表示以第i个元素结尾的最大子数组和
    dp = [0] * len(nums)
    dp[0] = nums[0]  # 边界条件
    
    print(f"数组: {nums}")
    print(f"dp[0] = {dp[0]}")
    
    # 填充DP数组
    for i in range(1, len(nums)):
        # 状态转移方程：要么将当前元素加入前面的子数组，要么以当前元素开始新的子数组
        dp[i] = max(nums[i], dp[i-1] + nums[i])
        print(f"dp[{i}] = max({nums[i]}, {dp[i-1]} + {nums[i]}) = {dp[i]}")
    
    # 最大子数组和就是dp数组中的最大值
    max_sum = max(dp)
    
    # 找到最大子数组的起始和结束索引
    end_index = dp.index(max_sum)
    start_index = end_index
    current_sum = max_sum
    
    while start_index > 0 and current_sum - nums[start_index] == dp[start_index - 1]:
        current_sum -= nums[start_index]
        start_index -= 1
    
    max_subarray = nums[start_index:end_index + 1]
    
    print(f"最大子数组和: {max_sum}")
    print(f"最大子数组: {max_subarray}")
    
    # 空间优化版本
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    print(f"空间优化后，最大子数组和: {max_sum}")
    
    return max_sum


def lanqiao_dp_example():
    """
    蓝桥杯风格例题：背包问题（0-1背包）
    题目：给定n个物品，每个物品有重量w[i]和价值v[i]，以及一个容量为C的背包，
         每个物品只能选择或不选择，求背包能装下的最大价值
    这里我们用一维DP数组来实现，空间优化版本
    """
    n = 4  # 物品数量
    C = 8  # 背包容量
    w = [2, 3, 4, 5]  # 物品重量
    v = [3, 4, 5, 6]  # 物品价值
    
    # 创建一维DP数组，dp[j]表示容量为j的背包能装下的最大价值
    dp = [0] * (C + 1)
    
    print(f"物品数量: {n}")
    print(f"背包容量: {C}")
    print(f"物品重量: {w}")
    print(f"物品价值: {v}")
    
    # 填充DP数组
    for i in range(n):
        # 逆序遍历容量，避免重复选择物品
        for j in range(C, w[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])
        print(f"处理物品{i+1}后，dp数组: {dp}")
    
    print(f"背包能装下的最大价值: {dp[C]}")
    
    return dp[C]


def main():
    print("===== 斐波那契数列的DP解法 =====")
    fibonacci_dp()
    
    print("\n===== 硬币找零问题的DP解法 =====")
    coin_change_dp()
    
    print("\n===== 爬楼梯问题的DP解法 =====")
    climb_stairs()
    
    print("\n===== 最大子数组和问题的DP解法 =====")
    maximum_subarray()
    
    print("\n===== 蓝桥杯风格例题：背包问题（0-1背包）=====")
    lanqiao_dp_example()


# 让代码可以直接运行
if __name__ == "__main__":
    main()