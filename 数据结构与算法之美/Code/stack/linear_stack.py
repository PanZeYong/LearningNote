"""
    线性栈的基本操作
"""

class LinearStack():
    """
        初始化栈
        top：栈顶指针，-1 时表示栈空，再退栈的话会出现下溢
    """
    def __init__(self):
        self.items = []
        self.top = -1    

    """
        判断栈是否为空
    """
    def is_empty(self):
        return self.top == -1

    """
        返回栈的长度
    """
    def size(self):
        return len(self.items)

    """
        入栈，每当添加一个元素时，栈顶指针 top 往上移，加 1
    """
    def push(self, element):
        self.items.append(element)
        self.top += 1

    """
        退栈，如果栈顶指针 top 等于 -1 时，说明此时栈为空，退出程序；
        否则，每当移除一个元素，栈顶指针往下移
    """

    def pop(self):
        if self.is_empty():
            print('此时栈为空')
            return

        x = self.items.pop(self.top)
        self.top -= 1
        return x

    """
        获取栈顶元素
    """

    def getElement(self):
        if self.is_empty():
            print('此时栈为空')
            return

        return self.items[self.top]

    # def traverse(self):
    #     if self.is_empty():
    #         print('此时栈为空')
    #         return

    #     for item in self.items:
    #         print('Value is: %s' % item)

if __name__ == '__main__':
    # 初始化空栈
    linear_stack = LinearStack()

    print('栈是否为空：%s' % linear_stack.is_empty())

    print('入栈：')
    for i in range(10):
        linear_stack.push(i)

    print('栈的长度：%d' % linear_stack.size())

    for i in range(10):
        print('退栈：%s' % linear_stack.pop())

    print('退栈后栈的长度：%d' % linear_stack.size())
    




