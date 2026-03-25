def function_one():
    # 'secret_value' exists only inside this local scope
    secret_value = "My_Secrets"
    print(f"Inside function_one: {secret_value}")

def function_two():
    # This will cause a NameError because 'secret_value' is NOT in this scope
    print(f"Inside function_two trying to access: {secret_value}")

function_one()
function_two()
