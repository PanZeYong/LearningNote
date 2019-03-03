#ecoding: utf-8
import datetime 
import random

def bubble_sort(array, n):

    for i in range(n):
        is_swap = False
        for j in range(n - i - 1):
            if (array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                is_swap = True

        if is_swap == False:
            break

    return array   

if __name__ == '__main__':
    start = datetime.datetime.now()
    array = []

    for i in range(10000):
        array.append(random.randint(1, 10000))
        # array.append(100000 - i)
    print(start)    
    print(array)
    print(bubble_sort(array, len(array)))
    end = datetime.datetime.now()
    print(end)
    print('执行时间：%s' % (end - start).seconds)