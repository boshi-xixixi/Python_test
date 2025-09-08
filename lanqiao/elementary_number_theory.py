# -*- coding: utf-8 -*-
"""
初等数论算法实例代码
适用场景：涉及整数性质、素数、模运算等数学问题
难度：3-5级（根据具体问题复杂度而定）
"""


def gcd(a, b):
    """
    计算最大公约数（欧几里得算法）
    原理：gcd(a, b) = gcd(b, a % b)，当b=0时，gcd(a, 0) = a
    时间复杂度：O(log min(a, b))
    
    参数：
        a: 正整数
        b: 正整数
    返回：
        a和b的最大公约数
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    计算最小公倍数
    原理：lcm(a, b) = a * b // gcd(a, b)
    时间复杂度：O(log min(a, b))
    
    参数：
        a: 正整数
        b: 正整数
    返回：
        a和b的最小公倍数
    """
    if a == 0 or b == 0:
        return 0
    return a * b // gcd(a, b)


def is_prime(n):
    """
    判断一个数是否为素数
    原理：检查从2到sqrt(n)的所有整数是否能整除n
    时间复杂度：O(sqrt(n))
    
    参数：
        n: 正整数
    返回：
        如果n是素数，返回True，否则返回False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # 检查所有形如6k±1的数，直到sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(max_n):
    """
    埃拉托斯特尼筛法：找出小于等于max_n的所有素数
    原理：从2开始，将每个素数的倍数标记为合数
    时间复杂度：O(n log log n)
    
    参数：
        max_n: 最大整数
    返回：
        一个布尔数组，is_prime[i]表示i是否为素数
    """
    if max_n < 2:
        return []
    
    # 初始化数组，假设所有数都是素数
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0和1不是素数
    
    # 从2开始筛选
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            # 将i的所有倍数标记为合数
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    
    # 返回所有素数
    primes = [i for i, val in enumerate(is_prime) if val]
    return primes, is_prime


def prime_factorization(n):
    """
    质因数分解
    原理：从2开始，依次检查每个素数是否是n的因数
    时间复杂度：O(sqrt(n))
    
    参数：
        n: 正整数
    返回：
        一个字典，键是质因数，值是该质因数的指数
    """
    factors = {}  # 存储质因数及其指数
    
    # 处理2的因子
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n = n // 2
    
    # 处理奇数因子
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n = n // i
        i += 2
    
    # 如果n本身是一个素数
    if n > 2:
        factors[n] = 1
    
    return factors


def fast_power(base, exponent, mod=None):
    """
    快速幂算法
    原理：通过二进制分解指数，将幂运算转换为乘法运算
    时间复杂度：O(log exponent)
    
    参数：
        base: 底数
        exponent: 指数
        mod: 模数，如果提供则进行模运算
    返回：
        base^exponent 或 base^exponent % mod
    """
    result = 1
    current_base = base
    
    while exponent > 0:
        # 如果当前位是1，将当前基数乘到结果中
        if exponent % 2 == 1:
            if mod:
                result = (result * current_base) % mod
            else:
                result *= current_base
        
        # 平方当前基数
        if mod:
            current_base = (current_base * current_base) % mod
        else:
            current_base *= current_base
        
        # 右移一位，相当于除以2取整
        exponent = exponent // 2
    
    return result


def euler_phi(n):
    """
    计算欧拉函数φ(n)：小于n且与n互质的正整数的个数
    原理：φ(n) = n * product(1 - 1/p)，其中p是n的所有不同质因数
    时间复杂度：O(sqrt(n))
    
    参数：
        n: 正整数
    返回：
        欧拉函数φ(n)的值
    """
    if n == 0:
        return 0
    result = n
    
    # 对n进行质因数分解，并应用欧拉函数公式
    # 处理2的因子
    if n % 2 == 0:
        while n % 2 == 0:
            n = n // 2
        result -= result // 2
    
    # 处理奇数因子
    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i
            result -= result // i
        i += 2
    
    # 如果n本身是一个素数
    if n > 2:
        result -= result // n
    
    return result


def chinese_remainder_theorem(a_list, m_list):
    """
    中国剩余定理
    原理：求解同余方程组x ≡ a_i mod m_i，其中m_i两两互质
    时间复杂度：O(k log M)，其中k是方程个数，M是所有m_i的乘积
    
    参数：
        a_list: 余数列表
        m_list: 模数列表
    返回：
        方程组的解x，如果无解则返回None
    """
    # 检查模数是否两两互质
    for i in range(len(m_list)):
        for j in range(i + 1, len(m_list)):
            if gcd(m_list[i], m_list[j]) != 1:
                print("模数不是两两互质的，无法使用中国剩余定理")
                return None
    
    # 计算所有模数的乘积
    M = 1
    for m in m_list:
        M *= m
    
    # 计算解x
    x = 0
    for a, m in zip(a_list, m_list):
        Mi = M // m  # Mi = M / mi
        # 计算Mi在模m下的逆元
        Mi_inv = 0
        for i in range(1, m):
            if (Mi * i) % m == 1:
                Mi_inv = i
                break
        x = (x + a * Mi * Mi_inv) % M
    
    return x


def lanqiao_number_theory_example():
    """
    蓝桥杯风格例题：阶乘末尾零的个数
    题目：计算n!的末尾有多少个连续的零
    原理：末尾的零由因子10产生，而10 = 2 * 5，由于2的数量远多于5，
         所以只需要计算n!中5的因子个数
    """
    def count_trailing_zeros(n):
        count = 0
        while n > 0:
            n = n // 5  # 计算包含5的因子的数的个数
            count += n  # 累加结果
        return count
    
    # 测试用例
    test_cases = [5, 10, 20, 50, 100]
    
    print("蓝桥杯风格例题：阶乘末尾零的个数")
    for n in test_cases:
        zeros = count_trailing_zeros(n)
        print(f"{n}! 的末尾有{zeros}个连续的零")


def modular_equation_solver(a, b, m):
    """
    求解模线性方程ax ≡ b (mod m)
    原理：使用扩展欧几里得算法
    
    参数：
        a: 系数
        b: 常数项
        m: 模数
    返回：
        方程的解的列表，如果无解则返回空列表
    """
    # 计算a和m的最大公约数
    d = gcd(a, m)
    
    # 如果d不整除b，则方程无解
    if b % d != 0:
        return []
    
    # 使用扩展欧几里得算法找到一个特解
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            g, x, y = extended_gcd(b, a % b)
            return (g, y, x - (a // b) * y)
    
    g, x0, y0 = extended_gcd(a, m)
    
    # 计算特解
    x0 = (x0 * (b // d)) % (m // d)
    
    # 方程共有d个解，形式为x = x0 + k*(m/d)，其中k = 0, 1, ..., d-1
    solutions = []
    for k in range(d):
        solution = (x0 + k * (m // d)) % m
        solutions.append(solution)
    
    return solutions


def main():
    print("===== 最大公约数和最小公倍数 =====")
    a, b = 48, 36
    print(f"gcd({a}, {b}) = {gcd(a, b)}")
    print(f"lcm({a}, {b}) = {lcm(a, b)}")
    
    print("\n===== 素数判定 =====")
    test_numbers = [17, 20, 97, 100]
    for num in test_numbers:
        print(f"{num} 是素数: {is_prime(num)}")
    
    print("\n===== 埃拉托斯特尼筛法 =====")
    max_n = 100
    primes, is_prime_array = sieve_of_eratosthenes(max_n)
    print(f"小于等于{max_n}的素数有{len(primes)}个:")
    print(primes)
    
    print("\n===== 质因数分解 =====")
    n = 120
    factors = prime_factorization(n)
    print(f"{n}的质因数分解: {factors}")
    # 验证结果
    result = 1
    for p, exp in factors.items():
        result *= p ** exp
    print(f"验证: {result} = {n}")
    
    print("\n===== 快速幂算法 =====")
    base, exponent, mod = 2, 10, 1000
    print(f"{base}^{exponent} = {fast_power(base, exponent)}")
    print(f"{base}^{exponent} % {mod} = {fast_power(base, exponent, mod)}")
    
    print("\n===== 欧拉函数 =====")
    n = 12
    phi = euler_phi(n)
    print(f"φ({n}) = {phi}")
    # 验证结果：列出所有小于n且与n互质的数
    coprimes = [i for i in range(1, n) if gcd(i, n) == 1]
    print(f"小于{n}且与{n}互质的数: {coprimes}")
    print(f"共有{len(coprimes)}个，与欧拉函数结果一致")
    
    print("\n===== 中国剩余定理 =====")
    a_list = [2, 3, 2]  # 余数列表
    m_list = [3, 5, 7]  # 模数列表
    x = chinese_remainder_theorem(a_list, m_list)
    if x is not None:
        print(f"同余方程组的解: x ≡ {x} (mod {lcm(lcm(m_list[0], m_list[1]), m_list[2])})")
        # 验证结果
        for a, m in zip(a_list, m_list):
            print(f"{x} ≡ {a} (mod {m}) {'✓' if x % m == a else '✗'}")
    
    print("\n===== 蓝桥杯风格例题 =====")
    lanqiao_number_theory_example()
    
    print("\n===== 模线性方程求解 =====")
    a, b, m = 3, 6, 9
    solutions = modular_equation_solver(a, b, m)
    print(f"方程 {a}x ≡ {b} (mod {m}) 的解: {solutions}")
    # 验证结果
    for x in solutions:
        print(f"{a}*{x} mod {m} = {(a*x) % m} {'✓' if (a*x) % m == b % m else '✗'}")


# 让代码可以直接运行
if __name__ == "__main__":
    main()