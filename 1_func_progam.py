
''' Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple. '''

# grades = [('English', 88), ('Science', 90),
#           ('Maths', 97), ('Social sciences', 82)]

# print(sorted(grades, key=lambda x: x[1]))

''' Write a lambda function to cube every element of a list. '''

# list = [3, 6, 9, 2]

# cubed = lambda x: [num**3 for num in x]

# print(cubed(list))

''''
Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False. '''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_odd = lambda x: [True if num % 2 == 0 else False for num in x]

# print(even_odd(numbers))

''' Use a list comprehension to create a list of the numbers from 1 to 100 (including 100). '''

# nums = [y for y in range(1, 101)]
# print(nums)

''' Use a dictionary comprehension to count the length of each word in a sentence. '''

# sentence = "The quick brown fox jumped over the fence."

# x = {word: len(word) for word in sentence.split()}
# print(x)
