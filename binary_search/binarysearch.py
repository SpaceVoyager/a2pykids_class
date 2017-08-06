import random
import time

numbers = []
for i in range(10000):
    numbers.append(random.randint(1,100000))

def linearsearch(num_list,x):
    index = 0
    for num in num_list:
        if num == x:
            return index
        index += 1
    return None

start_time = time.time()
print linearsearch(numbers, 2)
print("---%s seconds ---" % (time.time() - start_time))

numbers = sorted(numbers)

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)/2
        mid_number = alist[midpoint]
        if mid_number == item:
            found = True
        else:
            if item < mid_number:
                last = midpoint-1
            else:
                first = midpoint + 1

    return found


start_time = time.time()
print binarySearch(numbers, 100)
print("---%s seconds ---" % (time.time() - start_time))

def binarySearch2(alist, item):
    if len(alist) == 0:
        return False
    elif len(alist) == 1:
        if alist[0] == item:
            return True
        else:
            return False
    else:
        first = 0
        last = len(alist) - 1
        midpoint = (first + last) / 2
        mid_number = alist[midpoint]

        if mid_number == item:
            return True
        else:
            if item < mid_number:
                return binarySearch2(alist[0:midpoint], item)
            else:
                return binarySearch2(alist[midpoint+1:], item)


start_time = time.time()
print binarySearch2(numbers, 100)
print("---%s seconds ---" % (time.time() - start_time))
