
"""
Not to self:
how the sorting.py will work will be as simlar as what follows - 
array  = [5,2,3,4,1]
print(array)
merge_sort(array)
print(array)

run python3 sorting.py (input sort) to check 
"""


def merge(items1, items2):
    """Merge given lists of items each assumed to already be in sorted order and return a new list containing all items in sorted order."""
    items = []
    i1 = 0
    i2 = 0
    while i1 < len(items1) and i2 < len(items2):
        if items1[i1] < items2[i2]:
            items.append(items1[i1])
            i1 += 1
        else:
            items.append(items2[i2])
            i2 += 1
    items += items1[i1:]
    items += items2[i2:]
    return items


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves, sorting each with an iterative sorting algorithm, and merging results into a list in sorted order."""
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    items1 = split_sort_merge(items[:mid])
    items2 = split_sort_merge(items[mid:])
    return merge(items1, items2)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves, sorting each with a recursive sorting algorithm, and merging results into a list in sorted order."""
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    items1 = merge_sort(items[:mid])
    items2 = merge_sort(items[mid:])
    return merge(items1, items2)


def partition(items, low, high):
    """Partition given items in range `[low...high]` by partitioning index `p` after in-place partitioning given items in range `[low...high]` by choosing a pivot from that range, moving pivot into index `p`, items less than pivot into range `[low...p-1]`, and items greater than pivot into range `[p+1...high]`."""
    pivot = items[low]
    i = low + 1
    j = high
    while True:
        while i <= j and items[i] <= pivot:
            i += 1
        while j >= i and items[j] >= pivot:
            j -= 1
        if j < i:
            break
        items[i], items[j] = items[j], items[i]
    items[low], items[j] = items[j], items[low]
    return j


def quick_sort(items, low=None, high=None):  # passed sorting.py test
    """Sort given items in place by partitioning items in range `[low...high]` around a pivot item and recursively sorting each remaining sublist range."""
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1
    if low < high:
        p = partition(items, low, high)
        quick_sort(items, low, p - 1)
        quick_sort(items, p + 1, high)
