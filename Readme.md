Introduction:
    **To check installed python version**

    ansible@ansible-PowerEdge-T30:~$ python3 --version ; python3 -V
    Python 3.10.12
    Python 3.10.12

    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 
    Python 3.10.12 (main, Jan 26 2026, 14:55:28) [GCC 11.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sys
    >>> print(sys.version)
    3.10.12 (main, Jan 26 2026, 14:55:28) [GCC 11.4.0]
    >>> print(sys.version_info)
    sys.version_info(major=3, minor=10, micro=12, releaselevel='final', serial=0)
    >>> import platform
    >>> print(platform.python_version())
    3.10.12
    >>> 

Important Topics
    1. Expressions
    2. Data Types
    3. Variables

    Expressions: An expression is a combination of values, variables, and operators that the Python interpreter evaluates to produce a new value.
        Exp = Values/Variables + Operators
    
    Multiple Operators are available with Python
        +   => Addition
        -   => Subtraction
        *   => Mutltiplication (Asterisk)
        /   => Division (Forward Slash)
        ()  => Paranthesis
        **  => Exponentiation (Double Asterisk without Space)
        %   => Modulus/Reminder (Percentage Symbol)
        //  => Integer Division (Double Forward Slash)
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 
    Python 3.10.12 (main, Jan 26 2026, 14:55:28) [GCC 11.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 5 + 5    # Addition 
    10
    >>> 14 - 6   # Subtraction
    8
    >>> 5 * 8    # Multiplication
    40
    >>> 24 / 4   # Division
    6.0
    >>> 3**3     # Exponentiation
    27
    >>> remainder = 10 % 3    # Modulus Reminder Example
    >>> print (remainder)
    1
    >>> 7//2      # Integer Division
    3
    >>> 2 + (5*4) # Paranthesis example
    22
    >>> 'Ragu' + 'Ram'
    'RaguRam'
    >>> 'Ragu' + ' Ram'
    'Ragu Ram'
    >>> 

    Data Types: Python has several built-in data types to classify information
    a) Numeric ==> Integer, Float & Complex Number
    b) Dictionary
    c) Boolean
    d) Set
    e) Sequence Type ==> String, List & Tuple

    Numeric --> Used Interactive Shell Prompt
        >>> x = 15
        >>> y = 15.5
        >>> z = 2+5j
        >>> print (int(y))      # Integer
        15
        >>> print (float(x))    # Float
        15.0
        >>> print (complex(z))  # Complex
        (2+5j)
        >>> print (int(x+y))    # Here actual output is 30.5 but we asked to print only integer
        30
        >>> print (float(x+y))  # Printing with decimal value as floating
        30.5
        >>>

    String --> Used Interactive Shell Prompt
        >>> 'Hello Python Learner'      # Simple String execution with single quotes.
        'Hello Python Learner'
        >>> 'Python' + ' Learner'       # String Concatenation
        'Python Learner'
        >>> 'Python ' * 5               # String Replication
        'Python Python Python Python Python '
        >>> 
    
    Variables --> Used Interactive Shell Prompt
        >>> name = 'Nimalan'    # Variables should be kept under quotes
        >>> print (name)
        Nimalan
        >>> del name            # To delete the Variable
        >>> print (name)        # This ensures that after deleting the variable we cannot use it
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'name' is not defined
        >>> name = 'Nimalan'    # Variables should be kept under quotes
        >>> age = '7'
        >>> print ('My name is:' + name)   # Adding name with another strings - Here it's String Concatenation
        My name is:Nimalan
        >>> print ('My Age is:' + age)
        My Age is:7
        >>> print ('Next year my age will be: ' + str(int(age) + 1) + ' years')
        Next year my age will be: 8 years
        >>> print (len(name))
        7
    
    Practice Program:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat hello.py 
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

    Output:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 hello.py 
    Hello Python Learners
    What is your Age:
    7
    Your Age is:7
    Please enter your name: A.R.Nimalan
    A.R.Nimalan
    Enter two numbers separated by space: 7 8 
    First number: 7
    Second number: 8
    Enter two numbers with space: 10 15
    Sum: 25
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ 

    Variables example for Command line Arguments:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat hello_command_line_arguments.py 
    import sys

    # sys.argv is a list that contains the script name and all arguments passed to it
    print("Script name:", sys.argv[0])  # sys.argv[0] is the script name itself

    # Check if any arguments were passed
    if len(sys.argv) > 1:
        print("Arguments:", sys.argv[1:])  # sys.argv[1:] contains all arguments except the script name

    Output:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 hello_command_line_arguments.py Hello Mr.A.R.Nimalan
    Script name: hello_command_line_arguments.py
    Arguments: ['Hello', 'Mr.A.R.Nimalan']

    1) Boolean Values
    2) Comparison Operators
    3) Boolean Operators

    Boolean Values: Boolean data types have only 2 values ==> True & False
    Acceptable Format of Boolean Values     ==> True & False (Here first letter will be upper case, following all will be lower case)
    Not Acceptable Format of Boolean Values ==> TRUE / false / 'True' (All these formats are not accepted, we need provide as stated above only)
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 
    Python 3.10.12 (main, Jan 26 2026, 14:55:28) [GCC 11.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> True        # Acceptable Format
    True
    >>> False       # Acceptable Format
    False
    >>> false       # NOT Acceptable Format
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'false' is not defined. Did you mean: 'False'?
    >>> 'True'      # NOT Acceptable Format and it will take it as String
    'True'
    >>> FALSE       # NOT Acceptable Format
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'FALSE' is not defined. Did you mean: 'False'?
    >>> 

    Comparison Operators:
        Operator            Meaning
          ==                Equal to
          !=                Not Equal to
          <                 Less than
          >                 Greater than
          <=                Less than or equal to
          >=                Greater than or equal to

    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 
    Python 3.10.12 (main, Jan 26 2026, 14:55:28) [GCC 11.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 100 == 100
    True
    >>> 100 != 90
    True
    >>> 100 < 150
    True
    >>> 100 > 90
    True
    >>> 100 <= 100
    True
    >>> 100 >= 100
    True
    >>> 100 == 90
    False
    >>> 100 != 100
    False
    >>> 100 < 90
    False
    >>> 100 > 101
    False
    >>> 100 <= 99
    False
    >>> 100 >= 101
    False
    >>> 100 == 100.0    # Integer & Float values will remain same with the comparison
    True
    >>> 100 == '100'    # Integer & String are not same
    False
    >>> myage = 41
    >>> myage < 20      # Comparison example with variables
    False
    >>> 
    
    Boolean Operators:
         X           Y               X AND Y
        True        True              True
        True        False             False
        False       True              False
        False       False             False
        
         X           Y               X OR Y
        True        True              True
        True        False             True
        False       True              True
        False       False             False

         X           NOT X
        True         False  
        False        True
    
    Practice Examples:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat boolean_operators.py 
    # AND Operator
    age = 25
    has_license = True

    if age >= 18 and has_license:
        print("Eligible to drive")

    # OR Operator
    has_store_credit = False
    made_recent_purchase = True

    if has_store_credit or made_recent_purchase:
        print("Eligible for discount")

    # NOT Operator
    is_raining = True

    if not is_raining:
        print("Go for a walk")
    else:
        print("Stay inside")
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 boolean_operators.py 
    Eligible to drive
    Eligible for discount
    Stay inside
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ 

    
Flow Control Statements:
    Conditional Statements - if, else, elif
    Looping/Interactive Statements - for, while, else-clause
    Transfer Statements - break, continue, pass
    
    Colon (:) ==> In python colon is a crucial part of the syntax where it used to signal the start of a code block and for data manipulation operation like slicing.

    Conditional Statements:
    IF Example Exercises:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat if_example.py 
    name = 'Nial'
    if name == 'Nial':
        print ('Hello, Nial Welcome to If statements')
    print ('Done')
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 if_example.py 
    Hello, Nial Welcome to If statements
    Done
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ 

    IF-ELSE:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat if_else_example.py 
    name = 'Nial'
    if name == 'Nial':
        print ('Hello, Nial')
    else:
        print ('Wrong Name')
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 if_else_example.py 
    Hello, Nial
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat if_else_example.py 
    name = 'Ni'
    if name == 'Nial':
        print ('Hello, Nial')
    else:
        print ('Wrong Name')
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 if_else_example.py 
    Wrong Name
    
    IF-ELIF-ELSE:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat if_elif_example.py 
    name = 'Ni'
    if name == 'Ni':
        print ('Hello, Ni')
    elif name == 'Pappu':
        print ('Hello, Pappu')
    else:
        print ('Nial')
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 if_elif_example.py 
    Hello, Ni
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat if_elif_example.py 
    name = 'Pappu'
    if name == 'Ni':
        print ('Hello, Ni')
    elif name == 'Pappu':
        print ('Hello, Pappu')
    else:
        print ('Nial')
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 if_elif_example.py 
    Hello, Pappu
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat if_elif_example.py 
    name = 'Nial'
    if name == 'Ni':
        print ('Hello, Ni')
    elif name == 'Pappu':
        print ('Hello, Pappu')
    else:
        print ('Nial')
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 if_elif_example.py 
    Nial

    Looping & Transfer Statements:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat while_example.py 
    count = 0
    while count < 5:
        print ('Hello World')
        count = count + 1  # Here if count is missing then uninterrupted loop will print on Hello World. We need use CTL+C to cancel the loop. 
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 while_example.py 
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ 

    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat while_user_input.py 
    name = ''
    while name != 'Nial':
        print ('Please type your name:')
        name = input()
    print ('Hello,',name)
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 while_user_input.py 
    Please type your name:
    Pappu
    Please type your name:
    Nimalan
    Please type your name:
    Nial
    Hello, Nial

    Transfer - BREAK Statement:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat while_true_break_example.py 
    name = ''
    while True:
        print('Pleae enter your name:')
        name = input()
        if name == 'Nial':
            break
    print('Thank You')
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 while_true_break_example.py 
    Pleae enter your name:
    Pappu
    Pleae enter your name:
    Nimalan
    Pleae enter your name:
    Nial
    Thank You

    Transfer - CONTINUE Statement:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat while_true_continue_example.py 
    count = 0
    while count < 5:
        count = count + 1
        if count == 3:
            continue # Here if the value is 3 then it will go back to the loop and will not print 3, see the below output
        print('Count is ' + str(count))
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 while_true_continue_example.py 
    Count is 1
    Count is 2
    Count is 4
    Count is 5

    FOR LOOPING STATEMENTS:
    Before getting into FOR loop, we need to learn about "RANGE Functions". It has 3 parameters like start, stop & set. 

        >>> print(list(range(10)))          # This will print the value from 0 to 9, always range starts from 0. Ending will be before the stop value. 
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        >>> print(list(range(2, 10)))       # This will print the value from 2 to 9, always range starts from start value provied. Ending will be before the stop value.
        [2, 3, 4, 5, 6, 7, 8, 9]
        
        >>> print(list(range(2, 10, 2)))    # Here, the start value is 2, end value is before 10 and it has to set 2 of start value. So the answer will be 2, 4, 6 & 8
        [2, 4, 6, 8]
    
        Exercise FOR loop:
        ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat for_example.py 
        print ('My Name is')
        for i in range(3):
            print('Raghuram ' + str(i))
        
        ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 for_example.py 
        My Name is
        Raghuram 0
        Raghuram 1
        Raghuram 2

        ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat for_count.py
        total = 0
        for i in range(101):    # Total number starts with 0 and from 0 to 100, add all the number and print the value. 
            total = total + i
        print (total)
        
        ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 for_count.py 
        5050

    FUNCTIONS:
        Built-In functions {print(), input(), len()}
    If we want to call other modules then we need to use import to call the modules
    >>> import random
    >>> random.randint(1, 10)   # Printing random values between 1 & 10
    5
    >>> random.randint(1, 10)   # Printing random values between 1 & 10
    10
    >>> help(random)    # Help modules for random module and it's options

    >>> from random import *    # Another way to call module, here we don't want to mention random module infront of calling it's functions. 
    >>> randint(1, 10)
    8
    >>> randint(1, 10)
    1
    >>> randint(1, 10)

    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ cat module_functions_example.py
    import random
    print(random.randint(1,10))

    from random import *
    print (randint(11,20))

    import sys
    print ('Hello')
    sys.exit()          # Calling SYS.EXIT funtion
    print ('Thank You')
    
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3 module_functions_example.py 
    10
    14
    Hello

    Installig a Module using PIP 
    >>> import pyperclip
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'pyperclip'
    >>> 

    Installing modules
    $ sudo apt install python3-pip
    >>> import pyperclip
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'pyperclip'

    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ pip3 install pyperclip
    Defaulting to user installation because normal site-packages is not writeable
    Collecting pyperclip
      Downloading pyperclip-1.11.0-py3-none-any.whl (11 kB)
    Installing collected packages: pyperclip
    Successfully installed pyperclip-1.11.0
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ 

    For Copy/Paste Terminal values we need XCLIP package needs to be installed on your linux machine
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ sudo apt-get install xclip
    [sudo] password for ansible: 
    Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    The following package was automatically installed and is no longer required:
      libffi7
    Use 'sudo apt autoremove' to remove it.
    The following NEW packages will be installed:
      xclip
    0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
    Need to get 18.3 kB of archives.
    After this operation, 60.4 kB of additional disk space will be used.
    Get:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 xclip amd64 0.13-2 [18.3 kB]
    Fetched 18.3 kB in 1s (31.5 kB/s)
    Selecting previously unselected package xclip.
    (Reading database ... 260128 files and directories currently installed.)
    Preparing to unpack .../xclip_0.13-2_amd64.deb ...
    Unpacking xclip (0.13-2) ...
    Setting up xclip (0.13-2) ...
    Processing triggers for man-db (2.10.2-1) ...

    Working with PYPERCLIP for Copy/Paste:
    ansible@ansible-PowerEdge-T30:~/CloudDataOps/Python_Learnings$ python3
    Python 3.10.12 (main, Jan 26 2026, 14:55:28) [GCC 11.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> pyperclip.copy('Hello')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'pyperclip' is not defined
    >>> import pyperclip
    >>> pyperclip.copy('Hello')
    >>> pyperclip.paste()
    'Hello'
    >>> pyperclip.copy('Hello, Nial')
    >>> pyperclip.paste()
    'Hello, Nial'


    
    































