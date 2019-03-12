def findClosestElements(arr, k, x):


    lo, hi = 0, len(arr) - k
    while lo < hi:
        mid = (lo + hi) // 2
        if x - arr[mid] > arr[mid + k] - x:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo:lo + k]

print(findClosestElements([1,2,3,4,5,6], 3, 6))