from single_linked_list import LinkedList

def is_palindrome(self, linked_list):
    """
        回文串：一个正读和反读都一样的字符串，比如 “level” 或 “noon”

        快慢指针：这里的快慢指的是移动的步长，即每次向前移动的快慢。
        设置了两个指针，即慢指针和快指针，慢指针每次向前移动一步，快指针向前移动两步。

        快慢指针的应用：检测链表是否有环、单链表中查找中位数

        在单链表中查找中位数：
        1、如果单链表中的结点数是奇数时，那么当快指针无法移动时，慢指针指向的结点是中间结点；
        2、如果单链表中的结点数是偶数时，那么当快指针无法移动时，慢指针指向的结点上中位结点。

        解决步骤：（将链表拆成两部分）
        1、快慢指针找到中间结点；
        2、对 left 或者 right 部分逆序；
        3、前后部分进行比较，判断是否是回文；
        4、对逆序部分进行复原
    """

    if linked_list.is_empty():
        return False

    fast = linked_list.head.next
    slow = linked_list.head.next

    # 快慢指针查找中位数
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next




if __name__ == '__main__':
    # 创建一个链表对象
    linked_list = LinkedList()

    print('链表是否为空：%d' % linked_list.is_empty())

    linked_list.append('l')
    linked_list.append('e')
    linked_list.append('v')
    linked_list.append('e')
    linked_list.append('l')

    print('遍历单链表：')
    linked_list.traverse()
