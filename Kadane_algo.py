def max_subarray_sum(arr):
    if not arr:
        return 0

    current_sum = max_sum = arr[0]

    for num in arr[1:]:
        # Choose larger of current number and sum ending at previous position
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(array)
    print("Maximum Subarray Sum:", result)
