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
