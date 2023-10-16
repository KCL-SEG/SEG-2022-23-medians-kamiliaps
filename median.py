"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
sorted_numbers = numbers.sort()
mid = len(sorted_numbers)/2

if len(sorted_numbers)%2==0:
    median = (sorted_numbers[mid]+sorted_numbers[mid-1])/2

elif len(sorted_numbers) == 1:
    median = sorted_numbers[0]

else:
    median = sorted_numbers[mid]

print(median)
    
