listota = [5, 6, 7, 8, 9, 10, 1, 2, 3]
def count_rotations(arr):
    left, right = 0, len(arr) - 1
    if arr[left] < arr[right]:
        return 0
    while left <= right:
        mid = (left + right) // 2
        if mid > 0 and arr[mid] < arr[mid - 1]:
            return mid
        if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
            return mid + 1
        if arr[mid] >= arr[left]:
            left = mid + 1
        else:
            right = mid - 1
    return 0
print(count_rotations(listota))