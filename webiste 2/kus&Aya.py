# Head
# In head recursion, the recursive call happens before any operations in the function. 
# This means the function keeps calling itself until it reaches the base case, and 
# only then does it start to perform operations on the way back up the call stack.

# def head_recursion(n):
#     if n == 0:
#         return
#     head_recursion(n - 1)  # Recursive call first
#     print(n)  # Operation happens after the recursive call

# n = int(input("Enter your range"))
# print(head_recursion(n))

# Tail:
# In tail recursion, the recursive call happens after all the operations are performed. The recursive call is the last operation in the function.
# Tail recursion can often be optimized by compilers to avoid increasing the call stack size, leading to more efficient recursion.

# def tail_recursion(n):
#     if n == 0:
#         return
#     print(n)  # Operation happens before the recursive call
#     tail_recursion(n - 1)  # Recursive call as the last operation


# n = int(input("Enter your range"))
# print(tail_recursion(n))\\\
    
    
    
# arr = [4, 2, 9, 1, 5, 6]
# arr.sort()  # This modifies the original list
# print("Ascending:", arr)

# arr = [4, 2, 9, 1, 5, 6]
# arr.sort(reverse=True)  # This modifies the original list
# print("Descending:", arr)
    
    
# arr = [4, 2, 9, 1, 5, 6]
# total_sum = sum(arr)
# print("Sum of array:", total_sum)

# arr = [4, 2, 9, 1, 5, 6]
# largest_element = max(arr)
# print("Largest element in the array:", largest_element)




# arr = [1,2,4,56,76,345,53,432,345,345,436]
# print(len(arr))

# # print(arr[8])

# # arr.append(3)
# # print(arr)

# # arr.sort()
# # print(arr)


# # arr.sort(reverse=True)
# # print(arr)

# def reverse_integer(n):
#     # Check if the number is negative
#     if n > 0:
#         return int(str(n)[::-1])

# # Ask for user input
# number = int(input("Enter an integer: "))

# # Reverse the integer
# reversed_number = reverse_integer(number)

# print("Reversed Integer:", reversed_number)




# #string reverse 
# # Ask for user input
# user_input = input("Enter a string to reverse: ")

# # Reverse the string using slicing
# reversed_string = user_input[::-1]

# # Print the reversed string
# print("Reversed string:", reversed_string)






# Program to Print the number of ways to climb n stairs when you can jump 1,2,3 stair at a time

# def ways(stairs):

#   # check corner case
#   if stairs<0:
#     return 0

#   # if no stair left, just return one as we reach the top
#   if stairs==0:
#     return 1
#   twosteps=0
#   onestep=0

# # we can jump 2 only 2 or more stairs are left
#   if (stairs>=2):
#     twosteps = ways(stairs-2)
# # jump 1 if 1 or more stairs remains 
#   onestep = ways(stairs-1)
# # return total ways 
#   return twosteps+onestep

# stairs = int(input("enter number of steps :"))

# print("number to ways to climb :",ways(stairs))



# Base Case (Stairs < 0):

# If the number of stairs is negative (stairs < 0), it means we have taken too many steps, and that is not a valid path. So, we return 0.
# Base Case (Stairs == 0):

# If there are no stairs left (stairs == 0), it means we have exactly reached the top, which counts as one valid way. So, we return 1.
# Recursive Cases:

# Jump 2 steps: If stairs >= 2, you can jump two steps at once. So, the recursive call ways(stairs - 2) is made to calculate the number of ways to climb the remaining stairs after a 2-step jump.
# Jump 1 step: You can always jump 1 step if there is at least 1 stair. So, the recursive call ways(stairs - 1) is made to calculate the number of ways to climb the remaining stairs after a 1-step jump.
# Combine the results: The total number of ways to climb stairs is the sum of the two possible jumps (1-step and 2-step), so you return twosteps + onestep.

# Example:
  
  
#MEan MEdian

# # Sample array
# arr = [2, 4, 6, 8, 10]

# # Calculate mean
# mean = sum(arr) / len(arr)


# # Calculate median
# sorted_arr = sorted(arr)
# n = len(sorted_arr)
# median = (sorted_arr[n // 2] if n % 2 != 0 
#           else (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2)

# print("Mean:", mean)
# print("Median:", median)



# #MAX & MIN

# # Sample array
# arr = [2, 4, 6, 8, 10]

# # Initialize max and min with the first element
# max_value = arr[0]
# min_value = arr[0]

# # Iterate through the array
# for num in arr:
#     if num > max_value:
#         max_value = num
#     if num < min_value:
#         min_value = num

# print("Maximum value:", max_value)
# print("Minimum value:", min_value)


# #2nd largest element in array!

# # Sample array
# arr = [2, 4, 6, 8, 10]

# # Ensure there are at least two elements
# if len(arr) < 2:
#     print("Array needs at least two elements.")
# else:
#     # Sort the array in descending order
#     sorted_arr = sorted(arr, reverse=True)
    
#     # Find the second largest element
#     second_largest = sorted_arr[1]

#     print("Second largest element:", second_largest)


# #stock but & sell 

# def stock(prices):
#     # Ensure there are prices to process
#     if not prices or len(prices) < 2:
#         return 0

#     total_profit = 0

#     # Loop through the prices array
#     for i in range(1, len(prices)):
#         # Add profit for every price increase
#         if prices[i] > prices[i - 1]:
#             total_profit += prices[i] - prices[i - 1]

#     return total_profit

# # Example usage
# prices = [635,864,247,325,257,745,245]
# profit = stock(prices)

# print(f"The maximum profit from multiple transactions is: {profit}")


#sort array in 0 1 2
def sort_012(arr):
    return sorted(arr)

# Example usage
array = [2, 0, 1, 2, 1, 0, 1, 2, 0]
sorted_array = sort_012(array)
print("Sorted Array:", sorted_array)


#missing array 
def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

# Example usage
array = [1, 2, 4, 5, 6]  # Missing 3
n = 6
print(f"Missing number: {find_missing_number(array, n)}")
