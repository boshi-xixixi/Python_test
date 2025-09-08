# -*- coding: utf-8 -*-
"""
高精度算法实例代码
适用场景：处理超过普通数据类型范围的大数运算
难度：1-5级（根据具体运算复杂度而定）
"""


def high_precision_add(a, b):
    """
    高精度加法
    原理：模拟竖式加法，从低位到高位逐位相加，处理进位
    
    参数：
        a: 字符串形式的大整数
        b: 字符串形式的大整数
    返回：
        字符串形式的和
    """
    # 确保a是较长的数，方便处理
    if len(a) < len(b):
        a, b = b, a
    
    # 反转字符串，使低位在前，便于从低位开始相加
    a_rev = a[::-1]
    b_rev = b[::-1]
    
    result = []  # 存储结果的每一位
    carry = 0  # 进位
    
    print(f"计算 {a} + {b}")
    
    # 逐位相加
    for i in range(len(a_rev)):
        digit_a = int(a_rev[i])
        # 如果b已经处理完，就取0
        digit_b = int(b_rev[i]) if i < len(b_rev) else 0
        
        # 计算当前位的和
        total = digit_a + digit_b + carry
        # 当前位的值
        current_digit = total % 10
        # 更新进位
        carry = total // 10
        
        result.append(str(current_digit))
        print(f"  位{i+1}: {digit_a} + {digit_b} + {carry if i < len(b_rev) else 0} = {total} → {current_digit} (进位{carry})")
    
    # 如果最高位还有进位，添加到结果中
    if carry > 0:
        result.append(str(carry))
        print(f"  最高位进位: {carry}")
    
    # 反转结果，得到正确的顺序
    final_result = ''.join(result[::-1])
    print(f"结果: {final_result}")
    
    return final_result


def high_precision_subtract(a, b):
    """
    高精度减法
    原理：模拟竖式减法，从低位到高位逐位相减，处理借位
    注意：该函数假设a >= b
    
    参数：
        a: 字符串形式的大整数（被减数）
        b: 字符串形式的大整数（减数）
    返回：
        字符串形式的差
    """
    # 反转字符串，使低位在前
    a_rev = a[::-1]
    b_rev = b[::-1]
    
    result = []  # 存储结果的每一位
    borrow = 0  # 借位
    
    print(f"计算 {a} - {b}")
    
    # 逐位相减
    for i in range(len(a_rev)):
        digit_a = int(a_rev[i]) - borrow
        # 如果b已经处理完，就取0
        digit_b = int(b_rev[i]) if i < len(b_rev) else 0
        
        # 处理借位
        if digit_a < digit_b:
            digit_a += 10
            borrow = 1
        else:
            borrow = 0
        
        # 计算当前位的差
        diff = digit_a - digit_b
        result.append(str(diff))
        print(f"  位{i+1}: {digit_a} - {digit_b} = {diff} (借位{borrow})")
    
    # 反转结果，得到正确的顺序
    final_result = ''.join(result[::-1])
    # 移除前导零
    final_result = final_result.lstrip('0')
    # 如果结果为空，返回"0"
    final_result = final_result if final_result else "0"
    
    print(f"结果: {final_result}")
    
    return final_result


def high_precision_multiply(a, b):
    """
    高精度乘法
    原理：模拟竖式乘法，将a的每一位与b的每一位相乘，处理进位
    
    参数：
        a: 字符串形式的大整数
        b: 字符串形式的大整数
    返回：
        字符串形式的积
    """
    # 初始化结果数组，长度为两数长度之和
    result = [0] * (len(a) + len(b))
    
    print(f"计算 {a} × {b}")
    
    # 逐位相乘
    for i in range(len(a)-1, -1, -1):
        for j in range(len(b)-1, -1, -1):
            # 计算当前位的乘积
            product = int(a[i]) * int(b[j])
            # 加上当前位置已有的值
            sum_ = product + result[i+j+1]
            # 更新当前位置的值
            result[i+j+1] = sum_ % 10
            # 更新高位的进位
            result[i+j] += sum_ // 10
            
            print(f"  a[{i}]={a[i]}, b[{j}]={b[j]}, 乘积={product}, 位置{i+j+1}={sum_} → {result[i+j+1]} (进位{sum_//10})")
    
    # 移除前导零
    i = 0
    while i < len(result) and result[i] == 0:
        i += 1
    
    # 将结果数组转换为字符串
    final_result = ''.join(map(str, result[i:])) if i < len(result) else "0"
    
    print(f"结果: {final_result}")
    
    return final_result


def high_precision_power(base, exponent):
    """
    高精度幂运算
    原理：使用快速幂算法结合高精度乘法
    
    参数：
        base: 字符串形式的大整数
        exponent: 整数指数
    返回：
        字符串形式的幂
    """
    if exponent == 0:
        return "1"
    if exponent == 1:
        return base
    
    print(f"计算 {base}^{exponent}")
    
    # 快速幂算法
    result = "1"
    current = base
    
    while exponent > 0:
        if exponent % 2 == 1:
            # 如果当前指数是奇数，将结果乘以当前值
            result = high_precision_multiply(result, current)
        # 平方当前值
        current = high_precision_multiply(current, current)
        # 指数除以2
        exponent //= 2
        
        print(f"  exponent={exponent}, result={result}, current={current}")
    
    return result


def lanqiao_high_precision_example():
    """
    蓝桥杯风格例题：大数阶乘
    题目：计算n的阶乘，其中n可能很大
    例如：100的阶乘有158位数字
    """
    n = 20  # 计算20的阶乘，实际可以处理更大的n
    
    # 初始化结果为1
    result = "1"
    
    print(f"计算 {n} 的阶乘")
    
    # 从1乘到n
    for i in range(2, n + 1):
        result = high_precision_multiply(result, str(i))
        print(f"  {i}! = {result}")
    
    print(f"{n}! 的位数: {len(result)}")
    print(f"{n}! = {result}")
    
    return result


def high_precision_compare(a, b):
    """
    高精度比较
    比较两个大整数的大小
    
    参数：
        a: 字符串形式的大整数
        b: 字符串形式的大整数
    返回：
        1表示a > b，0表示a = b，-1表示a < b
    """
    # 移除前导零
    a = a.lstrip('0')
    b = b.lstrip('0')
    
    # 如果结果为空，说明原来是0
    if not a:
        a = "0"
    if not b:
        b = "0"
    
    # 首先比较长度，长度较长的数更大
    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1
    else:
        # 长度相同，逐位比较
        for i in range(len(a)):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1
        # 所有位都相同
        return 0


def main():
    print("===== 高精度加法 =====")
    high_precision_add("9999999999", "1")
    
    print("\n===== 高精度减法 =====")
    high_precision_subtract("10000000000", "1")
    
    print("\n===== 高精度乘法 =====")
    high_precision_multiply("999", "999")
    
    print("\n===== 高精度幂运算 =====")
    high_precision_power("2", "10")
    
    print("\n===== 蓝桥杯风格例题：大数阶乘 =====")
    lanqiao_high_precision_example()
    
    print("\n===== 高精度比较 =====")
    print(f"999 和 1000 比较结果: {high_precision_compare('999', '1000')}")
    print(f"1000 和 1000 比较结果: {high_precision_compare('1000', '1000')}")
    print(f"1001 和 1000 比较结果: {high_precision_compare('1001', '1000')}")


# 让代码可以直接运行
if __name__ == "__main__":
    main()