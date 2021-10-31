import random

def binarySearch(arr, x):
    l = 0
    r = len(arr) - 1
    global counters
    counters = 0
    while l <= r:
        counters += 1
        mid = l + (r - l) // 2;
        if arr[mid] == x:
            #counters += 1
            return mid
        elif arr[mid] < x:
            #counters += 1
            l = mid + 1
        else:
            #counters += 1
            r = mid - 1
    return -1



#Random Driver Code
def RandomSortedList(num):
    numbers = random.sample(range(1,200),num)
    numbers.sort()
    
    return numbers


# Driver Code
# arr = [1,2,3,4,5,6,7]
# target = 4




arr = RandomSortedList(100)
target = random.randint(1,200)

result = binarySearch(arr, target)

if result != -1:
    print("The sorted array:", arr)
    print("The target value:", target)
    print ("The target index :", result)
    print("The counters:",counters)
else:
    print ("The target index is -1")
    print("The counters",counters)