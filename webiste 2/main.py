# # Function to calculate mean
# def calculate_mean(arr):
#     return sum(arr) / len(arr)

# # Function to calculate median
# def calculate_median(arr):
#     arr.sort()  # Sorting the array
#     n = len(arr)
    
#     if n % 2 == 0:
#         # If even, median is the average of the two middle numbers
#         median = (arr[n//2 - 1] + arr[n//2]) / 2
#     else:
#         # If odd, median is the middle number
#         median = arr[n//2]
    
#     return median

# # Example usage
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mean = calculate_mean(arr)
# median = calculate_median(arr)

# print("Mean:", mean)
# print("Median:", median)


arr= [1,2,3,4,5,6,7,8,9,10]

def calculate_mean(arr):
    return sum(arr)/len(arr)

mean =calculate_mean(arr)
print("Mean =" ,mean)

arr2 = [1, 2, 3, 7]
n = len(arr2)
arr2median= (arr[n//2 - 1] + arr[n//2]) / 2

arr3= [1, 9, 4]
n = len(arr3)
arr3median =  arr[n//2]

def calculate_median_even(arr2):
    print("Median of even length of numbers" ,arr2median)
        
def calculate_median_odd(arr2):
    print("Median of odd length of numbers=" ,arr3median)