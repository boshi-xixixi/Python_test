# -*- coding: utf-8 -*-
"""
枚举算法练习题
请完成以下任务，然后运行代码检查结果
"""


def enum_exercise():
    """
    练习题：找出所有满足以下条件的四位数
    1. 四位数的各位数字互不相同
    2. 四位数能被11整除
    3. 四位数的各位数字之和等于20
    例如：符合条件的数有 2857（2+8+5+7=22，不符合；此为示例非答案）
    
    请在下方编写代码，实现上述功能
    提示：可以使用四层循环分别枚举千位、百位、十位和个位数字
    注意：千位数字不能为0
    """
    # 在这里编写你的代码
    # 初始化结果列表
    results = []
    
    # 枚举所有四位数的可能
    for a in range(1, 10):  # 千位，不能为0
        for b in range(0, 10):  # 百位
            for c in range(0, 10):  # 十位
                for d in range(0, 10):  # 个位
                    # 检查条件1：各位数字互不相同
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        # 组成四位数
                        num = a * 1000 + b * 100 + c * 10 + d
                        # 检查条件2：能被11整除
                        if num % 11 == 0:
                            # 检查条件3：各位数字之和等于20
                            if a + b + c + d == 20:
                                results.append(num)
    
    # 输出结果
    print(f"找到{len(results)}个符合条件的四位数：")
    print(results)
    return results


# 主函数：运行练习题
def main():
    print("===== 枚举算法练习题 ======")
    enum_exercise()


# 让代码可以直接运行
if __name__ == "__main__":
    main()