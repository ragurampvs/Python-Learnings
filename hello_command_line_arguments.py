import sys

# sys.argv is a list that contains the script name and all arguments passed to it
print("Script name:", sys.argv[0])  # sys.argv[0] is the script name itself

# Check if any arguments were passed
if len(sys.argv) > 1:
    print("Arguments:", sys.argv[1:])  # sys.argv[1:] contains all arguments except the script name
