# -*- coding: utf-8 -*-
"""
模拟算法实例代码
适用场景：需要按照问题描述逐步模拟过程的问题
难度：1-3级（根据具体问题复杂度而定）
"""


def simulation_basic_example():
    """
    简单模拟示例：掷骰子模拟
    模拟掷骰子1000次，统计每个点数出现的次数
    """
    import random
    
    # 初始化计数器
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    total = 1000  # 模拟次数
    
    print(f"模拟掷骰子{total}次...")
    
    # 模拟掷骰子过程
    for _ in range(total):
        # 随机生成1-6之间的整数
        dice = random.randint(1, 6)
        counts[dice] += 1
    
    # 计算每个点数出现的概率
    probabilities = {k: v/total for k, v in counts.items()}
    
    print("模拟结果:")
    for point in range(1, 7):
        print(f"点数{point}: 出现{counts[point]}次, 概率{probabilities[point]:.4f}")
    
    return counts


def simulation_queue_example():
    """
    队列模拟示例：银行排队问题
    模拟银行窗口的排队情况，计算平均等待时间
    """
    import random
    from collections import deque
    
    # 模拟参数
    total_time = 100  # 模拟总时间
    avg_arrival_time = 5  # 平均到达间隔时间
    avg_service_time = 3  # 平均服务时间
    window_count = 2  # 窗口数量
    
    # 初始化变量
    current_time = 0
    customers = []  # 存储到达的顾客，每个元素是(到达时间, 服务时间)
    wait_queue = deque()  # 等待队列
    window_busy_time = [0] * window_count  # 记录每个窗口的忙碌结束时间
    total_wait_time = 0  # 总等待时间
    customer_count = 0  # 顾客总数
    
    print(f"模拟银行排队情况，总时间{total_time}，窗口数{window_count}，平均到达间隔{avg_arrival_time}，平均服务时间{avg_service_time}")
    
    # 生成顾客到达事件
    arrival_time = 0
    while arrival_time < total_time:
        # 到达间隔时间服从指数分布
        inter_arrival_time = -avg_arrival_time * math.log(random.random()) if random.random() > 0 else avg_arrival_time
        arrival_time += inter_arrival_time
        
        if arrival_time < total_time:
            # 服务时间服从指数分布
            service_time = -avg_service_time * math.log(random.random()) if random.random() > 0 else avg_service_time
            customers.append((arrival_time, service_time))
            customer_count += 1
    
    # 模拟排队和服务过程
    customer_index = 0
    while current_time < total_time or wait_queue or any(t > current_time for t in window_busy_time):
        # 处理到达的顾客
        while customer_index < len(customers) and customers[customer_index][0] <= current_time:
            arrival_time, service_time = customers[customer_index]
            wait_queue.append((arrival_time, service_time))
            customer_index += 1
        
        # 处理空闲窗口
        for i in range(window_count):
            if window_busy_time[i] <= current_time and wait_queue:
                arrival_time, service_time = wait_queue.popleft()
                wait_time = current_time - arrival_time
                total_wait_time += wait_time
                window_busy_time[i] = current_time + service_time
                
                print(f"时间{current_time:.2f}: 顾客到达于{arrival_time:.2f}，等待{wait_time:.2f}，开始服务，预计结束于{window_busy_time[i]:.2f}")
        
        # 前进时间
        next_events = []
        if customer_index < len(customers):
            next_events.append(customers[customer_index][0])
        next_events.extend([t for t in window_busy_time if t > current_time])
        
        if next_events:
            current_time = min(next_events)
        else:
            break
    
    # 计算平均等待时间
    avg_wait_time = total_wait_time / customer_count if customer_count > 0 else 0
    print(f"\n模拟结束，共服务{customer_count}位顾客，平均等待时间{avg_wait_time:.2f}")
    
    return avg_wait_time


def lanqiao_simulation_example():
    """
    蓝桥杯风格例题：报数游戏
    题目：n个人围成一圈，从第1个人开始报数，数到m的人出列，然后从出列的下一个人开始重新报数，
         直到所有人都出列。请按出列顺序输出每个人的编号。
    例如：n=5, m=2，出列顺序为2,4,1,5,3
    """
    n = 5  # 人数
    m = 2  # 报数到m的人出列
    
    # 初始化队列，存储人的编号
    people = list(range(1, n + 1))
    result = []  # 存储出列顺序
    current = 0  # 当前报数的位置
    
    print(f"n={n}, m={m}")
    print(f"初始顺序: {people}")
    
    # 模拟报数过程
    while people:
        # 计算下一个要出列的人的位置
        current = (current + m - 1) % len(people)
        # 移除并记录出列的人
        out_person = people.pop(current)
        result.append(out_person)
        print(f"出列: {out_person}, 剩余: {people}")
    
    print(f"\n出列顺序: {result}")
    
    return result


def grid_simulation():
    """
    网格模拟示例：机器人路径
    模拟机器人在网格中的移动，根据给定的指令序列
    """
    # 指令序列：U(上), D(下), L(左), R(右)
    commands = "URRDLUD"
    # 初始位置
    x, y = 0, 0
    # 存储走过的路径
    path = [(x, y)]
    
    print(f"初始位置: ({x}, {y})")
    print(f"指令序列: {commands}")
    
    # 模拟移动过程
    for cmd in commands:
        if cmd == 'U':
            y += 1
        elif cmd == 'D':
            y -= 1
        elif cmd == 'L':
            x -= 1
        elif cmd == 'R':
            x += 1
        
        path.append((x, y))
        print(f"执行命令'{cmd}'后，位置: ({x}, {y})")
    
    print(f"\n最终位置: ({x}, {y})")
    print(f"完整路径: {path}")
    
    # 计算是否回到起点
    if x == 0 and y == 0:
        print("机器人回到了起点")
    else:
        print("机器人没有回到起点")
    
    return path


def main():
    print("===== 简单模拟示例：掷骰子模拟 =====")
    simulation_basic_example()
    
    print("\n===== 队列模拟示例：银行排队问题 =====")
    # 注意：这个示例需要导入math库
    try:
        import math
        simulation_queue_example()
    except Exception as e:
        print(f"银行排队模拟出错: {e}")
    
    print("\n===== 蓝桥杯风格例题：报数游戏 =====")
    lanqiao_simulation_example()
    
    print("\n===== 网格模拟示例：机器人路径 =====")
    grid_simulation()


# 让代码可以直接运行
if __name__ == "__main__":
    main()