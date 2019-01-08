class Node(object):
    def __init__(self, data=None, next=None):
        """
            链栈结点的数据结构
        """
        self.data = data
        self.next = next

class LinkedStack():
    def __init__(self):
        # 初始化空表，top 表示栈顶指针
        self.top = Node()

        self.length = 0

    """
        判断链栈是否为空
    """
    def is_empty(self):
        return self.length == 0

    """
        获取链栈的长度
    """
    def size(self):
        return self.length

    """
        入栈
    """
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.length += 1
        return self.top

    """
        出栈
    """
    def pop(self):
        if self.is_empty():
            return '此时链栈为空'
        else:
            next = self.top.next
            data = self.top.data
            self.top = None
            self.top = next
            self.length -= 1
            return data
            

    """
        获取栈顶元素
    """
    def get_top_element(self):
        if self.is_empty():
            return '此时栈为空'
        else:
            return self.top.data

if __name__ == '__main__':
    linked_stack = LinkedStack()

    print('链栈是否为空：%s' % linked_stack.is_empty())

    print('链栈的长度为：%s' % linked_stack.size())

    print('链栈入栈：')
    linked_stack.push(1)

    print("出栈：%s" % linked_stack.pop())

    print('链栈的长度为：%s' % linked_stack.size())




