# https://stackoverflow.com/questions/20455977/sum-up-all-the-integers-in-range
# https://realpython.com/python-sum-function/

# Ask the user for input, using input, which stored as a string.
n = int(input("Enter a number: "))

# we initialise a variable sum_of_numbers to store the sum of the numbers. 
sum_of_numbers = 0

# Calculate the sum of numbers from 1 to n
# We use a for loop to iterate through numbers from 1 to n, including n itself
for i in range(1, n + 1):   
    
    sum_of_numbers += i
# Inside the loop, we add each number to the sum_of_numbers variable.

# Print the result
print(f"The sum of numbers from 1 to {n} is: {sum_of_numbers}")

