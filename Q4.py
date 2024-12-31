def find_min_platforms(arr, dep):
    # Convert time strings to minutes for easier comparison
    arr = [int(time.split(':')[0]) * 60 + int(time.split(':')[1]) for time in arr]
    dep = [int(time.split(':')[0]) * 60 + int(time.split(':')[1]) for time in dep]

    # Sort the arrival and departure times
    arr.sort()
    dep.sort()

    n = len(arr)
    i, j = 0, 0  
    platforms = 0  
    max_platforms = 0  
    while i < n and j < n:
        if arr[i] <= dep[j]:  
            platforms += 1
            i += 1
            max_platforms = max(max_platforms, platforms)
        else:  
            platforms -= 1
            j += 1

    return max_platforms

arr1 = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
dep1 = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

arr2 = ["9:00", "9:40"]
dep2 = ["9:10", "12:00"]

print(find_min_platforms(arr1, dep1))  
print(find_min_platforms(arr2, dep2))  