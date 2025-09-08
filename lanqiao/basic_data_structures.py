# -*- coding: utf-8 -*-
"""
基础数据结构实例代码
包含栈、队列、链表
适用场景：各种需要特定数据存取方式的算法问题
难度：2-5级（根据具体数据结构和问题复杂度而定）
"""


class Stack:
    """
    栈的实现（后进先出，LIFO）
    原理：只能在一端（栈顶）进行插入和删除操作
    时间复杂度：基本操作均为O(1)
    """
    def __init__(self):
        self.items = []  # 使用列表实现栈
    
    def push(self, item):
        """入栈操作"""
        self.items.append(item)
    
    def pop(self):
        """出栈操作，如果栈为空则抛出异常"""
        if self.is_empty():
            raise IndexError("栈为空，无法出栈")
        return self.items.pop()
    
    def peek(self):
        """查看栈顶元素，如果栈为空则抛出异常"""
        if self.is_empty():
            raise IndexError("栈为空，无法查看栈顶元素")
        return self.items[-1]
    
    def is_empty(self):
        """判断栈是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """返回栈中元素的数量"""
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


class Queue:
    """
    队列的实现（先进先出，FIFO）
    原理：只能在一端（队尾）插入，在另一端（队头）删除
    时间复杂度：基本操作均为O(1)
    """
    def __init__(self):
        self.items = []  # 使用列表实现队列
    
    def enqueue(self, item):
        """入队操作"""
        self.items.append(item)
    
    def dequeue(self):
        """出队操作，如果队列为空则抛出异常"""
        if self.is_empty():
            raise IndexError("队列为空，无法出队")
        return self.items.pop(0)
    
    def front(self):
        """查看队首元素，如果队列为空则抛出异常"""
        if self.is_empty():
            raise IndexError("队列为空，无法查看队首元素")
        return self.items[0]
    
    def is_empty(self):
        """判断队列是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """返回队列中元素的数量"""
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


class Node:
    """\链表节点的实现"""
    def __init__(self, data):
        self.data = data  # 节点数据
        self.next = None  # 指向下一个节点的引用


class LinkedList:
    """
    单链表的实现
    原理：通过节点之间的引用连接形成的链式结构
    时间复杂度：
        - 表头操作：O(1)
        - 表尾操作：O(n)
        - 中间插入/删除：O(n)
    """
    def __init__(self):
        self.head = None  # 链表头节点
    
    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None
    
    def add_at_head(self, data):
        """在链表头部添加节点"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def add_at_tail(self, data):
        """在链表尾部添加节点"""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def remove_at_head(self):
        """删除链表头部节点，如果链表为空则抛出异常"""
        if self.is_empty():
            raise IndexError("链表为空，无法删除节点")
        
        self.head = self.head.next
    
    def remove_by_value(self, data):
        """删除链表中值为data的第一个节点，如果不存在则返回False"""
        if self.is_empty():
            return False
        
        # 如果头节点就是要删除的节点
        if self.head.data == data:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            return True
        
        return False
    
    def search(self, data):
        """查找链表中是否存在值为data的节点，存在返回True，否则返回False"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def __str__(self):
        """返回链表的字符串表示"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "空链表"


# 栈的应用示例
def stack_application():
    """
    栈的应用：括号匹配问题
    题目：检查一个字符串中的括号是否匹配
    """
    def is_valid_parentheses(s):
        stack = Stack()
        # 括号对应关系
        pairs = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in "([{":
                # 左括号入栈
                stack.push(char)
            elif char in ")]}":
                # 右括号，检查栈顶元素是否匹配
                if stack.is_empty() or stack.peek() != pairs[char]:
                    return False
                stack.pop()
        
        # 栈为空说明所有括号都匹配
        return stack.is_empty()
    
    # 测试用例
    test_cases = ["()", "()[]{", "([)]", "{[]}", "{{{{}}}"]
    
    print("栈的应用：括号匹配问题")
    for test in test_cases:
        result = is_valid_parentheses(test)
        print(f"字符串 '{test}' 的括号是否匹配: {result}")


# 队列的应用示例
def queue_application():
    """
    队列的应用：模拟打印机队列
    题目：模拟打印机处理打印任务的过程
    """
    def simulate_printer(print_jobs, print_speed):
        """
        模拟打印机队列
        print_jobs: 打印任务列表，每个元素是(任务名, 页数)
        print_speed: 打印速度，每页需要的时间
        """
        queue = Queue()
        # 将所有打印任务入队
        for job in print_jobs:
            queue.enqueue(job)
        
        current_time = 0
        print("模拟打印机队列处理过程:")
        
        # 处理队列中的所有任务
        while not queue.is_empty():
            job_name, pages = queue.dequeue()
            processing_time = pages * print_speed
            current_time += processing_time
            print(f"时间 {current_time}: 完成打印任务 '{job_name}'，共{pages}页，耗时{processing_time}")
    
    # 测试用例
    jobs = [("文档1", 5), ("文档2", 3), ("文档3", 8), ("文档4", 2)]
    speed = 2  # 每页需要2个时间单位
    
    print("队列的应用：模拟打印机队列")
    simulate_printer(jobs, speed)


# 链表的应用示例
def linked_list_application():
    """
    链表的应用：合并两个有序链表
    题目：将两个有序链表合并成一个新的有序链表
    """
    def merge_sorted_lists(l1, l2):
        """
        合并两个有序链表
        l1, l2: 两个有序链表的头节点
        返回：合并后的有序链表的头节点
        """
        # 创建一个哑节点作为新链表的头部
        dummy = Node(0)
        tail = dummy
        
        # 同时遍历两个链表，比较节点值的大小，将较小的节点添加到新链表中
        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # 处理剩余的节点
        tail.next = l1 if l1 else l2
        
        # 返回新链表的头节点（跳过哑节点）
        return dummy.next
    
    # 创建两个有序链表用于测试
    l1 = LinkedList()
    for val in [1, 3, 5, 7, 9]:
        l1.add_at_tail(val)
    
    l2 = LinkedList()
    for val in [2, 4, 6, 8, 10]:
        l2.add_at_tail(val)
    
    print("链表的应用：合并两个有序链表")
    print(f"链表1: {l1}")
    print(f"链表2: {l2}")
    
    # 合并两个链表
    merged_head = merge_sorted_lists(l1.head, l2.head)
    
    # 构建合并后的链表用于打印
    merged_list = LinkedList()
    merged_list.head = merged_head
    print(f"合并后的链表: {merged_list}")


# 蓝桥杯风格例题
def lanqiao_data_structure_example():
    """
    蓝桥杯风格例题：栈的应用 - 表达式求值
    题目：计算包含加减乘除的表达式的值
    例如：表达式 "3+5*2-8/4" 的值为 3+10-2=11
    """
    def evaluate_expression(expression):
        # 定义运算符优先级
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        
        # 初始化两个栈：一个存储数字，一个存储运算符
        nums = Stack()  # 数字栈
        ops = Stack()   # 运算符栈
        
        i = 0
        while i < len(expression):
            # 跳过空格
            if expression[i].isspace():
                i += 1
                continue
            
            # 处理数字
            if expression[i].isdigit():
                num = 0
                while i < len(expression) and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                nums.push(num)
                continue
            
            # 处理运算符
            if expression[i] in precedence:
                # 当当前运算符的优先级小于等于栈顶运算符的优先级时，计算栈顶的运算
                while not ops.is_empty() and precedence.get(ops.peek(), 0) >= precedence[expression[i]]:
                    calculate(nums, ops)
                ops.push(expression[i])
                i += 1
        
        # 处理剩余的运算
        while not ops.is_empty():
            calculate(nums, ops)
        
        # 最终结果在数字栈的栈顶
        return nums.pop() if not nums.is_empty() else 0
    
    def calculate(nums, ops):
        # 从数字栈中弹出两个数字，从运算符栈中弹出一个运算符，进行计算
        if ops.is_empty() or nums.size() < 2:
            return
        
        op = ops.pop()
        b = nums.pop()  # 第二个操作数
        a = nums.pop()  # 第一个操作数
        
        if op == '+':
            nums.push(a + b)
        elif op == '-':
            nums.push(a - b)
        elif op == '*':
            nums.push(a * b)
        elif op == '/':
            # 注意：这里使用整数除法
            nums.push(a // b if a % b == 0 else a / b)
    
    # 测试用例
    expressions = ["3+5*2-8/4", "10-2*3", "2*3+4*5", "100/25*4"]
    
    print("蓝桥杯风格例题：栈的应用 - 表达式求值")
    for expr in expressions:
        result = evaluate_expression(expr)
        print(f"表达式 '{expr}' 的值为: {result}")


def main():
    print("===== 栈的实现和基本操作 =====")
    stack = Stack()
    print(f"栈是否为空: {stack.is_empty()}")
    print("入栈操作: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"栈的大小: {stack.size()}")
    print(f"栈顶元素: {stack.peek()}")
    print(f"出栈操作: {stack.pop()}")
    print(f"出栈后栈的大小: {stack.size()}")
    print(f"栈的当前状态: {stack}")
    
    print("\n===== 队列的实现和基本操作 =====")
    queue = Queue()
    print(f"队列是否为空: {queue.is_empty()}")
    print("入队操作: 1, 2, 3")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"队列的大小: {queue.size()}")
    print(f"队首元素: {queue.front()}")
    print(f"出队操作: {queue.dequeue()}")
    print(f"出队后队列的大小: {queue.size()}")
    print(f"队列的当前状态: {queue}")
    
    print("\n===== 链表的实现和基本操作 =====")
    linked_list = LinkedList()
    print(f"链表是否为空: {linked_list.is_empty()}")
    print("在尾部添加元素: 1, 2, 3")
    linked_list.add_at_tail(1)
    linked_list.add_at_tail(2)
    linked_list.add_at_tail(3)
    print(f"链表的当前状态: {linked_list}")
    print("在头部添加元素: 0")
    linked_list.add_at_head(0)
    print(f"链表的当前状态: {linked_list}")
    print("删除头部元素")
    linked_list.remove_at_head()
    print(f"链表的当前状态: {linked_list}")
    print("查找元素2是否存在: {linked_list.search(2)}")
    print("删除元素2")
    linked_list.remove_by_value(2)
    print(f"链表的当前状态: {linked_list}")
    
    print("\n===== 栈的应用 =====")
    stack_application()
    
    print("\n===== 队列的应用 =====")
    queue_application()
    
    print("\n===== 链表的应用 =====")
    linked_list_application()
    
    print("\n===== 蓝桥杯风格例题 =====")
    lanqiao_data_structure_example()


# 让代码可以直接运行
if __name__ == "__main__":
    main()