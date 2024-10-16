def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot_index = partition(arr, low, high)
    
    if pivot_index == k:
        return arr[pivot_index]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

def ith_order_statistic(arr, i):
    return quickselect(arr, 0, len(arr) - 1, i - 1)

# Example usage:
if __name__ == "__main__":
    arr = [10, 4, 5, 8, 6, 11, 26]
    i = 3  # Find the 3rd smallest element
    result = ith_order_statistic(arr, i)
    print(f"The {i}th order statistic is: {result}")
