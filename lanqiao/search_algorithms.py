# -*- coding: utf-8 -*-
"""
搜索算法实例代码
包含BFS（广度优先搜索）和DFS（深度优先搜索）
适用场景：图或树的遍历，寻找路径或特定节点
难度：1-5级（根据具体问题复杂度而定）
"""

from collections import deque


def bfs(graph, start):
    """
    广度优先搜索实现
    原理：从起始节点开始，逐层访问所有相邻节点
    时间复杂度：O(V+E)，其中V是节点数，E是边数
    
    参数：
        graph: 图的邻接表表示
        start: 起始节点
    返回：
        按BFS顺序访问的节点列表
    """
    # 用于存储已访问的节点
    visited = set()
    # 用于存储访问顺序
    result = []
    # 使用队列来实现BFS
    queue = deque([start])
    visited.add(start)
    
    while queue:
        # 出队一个节点
        node = queue.popleft()
        result.append(node)
        
        # 将所有未访问的邻接节点入队
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def bfs_shortest_path(graph, start, end):
    """
    使用BFS寻找最短路径
    适用于无权图的最短路径问题
    """
    # 用于存储已访问的节点
    visited = set()
    # 使用队列来实现BFS，队列中的元素是(当前节点, 路径)
    queue = deque([(start, [start])])
    visited.add(start)
    
    while queue:
        node, path = queue.popleft()
        
        # 如果找到目标节点，返回路径
        if node == end:
            return path
        
        # 将所有未访问的邻接节点入队
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # 如果无法到达目标节点
    return None


def dfs(graph, start, visited=None):
    """
    深度优先搜索实现（递归版本）
    原理：从起始节点开始，尽可能深地探索图的分支
    时间复杂度：O(V+E)
    
    参数：
        graph: 图的邻接表表示
        start: 起始节点
        visited: 已访问节点集合（用于递归）
    返回：
        按DFS顺序访问的节点列表
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    # 递归访问所有未访问的邻接节点
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result


def dfs_iterative(graph, start):
    """
    深度优先搜索实现（迭代版本）
    使用栈来模拟递归
    """
    visited = set()
    result = []
    # 使用栈来实现DFS
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            # 将邻接节点入栈（注意顺序，以保持与递归版本相同的访问顺序）
            # 这里反转是为了让邻接节点的处理顺序与递归版本一致
            stack.extend(reversed(graph[node]))
    
    return result


def lanqiao_bfs_example():
    """
    蓝桥杯风格例题：迷宫最短路径
    题目：给定一个m×n的迷宫，0表示空格（可通行），1表示墙壁（不可通行）
    从左上角(0,0)出发，到达右下角(m-1,n-1)的最短路径长度是多少？
    """
    # 示例迷宫：0表示空格，1表示墙壁
    maze = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    m, n = len(maze), len(maze[0])
    # 定义四个方向：上、右、下、左
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # BFS寻找最短路径
    queue = deque([(0, 0, 0)])  # (x, y, distance)
    visited = set([(0, 0)])
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 到达终点
        if x == m-1 and y == n-1:
            print(f"迷宫最短路径长度: {dist}")
            return dist
        
        # 尝试四个方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 检查是否越界，是否是墙壁，是否已访问
            if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    
    # 无法到达终点
    print("无法到达终点")
    return -1


def lanqiao_dfs_example():
    """
    蓝桥杯风格例题：全排列问题
    题目：给定一个不包含重复数字的数组，返回其所有可能的全排列
    例如：数组[1,2,3]的全排列为[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
    """
    nums = [1, 2, 3]
    result = []
    
    def backtrack(path, used):
        # 如果路径长度等于数组长度，说明找到了一个全排列
        if len(path) == len(nums):
            result.append(path[:])  # 深拷贝当前路径
            return
        
        for i in range(len(nums)):
            # 如果当前数字已经使用过，跳过
            if used[i]:
                continue
            
            # 选择当前数字
            path.append(nums[i])
            used[i] = True
            
            # 递归搜索
            backtrack(path, used)
            
            # 回溯：撤销选择
            path.pop()
            used[i] = False
    
    backtrack([], [False] * len(nums))
    
    print(f"数组{nums}的全排列共有{len(result)}种：")
    for perm in result:
        print(perm)
    
    return result


def main():
    # 示例图的邻接表表示
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("===== BFS 示例 =====")
    bfs_result = bfs(graph, 'A')
    print(f"BFS访问顺序: {bfs_result}")
    
    print("\n===== BFS寻找最短路径示例 =====")
    shortest_path = bfs_shortest_path(graph, 'A', 'F')
    print(f"从A到F的最短路径: {shortest_path}")
    
    print("\n===== DFS 递归版本示例 =====")
    dfs_result = dfs(graph, 'A')
    print(f"DFS访问顺序(递归): {dfs_result}")
    
    print("\n===== DFS 迭代版本示例 =====")
    dfs_iter_result = dfs_iterative(graph, 'A')
    print(f"DFS访问顺序(迭代): {dfs_iter_result}")
    
    print("\n===== 蓝桥杯风格例题：迷宫最短路径 =====")
    lanqiao_bfs_example()
    
    print("\n===== 蓝桥杯风格例题：全排列问题 =====")
    lanqiao_dfs_example()


# 让代码可以直接运行
if __name__ == "__main__":
    main()