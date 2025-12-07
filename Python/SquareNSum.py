# Complete the square sum function so that it squares each number 
# passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9.

#Solution 1:
def square_sum(numbers):
    # Initialize a variable to hold the running total
    total_sum = 0
    
    for x in numbers:
        # Square the number
        squared_number = x ** 2
        # Add the squared number to the total sum
        total_sum += squared_number
    return total_sum

# Solution 2:
def square_sum(numbers):
     return sum([x**2 for x in numbers])