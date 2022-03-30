# See https://replit.com/@RN09/Sort for the explanations of the sorts

import random, statistics, time


START = 10
END = 1000
INCREMENT = 10


def bubble_sort(lst):
    for x in range(len(lst) - 1):
        for y in range(len(lst) - x - 1):
            if lst[y] > lst[y + 1]:
                lst[y], lst[y + 1] = lst[y + 1], lst[y]
    return lst

def bucket_sort(lst):
    diff = (max(lst) - min(lst)) / 8
    bucket_cutoffs = [
        min(lst) + diff,
        min(lst) + (diff * 2),
        min(lst) + (diff * 3),
        min(lst) + (diff * 4),
        max(lst) - (diff * 3),
        max(lst) - (diff * 2),
        max(lst) - diff
    ]
    buckets = [[] for _ in range(8)]
    for x in lst:
        for y in range(len(bucket_cutoffs)):
            if x <= bucket_cutoffs[y]:
                buckets[y].append(x)
                break
        else:
            buckets[-1].append(x)
    ret = []
    for z in buckets:
        ret += bubble_sort(z)
    return ret

def insertion_sort(lst):
    for x in range(1, len(lst)):
        for y in range(x):
            if lst[x] <= lst[y]:
                z = lst[x]
                lst.pop(x)
                lst.insert(y, z)
                break
    return lst

def quick_sort(lst):
    less = []
    equal = []
    greater = []
    if len(lst) > 1:
        pivot = lst[0]
        for x in lst:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return lst

def radix_sort(lst):
    lst = [str(x) for x in lst]
    digits = max([len(y) for y in lst])
    lst = [z.zfill(digits) for z in lst]
    for a in range(1, digits + 1):
        new_lst = []
        for b in lst:
            for c in range(10):
                if b[-a] == str(c):
                    new_lst.append(b)
        lst = new_lst
    return [int(d) for d in lst]

def selection_sort(lst):
    ret = []
    for x in range(len(lst)):
        y = min(lst)
        ret.append(y)
        lst.remove(y)
    return ret

def comb_sort(lst):
    gap = len(lst)
    swapped = True
    while swapped or gap > 1:
        swapped = False
        if gap > 1:
            gap = (gap * 10) // 13
        else:
            gap = 1
        for x in range(len(lst) - gap):
            if lst[x] > lst[x + gap]:
                lst[x], lst[x + gap]=lst[x + gap], lst[x]
                swapped = True
    return lst

def generate_random_list(l):
    lst = []
    for times in range(l):
        lst.append(random.randint(0, 999))
    return lst


for length in range(START, END + 1, INCREMENT):

    counts = [[] for times in range(7)]
    
    for times in range(100):

        nums_list = generate_random_list(length)
        
        start = time.time()
        bubble_sort(nums_list)
        counts[0].append((time.time() - start) * 1000)

        nums_list = generate_random_list(length)
        
        start = time.time()
        bucket_sort(nums_list)
        counts[1].append((time.time() - start) * 1000)

        nums_list = generate_random_list(length)
        
        start = time.time()
        insertion_sort(nums_list)
        counts[2].append((time.time() - start) * 1000)

        nums_list = generate_random_list(length)
        
        start = time.time()
        quick_sort(nums_list)
        counts[3].append((time.time() - start) * 1000)

        nums_list = generate_random_list(length)
        
        start = time.time()
        radix_sort(nums_list)
        counts[4].append((time.time() - start) * 1000)

        nums_list = generate_random_list(length)
        
        start = time.time()
        selection_sort(nums_list)
        counts[5].append((time.time() - start) * 1000)

        nums_list = generate_random_list(length)
        
        start = time.time()
        comb_sort(nums_list)
        counts[6].append((time.time() - start) * 1000)

    means = [round(statistics.mean(j), 3) for j in counts]
    
    f = open('times.csv', 'a')
    f.write(str(length) + ', ' + ', '.join([str(i) for i in means]) + '\n')
    f.close()
