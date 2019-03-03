"""
    基于数组实现，队列的基本操作
"""
import  sys

class Queue():
    def __init__(self, n):
        self.queue = [None] * n
        self.n = n
        self.head = 0
        self.tail = 0

    """
        判断队列是否为空
    """

    def is_empty(self):
        return self.head == self.tail

    """
        获取队列的大小
    """

    def size(self):
        return self.n

    """
        入队

        tail == n 表示队满，入队失败，返回 False
    """

    def enqueue(self, element):
        if self.tail == self.n:
            if self.head == 0:
                return False

            for i in range(self.tail - self.head):
                self.queue[i] = self.queue[self.head]
                self.queue[self.head] = None
                self.head += 1
            
            self.tail = self.head - 1
            self.head = 0

        self.queue[self.tail] = element
        self.tail += 1

        return True

    """
        出队

        head == tail 表示队空，队列空的时候返回 None；否则返回相应的值
    """

    def dequeue(self):
        if self.is_empty():
            return None

        element = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1

        return element

    """
        遍历队列
    """

    def traverse(self):
        for index in range(self.size()):
            print('Vaule: %s ' % self.queue[index])

    # def tailrecsum(self, x, running_total=0):
    #     if x == 0:
    #         return running_total
    #     else:
    #         return self.tailrecsum(x - 1, running_total + x)

if __name__ == '__main__':
    # 初始化队列
    queue = Queue(10)

    # 判断队列是否为空
    print('队列是否为空：%s' % queue.is_empty())

    # 获取队列的长度
    print('获取队列的长度：%s' % queue.size())

    # 元素入队
    elements = [2, 4, 5, 8, 12, 14, 21, 25, 31, 54]
    for i in elements:
        queue.enqueue(i)

    # 遍历队列
    queue.traverse()

    # 出队
    print('获取出队元素：%s ' % queue.dequeue())


    # 遍历队列
    queue.traverse()

    print('添加元素：%s' % queue.enqueue(12))

    # 遍历队列
    queue.traverse()

    # sys.setrecursionlimit(100000)
    # print(queue.tailrecsum(99999))