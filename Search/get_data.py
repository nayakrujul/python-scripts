import random, statistics, time

START, END, INCREMENT = 10, 1000, 10

def insertion_sort(lst):
    for x in range(1, len(lst)):
        for y in range(x):
            if lst[x] <= lst[y]:
                z = lst[x]
                lst.pop(x)
                lst.insert(y, z)
                break
    return lst

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def generate_random_list(l):
    lst = []
    for times in range(l):
        lst.append(random.randint(0, 999))
    return lst

for length in range(START, END + 1, INCREMENT):
    
    counts1, counts2 = [], []
    
    for times in range(100):
        
        nums_list = insertion_sort(generate_random_list(length))
        search_for = nums_list[random.randint(0, len(nums_list) - 1)]
        start = time.time()
        binarySearch(nums_list, 0, length - 1, search_for)
        counts1.append((time.time() - start) * 1000)
        
        nums_list = generate_random_list(length)
        search_for = nums_list[random.randint(0, len(nums_list) - 1)]
        start = time.time()
        linearSearch(nums_list, search_for)
        counts2.append((time.time() - start) * 1000)

    f = open('times.csv', 'a')
    f.write(str(length) + ', ' + str(round(statistics.mean(counts1), 3)) + ', ' + str(round(statistics.mean(counts2), 3)) + '\n')
    f.close()