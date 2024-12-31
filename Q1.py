def square_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    result = [0] * n 
    pos = n - 1 

    while left <= right:
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        
        pos -= 1

    return result

input_array = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
output_array = square_sort(input_array)
print(output_array)