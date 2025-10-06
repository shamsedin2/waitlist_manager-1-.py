def linear_search(arr, target):
    """
    Finds the index of target in arr using linear search.
    Returns -1 if target not found.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Test cases
print(linear_search([1, 3, 5, 7], 5))  # 2
print(linear_search([1, 3, 5, 7], 2))  # -1
print(linear_search([], 1))            # -1
print(linear_search([10], 10))         # 0

"""
Performance Analysis:
- Best-case time complexity: O(1)  (target found at first index)
- Worst-case time complexity: O(n) (target not found or at last index)
- Average-case time complexity: O(n)
- Space complexity: O(1)  (only a single index variable)
- Approach chosen for simplicity; cannot be optimized beyond O(n) for unsorted arrays.
"""
def binary_search(arr, target):
    """
    Finds the index of target in a sorted arr using binary search.
    Returns -1 if target not found.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test cases
print(binary_search([1, 3, 5, 7], 5))  # 2
print(binary_search([1, 3, 5, 7], 2))  # -1
print(binary_search([], 1))            # -1
print(binary_search([10], 10))         # 0

"""
Performance Analysis:
- Best-case: O(1) (target found at mid initially)
- Worst-case: O(log n)
- Average-case: O(log n)
- Space complexity: O(1) (only left, right, mid variables)
- Optimized for sorted arrays. Trade-off: requires array to be sorted.
"""
def find_max(arr):
    """
    Returns the maximum value in arr.
    """
    if not arr:
        return None  # edge case for empty list
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

# Test cases
print(find_max([1, 3, 5, 7]))   # 7
print(find_max([-1, -3, -5]))   # -1
print(find_max([42]))           # 42
print(find_max([]))             # None

"""
Performance Analysis:
- Best-case, worst-case, average-case: O(n) (must check all elements)
- Space complexity: O(1)
- Simple single-pass solution; cannot improve time complexity.
"""
def sum_of_subsets(arr):
    """
    Returns the sum of all possible subsets of arr.
    """
    total_sum = 0
    n = len(arr)
    num_subsets = 1 << n  # 2^n subsets

    for i in range(num_subsets):
        subset_sum = 0
        for j in range(n):
            if i & (1 << j):
                subset_sum += arr[j]
        total_sum += subset_sum
    return total_sum

# Test cases
print(sum_of_subsets([1, 2]))     # 6  ([1],[2],[1,2],[]) -> 1+2+3+0=6
print(sum_of_subsets([1, 2, 3]))  # 24
print(sum_of_subsets([]))         # 0
print(sum_of_subsets([10]))       # 10

"""
Performance Analysis:
- Best, worst, average-case: O(n * 2^n)
- Space complexity: O(1) (only counters used)
- Approach chosen for clarity; cannot be improved beyond O(n*2^n) because all subsets must be considered.
- Trade-off: exponential time for large arrays.
"""
def bubble_sort(arr):
    """
    Sorts arr in-place using bubble sort.
    """
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break  # Optimization: stop if array already sorted
    return arr

# Test cases
print(bubble_sort([5, 3, 1, 4, 2]))  # [1,2,3,4,5]
print(bubble_sort([1,2,3]))          # [1,2,3] (optimized early exit)
print(bubble_sort([]))               # []
print(bubble_sort([42]))             # [42]

"""
Performance Analysis:
- Best-case: O(n) (already sorted, optimized)
- Worst-case: O(n^2) (reversed array)
- Average-case: O(n^2)
- Space complexity: O(1) (in-place)
- Optimization: early exit if no swaps in a pass.
- Trade-offs: slower than O(n log n) sorts, but simple and stable.
"""
