'''
Create a menu to perform basic mathematical operations (addition, subtraction, multiplication, division, modulo) on two numbers.

'''
def math_operations_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    
    choice = int(input("Enter your choice: "))

    a, b = map(int, input("Enter two numbers: ").split())

    if choice == 1:
        print("Addition:", a + b)  
    elif choice == 2:
        print("Subtraction:", a - b)  
    elif choice == 3:
        print("Multiplication:", a * b)  
    elif choice == 4:
        if b != 0:  
            print("Division:", a / b)
        else:
            print("Error.")
    elif choice == 5:
        if b != 0: 
            print("Modulo:", a % b)
        else:
            print("Error")
    else:
        print("Invalid option")
        
math_operations_menu()
