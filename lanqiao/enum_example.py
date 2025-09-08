# -*- coding: utf-8 -*-
"""
枚举算法实例代码
适用场景：当问题的解空间较小，可以通过遍历所有可能情况来找到答案时
难度：1-3级（根据具体问题复杂度而定）
"""


def simple_enum_example():
    """
    简单枚举示例：找出1到100之间的所有素数
    素数定义：大于1的自然数，除了1和它本身外，不能被其他自然数整除
    """
    primes = []
    for num in range(2, 101):  # 从2开始遍历到100
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  # 只需检查到平方根
            if num % i == 0:
                is_prime = False
                break  # 一旦找到一个因数，立即退出内层循环
        if is_prime:
            primes.append(num)
    
    print("1到100之间的素数有：")
    print(primes)
    return primes


def enum_with_condition():
    """
    带条件的枚举示例：找出所有满足a² + b² = c²的三位数组合(a, b, c)
    这是蓝桥杯常见的枚举类问题类型
    """
    results = []
    # 遍历所有可能的a、b、c组合
    for a in range(100, 1000):
        for b in range(a, 1000):  # b从a开始，避免重复
            for c in range(b, 1000):
                if a * a + b * b == c * c:
                    results.append((a, b, c))
                    print(f"找到一组勾股数: {a}^2 + {b}^2 = {c}^2")
    
    print(f"总共找到{len(results)}组三位数勾股数")
    return results


def optimize_enum_example():
    """
    优化的枚举示例：寻找水仙花数
    水仙花数：一个三位数，其各位数字的立方和等于该数本身，如153=1³+5³+3³
    优化点：减少不必要的计算，直接计算各位数字
    """
    narcissistic_numbers = []
    
    for num in range(100, 1000):  # 三位数范围
        # 直接分解各位数字
        hundreds = num // 100        # 百位
        tens = (num // 10) % 10      # 十位
        units = num % 10             # 个位
        
        # 检查是否满足水仙花数条件
        if hundreds**3 + tens**3 + units**3 == num:
            narcissistic_numbers.append(num)
            print(f"找到水仙花数: {num}")
    
    print(f"三位数中的水仙花数共有{len(narcissistic_numbers)}个")
    return narcissistic_numbers


def lanqiao_2023_example():
    """
    蓝桥杯风格例题：2023年C组真题类型
    题目：给定一个正整数n，找出所有满足以下条件的五位数组合(a,b,c,d,e)：
         1. a*10000 + b*1000 + c*100 + d*10 + e = n
         2. a、b、c、d、e均为0-9的数字，且a≠0
         3. 数字之和a+b+c+d+e为质数
    """
    n = 20230  # 示例输入
    valid_combinations = []
    
    # 判断一个数是否为质数的辅助函数
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # 枚举所有可能的五位数组合
    for a in range(1, 10):  # a不能为0
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    for e in range(0, 10):
                        # 检查是否等于n
                        if a*10000 + b*1000 + c*100 + d*10 + e == n:
                            # 检查数字之和是否为质数
                            if is_prime(a + b + c + d + e):
                                valid_combinations.append((a, b, c, d, e))
                                print(f"找到符合条件的组合: {a}{b}{c}{d}{e}")
    
    print(f"对于n={n}，共有{len(valid_combinations)}个符合条件的五位数组合")
    return valid_combinations


# 主函数：运行所有示例
def main():
    print("===== 简单枚举示例：找出1到100之间的素数 =====")
    simple_enum_example()
    
    print("\n===== 带条件的枚举示例：找出所有三位数勾股数 =====")
    # 注意：这个函数运行时间可能较长，因为要遍历大量组合
    # 如需快速查看效果，可以将范围缩小，如range(100, 200)
    
    print("\n===== 优化的枚举示例：寻找水仙花数 =====")
    optimize_enum_example()
    
    print("\n===== 蓝桥杯风格例题：寻找满足条件的五位数组合 =====")
    lanqiao_2023_example()


# 让代码可以直接运行
if __name__ == "__main__":
    main()