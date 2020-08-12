# Recursive version, memory non-efficient
def binary_search_r(collection, element, low, high):
    mid = high - (high - low) // 2
    if element == collection[mid]:
        return mid
    elif element < collection[mid]:
        return binary_search_r(collection, element, low, mid)
    elif element > collection[mid]:
        return binary_search_r(collection, element, mid, high)
    return -1

# Non recursive version
def binary_search(collection, element):
    low = 0
    high = len(collection) - 1
    while (low < high):
        mid = high - (high - low) // 2
        if element == collection[mid]:
            return mid
        elif element < collection[mid]:
            high = mid
        elif element > collection[mid]:
            low = mid

# Examples
print(binary_search(range(100), 8))