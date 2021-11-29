def binary_search(arr, element):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == element:
            return mid
        if arr[mid] < element:
            start = mid + 1
        else:
            end = mid - 1


for c in range(10):
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], c))
