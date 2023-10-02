# https://stackoverflow.com/questions/20455977/sum-up-all-the-integers-in-range
# https://realpython.com/python-sum-function/

# Ask the user for input, using input, which stored as a string.
# int() converts this string to an integer
n = int(input("Enter a number: "))

# we initialize a variable sum_of_numbers to store the sum of the numbers. 
# We start it at 0 because we haven't added any numbers to it yet
sum_of_numbers = 0

# Calculate the sum of numbers from 1 to n
# We use a for loop to iterate through numbers from 1 to n, including n itself
for i in range(1, n + 1):
# he range(1, n + 1) function generates a sequence of numbers starting from 1 and ending at n. 
# if the user entered n as 5, this loop will iterate over the numbers 1, 2, 3, 4, and 5.   
    
    sum_of_numbers += i
# Inside the loop, we add each number to the sum_of_numbers variable.
# += operator is a shorthand way of writing sum_of_numbers = sum_of_numbers + i

# Print the result
print(f"The sum of numbers from 1 to {n} is: {sum_of_numbers}")

