"""
    基于数组实现循环队列
"""

class CircularQueue():
    """
        初始化操作

        capacity 设置列表容量
    """

    def __init__(self, capacity):
        self.items = [None] * capacity
        self.head = 0
        self.tail = 0
        self.capacity = capacity


    """
        判断队列是否为空
    """

    def is_empty(self):
        return self.head == self.tail

    """
        获取列表长度
    """

    def size(self):
        return len(self.items)

    """
        往队列添加元素，通过占用一个空间来表示队列已满
    """

    def enqueue(self, element):
        if (self.tail + 1) % self.capacity == self.head:
            print('队列已满')
            return False 
        
        self.items[self.tail] = element
        self.tail = (self.tail + 1) % self.capacity
        return True


    def dequeue(self):
        if self.is_empty():
            return None

        element = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.capacity
        return element

    def traverse(self):
        for i in range(self.size()):
            print('Value: %s ' % self.items[i])

"""
    通过 is_empty 标志位判断队列是否为空，true 表示空；false 表示不为空
"""

class CircularQueueByFlag():
    """
        初始化操作

        capacity 设置列表容量
    """

    def __init__(self, capacity):
        self.items = [None] * capacity
        self.head = 0
        self.tail = 0
        self.capacity = capacity
        self.empty = True


    """
        判断队列是否为空
    """

    def is_empty(self):
        return self.empty

    """
        获取列表长度
    """

    def size(self):
        return len(self.items)

    def enqueue(self, element):
        if not self.empty and self.head == self.tail:
            print('队列已满')
            return False 
        
        self.items[self.tail] = element
        self.tail = (self.tail + 1) % self.capacity
        self.empty = False
        return True


    def dequeue(self):
        if self.is_empty():
            print('队列为空')
            return None

        element = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.capacity

        if self.head == self.tail:
            self.empty = True

        return element

    def traverse(self):
        for i in range(self.size()):
            print('Value: %s ' % self.items[i])

"""
    通过计数器 count 来判断队列是否为空
"""

class CircularQueueByCount():
    """
        初始化操作

        capacity 设置列表容量
    """

    def __init__(self, capacity):
        self.items = [None] * capacity
        self.head = 0
        self.tail = 0
        self.capacity = capacity
        self.count = 0


    """
        判断队列是否为空
    """

    def is_empty(self):
        return self.count == 0

    """
        获取列表长度
    """

    def size(self):
        return len(self.items)

    def enqueue(self, element):
        if self.count == self.capacity:
            print('队列已满')
            return False 
        
        self.items[self.tail] = element
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1
        return True


    def dequeue(self):
        if self.is_empty():
            print('队列为空')
            return None

        element = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.capacity

        self.count -= 1

        return element

    def traverse(self):
        for i in range(self.size()):
            print('Value: %s ' % self.items[i])

if __name__ == '__main__':
    # circular_queue = CircularQueue(12)

    # CircularQueueByFlag 测试
    # circular_queue = CircularQueueByFlag(12)

    # print('队列是否为空：%s' % circular_queue.is_empty())
    # print('队列长度：%s' % circular_queue.size())

    # # 元素入队
    # elements = [2, 4, 5, 8, 12, 14, 21, 25, 31, 54]
    # for element in elements:
    #     print('往队列添加元素：%s' % circular_queue.enqueue(element))

    # # 遍历元素
    # circular_queue.traverse()

    # # 元素出队
    # for i in range(11):
    #     print('队列返回的元素: %s' % circular_queue.dequeue())

    # print('队列是否为空：%s' % circular_queue.is_empty())

    # print('Head: %s' % circular_queue.head)
    # print('Tail: %s' % circular_queue.tail)

    # # 遍历元素
    # circular_queue.traverse()

    # # 元素入队
    # print('往队列添加元素：%s' % circular_queue.enqueue(25))
    # print('往队列添加元素：%s' % circular_queue.enqueue(26))
    # print('往队列添加元素：%s' % circular_queue.enqueue(27))
    # print('往队列添加元素：%s' % circular_queue.enqueue(28))
    # print('往队列添加元素：%s' % circular_queue.enqueue(29))
    # print('往队列添加元素：%s' % circular_queue.enqueue(30))
    # print('往队列添加元素：%s' % circular_queue.enqueue(31))
    # print('往队列添加元素：%s' % circular_queue.enqueue(32))

    # # 遍历元素
    # circular_queue.traverse()

    # CiccularQueueByCount 测试
    circular_queue = CircularQueueByCount(12)

    print('队列是否为空：%s' % circular_queue.is_empty())
    print('队列长度：%s' % circular_queue.size())

    # 元素入队
    elements = [2, 4, 5, 8, 12, 14, 21, 25, 31, 54, 55, 67, 98]
    for element in elements:
        print('往队列添加元素：%s' % circular_queue.enqueue(element))

    # 遍历元素
    circular_queue.traverse()

    # 元素出队
    for i in range(13):
        print('队列返回的元素: %s' % circular_queue.dequeue())

    print('队列是否为空：%s' % circular_queue.is_empty())

    # 遍历元素
    circular_queue.traverse()

    # 元素入队
    print('往队列添加元素：%s' % circular_queue.enqueue(25))
    print('往队列添加元素：%s' % circular_queue.enqueue(26))
    print('往队列添加元素：%s' % circular_queue.enqueue(27))
    print('往队列添加元素：%s' % circular_queue.enqueue(28))
    print('往队列添加元素：%s' % circular_queue.enqueue(29))
    print('往队列添加元素：%s' % circular_queue.enqueue(30))
    print('往队列添加元素：%s' % circular_queue.enqueue(31))
    print('往队列添加元素：%s' % circular_queue.enqueue(32))

    # 遍历元素
    circular_queue.traverse()
