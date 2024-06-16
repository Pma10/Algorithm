def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less, same, more = [], [], []

    for num in arr:
        if num > pivot:
            more.append(num)
        elif num < pivot:
            less.append(num)
        else:
            same.append(num)

    return quick_sort(less) + same + quick_sort(more)
