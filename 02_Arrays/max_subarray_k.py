array = [5,3,8,2]
k = 2

window_sum = sum(array[:k])
max_sum = window_sum

for i in range(k, len(array)):
    window_sum = window_sum - array[i-k] + array[i]
    max_sum = max(max_sum, window_sum)

print("Max sum:", max_sum)