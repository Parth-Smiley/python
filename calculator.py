print("Welcome to calc")

operator = input("Which operation you want to perform (+,-,%,/,*) : ")

first_operand = int(input("Enter your first operand : "))
second_operand = int(input("Enter your second operand : "))

def addition(x,y):
    result = x+y
    return result

def subtraction(x,y):
    result = x-y
    return result

def remainder(x,y):
    result = x%y
    return result

def division(x,y):
    result = x/y
    return result

def multiplication(x,y):
    result = x*y
    return result


if operator == "+" :
    print(addition(first_operand,second_operand))
elif operator == "-" :
    print(subtraction(first_operand,second_operand))
elif operator == "%" :
    print(remainder(first_operand,second_operand))
elif operator == "/" :
    print(division(first_operand,second_operand))
elif operator == "*" :
    print(multiplication(first_operand,second_operand))

else:
    print("Sorry")