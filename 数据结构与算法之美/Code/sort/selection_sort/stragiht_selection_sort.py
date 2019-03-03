#ecoding: utf-8
import datetime 
import random

def straight_selection_sort(array, n):
    if n <= 1:
        return array

    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if array[min] > array[j]:
                min = j

        if min != i:
            temp = array[i]
            array[i] = array[min]
            array[min] = temp

    return array


if __name__ == '__main__':
    # array = [2, 1, 8, 7, 21, 25, 18, 17, 32, 11]
    # print(straight_selection_sort(array, len(array)))

    start = datetime.datetime.now()
    array = []

    for i in range(10000):
        array.append(random.randint(1, 10000))
        # array.append(100000 - i)
    print(start)    
    print(array)
    print(straight_selection_sort(array, len(array)))
    end = datetime.datetime.now()
    print(end)
    print('执行时间：%s' % (end - start).seconds)
