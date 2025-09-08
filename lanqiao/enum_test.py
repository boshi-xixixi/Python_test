# -*- coding: utf-8 -*-
"""
枚举算法测试题
请完成以下测试题，检验对枚举算法的理解
"""


# 测试题1：找出1到200之间所有能被3整除但不能被5整除的数
def test_1():
    """
    测试题1：找出1到200之间所有能被3整除但不能被5整除的数
    返回：满足条件的数的列表
    """
    result = []
    # 在这里编写你的代码
    # 遍历1到200之间的所有数
    for num in range(1, 201):
        # 检查是否能被3整除但不能被5整除
        if num % 3 == 0 and num % 5 != 0:
            result.append(num)
    
    return result


# 测试题2：找出所有满足a³ + b³ = c³ + d³的四元组(a, b, c, d)
# 其中1 <= a, b, c, d <= 100，且a <= b，c <= d，(a, b) != (c, d)
def test_2():
    """
    测试题2：找出所有满足a³ + b³ = c³ + d³的四元组(a, b, c, d)
    条件：1 <= a, b, c, d <= 100，且a <= b，c <= d，(a, b) != (c, d)
    返回：满足条件的四元组列表
    """
    result = []
    # 在这里编写你的代码
    # 首先计算所有可能的a³ + b³的值，并存储对应的(a, b)对
    sums = {}
    for a in range(1, 101):
        for b in range(a, 101):
            s = a**3 + b**3
            if s not in sums:
                sums[s] = []
            sums[s].append((a, b))
    
    # 然后检查每个和对应的多对(a, b)
    for s, pairs in sums.items():
        if len(pairs) >= 2:
            # 对于每对不同的(a, b)和(c, d)，添加到结果中
            for i in range(len(pairs)):
                for j in range(i + 1, len(pairs)):
                    a, b = pairs[i]
                    c, d = pairs[j]
                    result.append((a, b, c, d))
    
    return result


# 测试题3：求解百钱百鸡问题
# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100元买100只鸡，有多少种买法？
def test_3():
    """
    测试题3：求解百钱百鸡问题
    条件：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100元买100只鸡
    返回：满足条件的买法列表，每个元素是(公鸡数, 母鸡数, 小鸡数)
    """
    result = []
    # 在这里编写你的代码
    # 遍历可能的公鸡数量
    for cock in range(0, 21):  # 最多买20只公鸡（5*20=100）
        # 遍历可能的母鸡数量
        for hen in range(0, 34):  # 最多买33只母鸡（3*33=99）
            # 计算小鸡数量
            chick = 100 - cock - hen
            # 检查是否满足条件：总钱数为100元，且小鸡数必须是3的倍数
            if chick >= 0 and chick % 3 == 0 and 5*cock + 3*hen + chick/3 == 100:
                result.append((cock, hen, chick))
    
    return result


# 测试题4：寻找阿姆斯特朗数
# 阿姆斯特朗数：一个n位数，其各位数字的n次方和等于该数本身
# 例如：153=1³+5³+3³
# 找出1到10000之间的所有阿姆斯特朗数
def test_4():
    """
    测试题4：寻找阿姆斯特朗数
    条件：1到10000之间的阿姆斯特朗数
    返回：满足条件的数的列表
    """
    result = []
    # 在这里编写你的代码
    for num in range(1, 10001):
        # 转换为字符串，方便获取每一位数字
        num_str = str(num)
        n = len(num_str)  # 数字的位数
        total = 0
        # 计算各位数字的n次方和
        for digit_char in num_str:
            digit = int(digit_char)
            total += digit ** n
        # 检查是否是阿姆斯特朗数
        if total == num:
            result.append(num)
    
    return result


# 主函数：运行所有测试题
def main():
    print("===== 枚举算法测试题 =====")
    
    print("\n测试题1：找出1到200之间所有能被3整除但不能被5整除的数")
    result1 = test_1()
    print(f"满足条件的数共有{len(result1)}个")
    print(f"前10个数: {result1[:10]}...")
    
    print("\n测试题2：找出所有满足a³ + b³ = c³ + d³的四元组(a, b, c, d)")
    # 注意：这个测试可能需要较长时间运行
    # 为了快速测试，可以将范围从1-100改为1-20
    # result2 = test_2()
    # print(f"满足条件的四元组共有{len(result2)}个")
    # print(f"前5个四元组: {result2[:5]}...")
    print("提示：由于计算量较大，此测试已注释掉。如需运行，请取消注释，并可考虑缩小范围。")
    
    print("\n测试题3：求解百钱百鸡问题")
    result3 = test_3()
    print(f"共有{len(result3)}种买法：")
    for i, (cock, hen, chick) in enumerate(result3, 1):
        print(f"买法{i}：公鸡{cock}只，母鸡{hen}只，小鸡{chick}只")
    
    print("\n测试题4：寻找1到10000之间的所有阿姆斯特朗数")
    result4 = test_4()
    print(f"1到10000之间共有{len(result4)}个阿姆斯特朗数：")
    print(result4)


# 让代码可以直接运行
if __name__ == "__main__":
    main()