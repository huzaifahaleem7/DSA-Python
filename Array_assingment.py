# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_number = int(input("Enter the Max Number: "))
numbers = []
for i in range (0, max_number):
    if i % 2 != 0:
        numbers.append(i)
    
print(numbers)