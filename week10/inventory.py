
# ISM2411 - Module 10: Lists and Tuples
# Name: Aliyah Fisher

# REFLECTION
# Question 1:
# What surprised me most about Python lists is how easily I can change 
# items remove items or organize items without having to rewrite the list. 
# I also didn’t expect indexing to make finding items from the end of a 
# list so simple. It just works.

# Question 2:
# When I ran my hair braiding business I could have used Python lists
#  to sort my clients, services and prices. Of updating everything by 
# hand in Excel I could have used Python lists to calculate totals and 
# keep track of appointments.


# Exercise 1: Build the List
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print("Exercise 1:")
print(inventory)
print(len(inventory))


# Exercise 2: Index Practice
print("\nExercise 2:")
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# Exercise 3: Slicing
print("\nExercise 3:")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4: Modify
print("\nExercise 4:")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5: Tuple Comparison
print("\nExercise 5:")

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed after creation.")
    print("This makes them useful for coordinates because")
    print("the original location stays protected.")

print(coords)


# Exercise 6: Average of a List of Sales
print("\nExercise 6:")

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7: Accumulator Pattern
print("\nExercise 7:")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original:", prices)
print("Discounted:", discounted)


# Exercise 8: Filter Above Threshold
print("\nExercise 8:")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

high_count = len(high_sales)
high_average = sum(high_sales) / high_count

print("High Sales:", high_sales)
print("Count:", high_count)
print("Average:", round(high_average, 2))
