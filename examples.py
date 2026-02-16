# O(1) Example
def get_first_element(arr):
    return arr[0]  # Time: O(1), Space: O(1)


# O(n) Example
def print_all_elements(arr):
    for num in arr:
        print(num)  # Time: O(n), Space: O(1)


# O(n^2) Example
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # Time: O(n^2), Space: O(1)


# O(log n) Example
def divide_by_two(n):
    while n > 1:
        n = n // 2
    # Time: O(log n), Space: O(1)
