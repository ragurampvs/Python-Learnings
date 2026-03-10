# This python program says Hello, asks user input and using few funtions

print ('Hello Python Learners')

# Option 1 - Getting User Input
print ('What is your Age:')
myage = input()
print ('Your Age is:' + myage)

# Option 2 - Getting User Input
myname = input('Please enter your name: ')
print (myname)

# Option 3 - Getting Multiple User Inputs
a, b = input("Enter two numbers separated by space: ").split()
print("First number:", a)
print("Second number:", b)

# Option 4 - Getting Multiple User Inputs
x, y = map(int, input("Enter two numbers with space: ").split())
print("Sum:", x + y)
