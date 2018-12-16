class Node(object):
    """
        定义单链表节点数据结构：
        data: 存储数据元素的值
        next：存储下一个元素的地址
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        """
            Node 数据域的输出
        """
        print(str(self.data))


class LinkedList():
    """
        创建链表及一系列操作
    """

    def __init__(self):
        """
            初始化空链表，并指定其头节点
        """
        self.head = Node()

    def __str__(self):
        return self.head

    def is_empty(self):
        """
            检查链表是否为空
        """
        return self.head.next is None

    def size(self):
        """
            获取链表大小
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

    def append(self, data):
        """
            尾插法：在链表的尾部添加节点
        """
        if self.is_empty():
            self.head.next = Node(data=data)
            return self.head
        else:
            cursor = self.head
            while cursor.next is not None:
                cursor = cursor.next
            if cursor.next is None:
                cursor.next = Node(data=data)
            return self.head

    def insertToFront(self, data):
        """
            头插法：在链表的头部插入节点
        """
        if self.is_empty():
            self.head.next = Node(data=data)
        else:
            node = Node(data=data)
            node.next = self.head.next
            self.head.next = node
        return self.head

    def insertNodeInPosition(self, data, index):
        """
            在链表某个位置插入数据元素
        """
        count = 0

        if self.is_empty():
            return None
        elif index < 0 or index > self.size() - 1:
            return None
        else:
            cursor = self.head.next
            pre = self.head

            while cursor is not None and count != index:
                pre = cursor
                cursor = cursor.next
                count += 1
            
            node = Node(data=data)
            pre.next = node
            node.next = cursor

            return self.head
            
    def traverse(self):
        """
            遍历链表
        """
        if self.is_empty():
            return None
        else: 
            cursor = self.head.next
            while cursor is not None:
                print('Value：%s' % cursor.data)
                cursor = cursor.next
            return self.head
    
    def getValue(self, index):
        """
            通过索引获取相应的值，找不到的话返回 -1
        """
        count = 0

        if self.is_empty():
            return -1
        elif index < 0 or index > self.size() - 1:
            return -1
        else:
            cursor = self.head.next
            while cursor != None and index != count:
                cursor = cursor.next
                count += 1
            if index == count:
                return cursor.data
            else:
                return -1

    def locationNode(self, data):
        """[查找数据元素在链表中的元素，若找不到则返回 -1；否则返回相应位置]
        
        Arguments:
            data {[int]} -- [查找数据元素]]
        """
        count = 0

        if self.is_empty():
            return -1
        else:
            cursor = self.head.next
            while cursor is not None and cursor.data != data:
                cursor = cursor.next
                count += 1
            if cursor != None and cursor.data == data:
                return count
            else:
                return -1

    def getNodePrior(self, data):
        """[查找指定数据元素的前驱节点，并返回其值；若找不到则返回 -1]
        
        Arguments:
            data {[int]} -- [指定数组元素的值]
        """
        if self.is_empty():
            return -1
        else:
            pre = self.head
            cursor = self.head.next
            while cursor is not None and cursor.data != data:
                pre = cursor
                cursor = cursor.next
            if cursor != None and cursor.data == data:
                if pre == self.head:
                    return -1
                else:
                    return pre.data
            else:
                return -1

    def getNextNode(self, data):
        """[查找指定数据元素的后继节点，并返回后继节点的值；若找不到则返回 -1]
        
        Arguments:
            data {[int]} -- [指定数据元素的值]
        """
        if self.is_empty():
            return -1
        else:
            cursor = self.head.next
            while cursor is not None and cursor.data != data:
                cursor = cursor.next
            if cursor is not None and cursor.data == data and cursor.next is not None:
                return cursor.next.data
            else:
                return -1

    def updateNodeValue(self, i, data):
        """[更新链表某个位置节点的值，查找到值并更新成功返回 0，否则返回 -1]
        
        Arguments:
            i {[int]} -- [更新节点的位置]
            data {[int]} -- [更新节点的值]
        """
        count = 0

        if self.is_empty():
            return -1
        elif i < 0 or i > self.size() - 1:
            return -1
        else:
            cursor = self.head.next
            while cursor is not None and count != i:
                cursor = cursor.next
                count += 1

            if cursor is not None and count == i:
                cursor.data = data
                return 0
            else:
                return -1

    def deleteNode(self, i):
        """[删除链表位置为 i 的节点，查找到并删除成功返回 0；否则返回 -1]
        
        Arguments:
            i {[int]} -- [删除节点位置]
        """

        count = 0

        if self.is_empty():
            return -1
        elif i < 0 or i > self.size() - 1:
            return -1
        else:
            cursor = self.head.next
            pre = self.head
            while cursor is not None and count != i:
                pre = cursor
                cursor = cursor.next
                count += 1

            if cursor is not None and count == i:
                if cursor.next is None:
                    pre.next = None
                    cursor = None
                else:
                    pre.next = cursor.next
                    cursor = None
                return 0
            else:
                return -1

# if __name__ == '__main__':
#     # 创建一个链表对象
#     linked_list = LinkedList()

#     print('链表是否为空：%d' % linked_list.is_empty())

#     print('往链表添加 10 个节点：')

#     for i in range(10):
#         linked_list.append(i)

#     print('链表的长度为：%d' % linked_list.size())

#     print('遍历链表：')
#     linked_list.traverse()

#     print('在链表头部插入数据元素：10')
#     linked_list.insertToFront(10)

#     print('遍历链表：')
#     linked_list.traverse()

#     print('在链表第 4 个位置插入数据元素：11')
#     linked_list.insertNodeInPosition(11, 10)

#     print('遍历链表：')
#     linked_list.traverse()

#     print('获取链表索引为 8 的值：%d' % linked_list.getValue(3))

#     print('查找数据元素 8 位于链表中的位置：%d' % linked_list.locationNode(80))

#     print('查找数据元素 8 的前驱节点的值：%d' % linked_list.getNodePrior(9))

#     print('查找数据元素 8 的后继节点的值：%d' % linked_list.getNextNode(9))

#     print('更新数据元素位置为 8 节点的值为 20：%d' % linked_list.updateNodeValue(8, 20))

#     print('遍历链表：')
#     linked_list.traverse()

#     print('删除数据元素索引为 8 节点：%d' % linked_list.deleteNode(11))
    
#     print('遍历链表：')
#     linked_list.traverse()
