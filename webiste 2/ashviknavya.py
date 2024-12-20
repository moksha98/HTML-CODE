#Reverse array
 
arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)


#left rotate
def left_rotate(arr, d):
    # Rotate the array by slicing
    return arr[d:] + arr[:d]

# Example usage
arr = [2, 3, 4, 5]
d = 2
rotated_arr = left_rotate(arr, d)
print(rotated_arr)


#right rotate
def right_rotate(arr, d):
    # Rotate the array by slicing
    return arr[-d:] + arr[:-d]

# Example usage
arr = [2, 3, 4, 5]
d = 2
rotated_arr = right_rotate(arr, d)
print(rotated_arr)



