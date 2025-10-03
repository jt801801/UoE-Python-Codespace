# ======================================
# Python Exercises: Lists, Loops & Tuples
# ======================================
# Save this file as exercises2.py
# Topics covered:
# - Lists and Tuples
# - Organizing and modifying lists
# - Looping through data
# - Using range() and comprehensions
# - Basic statistics
# - Slicing
# - Code styling (PEP 8)
# Learning Objectives:
#   * Store and manipulate collections of data.
#   * Automate repetitive tasks with loops.
#   * Follow basic Python style guidelines.

# ======================================
# 1. Defining and Accessing Lists
# --------------------------------------
# Create a list called fruits with at least three fruit names.
# Print the list.
# Print the first and last items using their index.
fruits = ["Apples", "Oranges", "Pear", "Banana"]
print (fruits)
print (fruits[0])
print(fruits[-1])
    

# ======================================
# 2. Modifying Lists
# --------------------------------------
# Change the value of the first fruit in your list.
# Add a new fruit to the end of the list using append().
# Insert a fruit at the beginning using insert().
# Remove one fruit using del, one using pop(), and one using remove().
# Print the updated list.
fruits[0] = "blueberry"
fruits.append("peach")
del fruits [2]
print(fruits)


# ======================================
# 3. Organizing Lists
# --------------------------------------
# Create a list of three or more country names.
# Print the list in alphabetical order using sorted().
# Print the original list to show it is unchanged.
# Sort the list permanently using sort() and print it again.
# Print the list in reverse order using reverse().
# Print the number of countries in the list using len().
countries = ["Eng", "USA", "Russia", "China"]
print(sorted(countries))
print(countries)
countries.sort()
print(countries)
countries.reverse()
print(len(countries))
print(countries)

# ======================================
# 4. Avoiding Index Errors
# --------------------------------------
# Try to print an element at an index that doesn’t exist.
# Wrap your code in a try/except block to handle the error gracefully.
try:
    # This line will fail because there is no index 10
    print(countries[10])
except IndexError:
    # This runs instead of crashing the program
    print("That countires isnt on the list!")

# ======================================
# 5. Looping with for
# --------------------------------------
# Create a list of animals and use a for loop to print each animal’s name.
# Add a message after the loop to thank the user.
animals = ["dog", "cat", "bear", "panda"]
for animal in animals:
    print("I like", animal)
print("Thanks for looking at my animal list!")




# ======================================
# 6. Numerical Lists
# --------------------------------------
# Use range() to generate a list of numbers from 1 to 10.
# Print each number using a for loop.
# Create a list of even numbers between 2 and 20 using range().
# Use min(), max(), and sum() to print statistics about your list.
numbers_1=list(range(1,11))
print(numbers_1)
for number in numbers_1:
    print(number)
evens= list(range(2,21,2))
print(evens)
print("Sum:", sum(evens))
print("Max:", max(evens))
print("Min:", min(evens))


# ======================================
# 7. List Comprehensions
# --------------------------------------
# Use a list comprehension to create a list of squares (1 to 10).
# Print the list.
sqr_number_3 = [x**2 for x in range(1,11)]
print(sqr_number_3)


# ======================================
# 8. Slicing Lists
# --------------------------------------
# Create a list of your favourite foods.
# Print the first three items, middle three items, and last three items using slices.
# Loop through a slice of the list (e.g., first three items) and print each item.
# Make a copy of the list using slicing and modify one of them.
# Exercise 8: Slicing Lists

food = ["choco", "biscuits", "apples", "water", "peaches", "plums"]

# Show slices
print(food[0:3])     # first three
print(food[2:5])     # middle three
print(food[-3:])     # last three

# Loop through a slice
print("First 3 foods:")
for item in food[:3]:     # use 'item' so we don't overwrite 'food'
    print(item)

# Make a copy of the list
fav_food = food[:]        # copy using slicing
fav_food.append("cake")   # modify the copy

# Show the difference
print("Original list:", food)
print("Modified copy:", fav_food)



# ======================================
# 9. Tuples
# --------------------------------------
# Create a tuple called dimensions with two values (width, height).
# Print each value using a loop.
# Try changing one of the values (should cause an error) and note what happens.
# Reassign the tuple to a new pair of values and print it again.
dimensions = (200, 50)

# Print slices
print(dimensions[0:])   # prints (200, 50)
print(dimensions[:1])   # prints (200,)

# Try to change one value (will cause TypeError)
try:
    dimensions[0] = 70   # tuples cannot be modified!
except TypeError:
    print("You can't change a tuple directly!")

# Reassign the whole tuple (this works fine)
dimensions = (250, 100)
print("These are the new dimensions:", dimensions)




# ======================================
# 10. Code Styling (PEP 8)
# --------------------------------------
# Review your code and ensure:
# - Indentation is 4 spaces
# - Lines are under 79 characters
# - Use blank lines to separate logical sections
# This exercise is for self-review.


# ======================================
# Final Challenge
# --------------------------------------
# Create a program that:
#   1. Creates a list of favourite movies.
#   2. Prints them sorted alphabetically.
#   3. Loops through and prints each movie with a custom message.
#   4. Creates a tuple of movie ratings (1–5) and prints the average rating.
#   5. Ensures your program follows PEP 8 guidelines.
