def climbStairs(n):
    if n <= 2:
        return n
    # Initialize the first two base cases
    a = 1
    b = 2
    
    # Use a loop to calculate the number of ways to reach each step
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
        
    return b

# Example: Get the number of ways to climb n stairs
n = int(input("Enter the number of steps: "))
result = climbStairs(n)
print(f"There are {result} distinct ways to climb {n} steps.")










# If you are at step n, you must have come from either:
# Step n-1 (by taking 1 step), or
# Step n-2 (by taking 2 steps).
# Thus, the number of ways to reach step n is the sum of the number of ways to reach step n-1 and step n-2.

# ways(n) = ways(n-1) + ways(n-2)

# If there is 1 step (n = 1), there is only 1 way to climb (just take 1 step).

# If there are 2 steps (n = 2), there are 2 ways to climb (take two 1-steps or take one 2-step).




# Rules for Balanced Parentheses:
# Every opening parenthesis must have a corresponding closing parenthesis.
# The parentheses must be properly nested. This means that no closing parenthesis can appear before its matching opening parenthesis.
# For example:

# Balanced examples:

# ()
# (())
# (()(()))
# Unbalanced examples:

# ( (no closing parenthesis)
# )( (incorrect order)
# (() (missing one closing parenthesis)\
    
    
