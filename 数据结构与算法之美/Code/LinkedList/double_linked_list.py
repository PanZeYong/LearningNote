"""
    双向链表增删改查操作
"""

class Node(object):
    """
        双向链表节点的数据结构
    
        参数:
            data: 结点数据；
            prior：上一个结点的内存地址；
            next：下一个结点的内存地址。
    """
    def __init__(self, data=None, prior=None, next=None):
        self.data = data
        self.prior = prior
        self.next = next

"""
    创建双向链表及增删改查操作
"""

class DoubleLinkedList():
    """
        初始化空链表，并指定其头结点
    """
    def __init__(self):
        self.head = Node()
        self.length = 0

    def is_empty(self):
        """
            检查是否为空表
        """
        return self.head.next is None

    def size(self):
        """
            获取链表的长度
        """
        count = 0

        if self.is_empty():
            return count
        else:
            cursor = self.head.next
            while cursor is not None:
                count += 1
                cursor = cursor.next
            return count

    def travel(self):
        """
            遍历双向链表
        """
        cursor = self.head.next
        while cursor is not None:
            print('Value is: %d' % cursor.data)
            cursor = cursor.next

    def add(self, data):
        """
            在链表头部添加元素
        """
        node = Node(data)
        if self.is_empty():
            self.head.next = node
            node.prior = self.head
        else:
            node.prior = self.head
            node.next = self.head.next
            self.head.next.prior = node
            self.head.next = node

    def append(self, data):
        """
            在链表尾部添加元素
        """
        if self.is_empty():
            self.add(data)
        else:
            node = Node(data)
            cursor = self.head.next
            while cursor is not None and cursor.next is not None:
                cursor = cursor.next
            if cursor is not None and cursor.next is None:
                cursor.next = node
                node.prior = cursor

    def insert(self, data, i):
        """
            在双向链表某个位置插入元素
        """
        count = 0

        if i > self.size() - 1:
            self.append(data)
        elif i < 0:
            self.add(data)
        else:
            cursor = self.head.next
            while cursor is not None and count != i:
                cursor = cursor.next
                count += 1
            if cursor is not None and count == i:
                node = Node(data)
                node.prior = cursor.prior
                node.next = cursor
                cursor.prior.next = node
                cursor.prior = node

    def search(self, data):
        """
            查找元素是否存在于链表，存在的话返回元素索引，否则返回 -1
        """
        count = 0

        if self.is_empty():
            return -1
        else:
            cursor = self.head.next
            while cursor is not None and cursor.data != data:
                cursor = cursor.next
                count += 1
            if cursor is not None and cursor.data == data:
                return count
            else:
                return -1

    def getValue(self, index):
        """
            通过索引查找元素，存在的话返回相应的元素；否则返回 -1
        """
        count = 0

        if self.is_empty():
            return -1
        elif index > self.size() - 1 or index < 0:
            return -1
        else:
            cursor = self.head.next
            while cursor is not None and count != index:
                cursor = cursor.next
                count += 1
            if cursor is not None and count == index:
                return cursor.data
            else:
                return -1

    def updateValue(self, index, data):
        """
            通过索引更新值
        """
        count = 0

        if self.is_empty():
            return -1
        elif index > self.size() -1 or index < 0:
            return -1
        else:
            cursor = self.head.next
            while cursor is not None and count != index:
                cursor = cursor.next
                count += 1
            if cursor is not None and count == index:
                cursor.data = data
                return 1
            else:
                return -1

    def deletebyIndex(self, index):
        """
            通过索引删除元素，成功返回 1，否则返回 -1
        """
        count = 0

        if self.is_empty():
            return -1
        elif index > self.size() - 1 or index < 0:
            return -1
        else:
            cursor = self.head.next
            while cursor is not None and count != index:
                cursor = cursor.next
                count += 1
            if cursor is not None and count == index:
                if cursor.next is not None:
                    cursor.prior.next = cursor.next
                    cursor.next.prior = cursor.prior
                    cursor = None
                else:
                    cursor.prior.next = None
                    cursor = None
                return 1
            else:
                return -1

if __name__ == '__main__':
    double_linked_list = DoubleLinkedList()

    print('检查双链表是否为空表：%d' % double_linked_list.is_empty())

    print('双链表的长度为：%d' % double_linked_list.size())

    print('往双向链表头部添加元素：')
    for i in range(10):
        double_linked_list.add(i)

    print('往双向链表尾部添加元素：')
    double_linked_list.append(10)

    print('往双向链表位置 %d 插入元素' % 15)
    double_linked_list.insert(15, 15)

    print('遍历双向链表：')
    double_linked_list.travel()

    print('查找元素 %d 在链表中的位置：%d' % (5, double_linked_list.search(5)))

    print('查找索引为 %d 元素：%d' % (14, double_linked_list.getValue(14)))

    print('更新索引为 %d，值为 %d 的元素的新值为 %d：', (6, 3, double_linked_list.updateValue(6, 12)))

    print('遍历双向链表：')
    double_linked_list.travel()

    print('删除索引为 %d 的元素：%d' % (11, double_linked_list.deletebyIndex(11)))

    print('遍历双向链表：')
    double_linked_list.travel()



