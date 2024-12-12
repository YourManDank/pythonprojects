# List comprehension allows us to create a new list using items that exist in a previous list
squares = [value **2 for value in range(1,11)]
print(squares)

# In this example we create our expression that multiplies the given range (1,11) by the second power (**2); generating the square numbers of each value in the range