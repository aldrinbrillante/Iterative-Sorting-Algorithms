

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order"""
    return all(items[i] <= items[i+1] for i in range(len(items)-1))


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order"""
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items


def selection_sort(items):
    """Sort given items by finding minimum item and swapping it with first unsorted item"""
    for i in range(len(items)):
        min_index = i
        for j in range(i+1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item and inserting it in sorted order in front of items"""
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    return items
