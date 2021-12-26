def arithmetic_arranger(a): #build function
    b = a.split()   #split user input into list
    num1 = b[0]
    operation = b[1]
    num2 = b[2]
    if len(num2) > 4 and len(num1) > 4 or len(num2) > 4: #Prohibit more than 4 digits input
        print("Error: Numbers cannot be more than four digits.")
        exit()
    try: #Prohibit user input other than number and operation
        if operation == "+":
            res = int(num1) + int(num2)
        elif operation == "-":
            res = int(num1) - int(num2)
        else:  #Prohibit operator input other than + -
            print("Error: Operator must be '+' or '-'.")
            exit()

    except:
        print("Error: Numbers must only contain digits.")
    
    
    return b, num1, operation, num2, res 
    
    

n = int(input("Input max arithmetic problem (1 until 5): ")) #input maximum arithmetic problems
if n > 5:
    print("Error: Too many problems.")
    exit()
print('Input example: 123 + 45')

ariths = [] 
for i in range(0,n): #Input Arithmetic problems into list
    metic = str(input("Input arithmetics operation : "))
    ariths.append(metic)
for arith in ariths: #Calling function and arange output format
    b, num1, operation, num2, res = arithmetic_arranger(arith)
    number = len(str(max(b,key=len))) + 2
    print(f"{num1 : >{number}}",end=' '*4)
print("\n",end="")
for arith in ariths:
    b, num1, operation, num2, res = arithmetic_arranger(arith)
    number = len(str(max(b,key=len))) + 2
    print(f"{operation : >1}{num2 : >{number - 1}}",end=' '*4)
print("\n",end="")
for arith in ariths:
    b, num1, operation, num2, res = arithmetic_arranger(arith)
    number = len(str(max(b,key=len))) + 2
    print(f"{'-'*number : >{number}}",end=' '*4)
print("\n",end="")
for arith in ariths:
    b, num1, operation, num2, res = arithmetic_arranger(arith)
    number = len(str(max(b,key=len))) + 2
    print(f"{res : >{number}}",end=' '*4)

