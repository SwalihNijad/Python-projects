try:

    a = int(input("Enter a first number: "))

    b = int(input("Enter a second number"))

    print('''What kind of operations you want to perform? 
          
Press '+' to perform Addition
Press '-' to perform Subtraction
Press '*' to perform Multiplication
Press '/' to perform Division     
    ''')

    o = input("Enter operations")
    match o :
        case '+':
            print(f"The Result is : {a + b}")

        case '-':
            print(f"The Result is : {a - b}")

        case '*':
            print(f"The Result is {a * b}")

        case '/':
            print(f"The Result is {a / b}")

except Exception as e :
    print("Input is invalid! Enter Integer Value")         

else:
    print("Thank you!")