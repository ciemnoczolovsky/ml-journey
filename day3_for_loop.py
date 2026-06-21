#Chapter4 - Exercise 4.1 - for loop
print("#Chapter4 - Exercise 4.1 - for loop")
teams = ['Arsenal', 'Tottenham', 'Chelsea', 'Manchester United', 'Manchester City','Liverpool']
for team in teams:
    print(team)

#Chapter4 - WarmUp - Range + Loop + Comprehension
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

print("Comprehension")
squares = [value**2 for value in range(1,11)]
print(f"Comprehension list: {squares}")

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
