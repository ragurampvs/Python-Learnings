name = "Nial" # Global variable

def read_global():
    # Reading 'name' directly from global scope
    print(f"Inside function: {name}") 

read_global()
print(f"Outside function: {name}")

