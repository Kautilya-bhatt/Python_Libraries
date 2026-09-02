'''#####7. Functions-Based Calculator Create separate functions for addition, subtraction, multiplication, and division. Take the user's choice and numbers as input, call the appropriate function, and display the result. 
Expected concepts: Functions, parameters/arguments, return values, and conditions#####.'''

def add(num1,num2):
    return num1+num2

def substract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2


def calculator():
    print("press 1 for addition : ")
    print("press 2 for substaction : ")
    print("press 3 for multiplication : ")
    print("press 4 for division : ")
    print("press 5 for exit : ")
calculator()
choice=input("Enter your choice 1/2/3/4 : ")
n1=float(input("Enter a number1: "))
n2=float(input("Enter a number2 : "))


if choice not in  ['1','2','3','4']:
    print ("Invalid choice ")
    

elif choice == "1":
    result=add(n1,n2)
    print("Addition =" ,result)

elif choice == "2":
    result=substract(n1,n2)
    print("Substraction =" ,result)

elif choice == "3":
    result=multiply(n1,n2)
    print("Multiplication =" ,result)
    

elif choice == "4":
    if n2>0:
       result=divide(n1,n2)
       print("Division =" ,result)
       
    else:
        print("Zero divison Error")


