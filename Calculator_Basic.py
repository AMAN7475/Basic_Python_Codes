def add(value_1,value_2):
    return (value_1 + value_2)

def substract(value_1,value_2):
    return (value_1 - value_2)

def multiply(value_1,value_2):
    return (value_1 * value_2)

def divide(value_1,value_2):
    return (value_1 / value_2)      

def convert_to_integer(value):
    new = value // 1

    aman = value - new 

    if aman == 0.0:
        return(int(value))

    else:
        return(value)   

def AMAN_R(): 
    select = int(input("Select operation among 1,2,3,4 : "))

    if select == 1:
        print ("{} + {} = {}".format(Num_1,Num_2,convert_to_integer(add(Num_1,Num_2))))

    elif select == 2:
        print ("{} - {} = {}".format(Num_1,Num_2,convert_to_integer(substract(Num_1,Num_2))))
        
    elif select == 3:
        print ("{} * {} = {}".format(Num_1,Num_2,convert_to_integer(multiply(Num_1,Num_2))))
            
    elif select == 4:
        print ("{} / {} = {}".format(Num_1,Num_2,convert_to_integer(divide(Num_1,Num_2))))  

    else:
        print("Invalid Input")
        AMAN_R()     

Num_1 = float(input("Enter 1st Number : "))
Num_2 = float(input("Enter 2nd Number : "))

print("Select among following operations")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

aman = True
while aman:

    AMAN_R()

    next_calculation = input("Want to do next calculation ? Y/N : ")
    if next_calculation == "N":
        aman = False