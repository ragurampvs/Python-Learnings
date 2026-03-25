x = "Global Value"  # Global variable

def my_function():
    x = "Local Value"  # Local variable with same name
    print("Inside function:", x)

my_function()
print("Outside function:", x)
