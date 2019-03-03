#ecoding: utf-8
import datetime 
import random

def straight_insertion_sort(array, n):
    if n <= 1:
        return array

    for i in range(1, n):
        key = array[i]
        j = i - 1
        
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array

if __name__ == '__main__':
    start = datetime.datetime.now()
    # array = [23, 21, 4, 2, 45, 17, 8, 28]
    array = []

    # print(straight_insertion_sort(array, len(array)))

    for i in range(10000):
        array.append(random.randint(1, 10000))
        # array.append(100000 - i)
    # print(start)    
    print(array)
    print(straight_insertion_sort(array, len(array)))
    end = datetime.datetime.now()
    # print(end)
    print('执行时间：%s' % (end - start).seconds)