#Chapter4 - Exercise 4.1 - for loop
print("#Chapter4 - Exercise 4.1 - for loop")
teams = ['Arsenal', 'Tottenham', 'Chelsea', 'Manchester United', 
         'Manchester City','Liverpool']
for team in teams:
    print(team)

#Chapter4 - WarmUp - Range + Loop + Netsing
print("\n#Chapter4 - WarmUp - Range + Loop")
for value in range (-2,6):
    print(value)

print("Range to list")
numbers = list(range(1,6))
print(numbers)

print("Range to list - odd numbers")
odd_numbers = list(range(1,10,2))
print(odd_numbers)

print("Square roots of numbers 1-10")
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

print("Min/Max/Sum")
print(f"Minimal value of squares list: {min(squares)}")
print(f"Maximal value of squares list: {max(squares)}")
print(f"Sum of squares list: {sum(squares)}")

print("Nesting")
squares = [value**2 for value in range(1,11)]
print(f"List nesting: {squares}")

#Chapter4 - Exercise 4.3 - count to 20 with for loop
print("#Chapter4 - Exercise 4.3 - count to 20 with for loop")
for value in range(1,21):
    print(value)

#Chapter4 - Exercise 4.4 - printing list of milion 
print("#Chapter4 - Exercise 4.4 - printing list of milion ")
numbers = list(range(1,1000001))
for number in numbers:
    print(number)

#Chapter4 - Exercise 4.5 - min/max/sum of list of milion
print("#Chapter4 - Exercise 4.5 - min/max/sum of list of milion")
print(f"Min: {min(numbers)}")
print(f"Min: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

#Chapter4 - Exercise 4.6 - odd numbers in 1-20 range
print("#Chapter4 - Exercise 4.6 - odd numbers in 1-20 range")
odd_numbers = list(range(1,21,2))
print(f"Odd numbers in 1-20 range: {odd_numbers}")

#Chapter4 - Exercise 4.7 - list of squares of 3-30 numbers
print("#Chapter4 - Exercise 4.7 - list of squares of 3-30 numbers")
squares = []
for value in range(3,31):
    squares.append(value**2)
for square in squares:
    print(square)

#Chapter4 - Exercise 4.8 - list of cubes of 1-10 numbers
print("#Chapter4 - Exercise 4.8 - list of cubes of 1-10 numbers")
cubes = []
for value in range(1,11):
    cubes.append(value**3)
for cube in cubes:
    print(cube)

#Chapter4 - Exercise 4.9 - list of ^3 in 1-10 range in list nesting
print("#Chapter4 - Exercise 4.9 - "
      "list of ^3 in 1-10 range in list nesting")
cubes = [value**3 for value in range(1,11)]
print(cubes)

#Chapter4 - Slices - Warm up
print(f"0-3 slice of teams list: {teams[0:3]}")
print(f"2-5 slice of teams list: {teams[2:5]}")
print(f":2 slice of teams list: {teams[:2]}")
print(f"3: slice of teams list: {teams[3:]}")
print(f"-2: slice of teams list: {teams[-2:]}")

print("TOP3 teams in Premier League:")
for team in teams[0:3]:
    print(team)

#Chapter4 - Copying list - Warm up
best_teams = teams[:]
print(f"Best teams: {best_teams}")

#Chapter4 - Excercise 4.10 - different list splits
print("Chapter4 - Excercise 4.10 - different list splits")
print(f"Firs two elements on a list are: {teams[0:2]}")
list_length_int = int(len(teams)/2)
print("Three elements in the middle of the list are:"
      f" {teams[(list_length_int-1):(list_length_int+2)]}")
print(f"Last three elements of the list are: {teams[-3:]}")

#Chapter4 - Excercise 4.11 - copy of pizzas list
pizzas = ["Capriciosa", "Diavolo", "Quatro fromaggi"]
friend_pizzas = pizzas[:]
print(f"My pizzas: {pizzas}")
print(f"My friend's pizzas: {friend_pizzas}")
pizzas.append("Bianca")
friend_pizzas.append("Fungi")
print(f"My pizzas: {pizzas}")
print(f"My friend's pizzas: {friend_pizzas}")

#Chapter4 - Tuples warm up
rectangle_dimensions = (6,4)
print(f"First dimension: {rectangle_dimensions[0]}\n"
      "Second dimension: {rectangle_dimensions[1]}")

#Chapter4 - Excercise 4.13 - tuples
print("\n#Chapter4 - Excercise 4.13 - tuples")
buffet = ("Dumplings","Burger","Pizza","Pasta","Chicken tenders")
for dish in buffet:
    print(dish)
    
