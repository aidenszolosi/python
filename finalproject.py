#Aiden Szolosi
#Final Project
#12/14/22
#This program is an evenly divisible calculator that allows the user to enter a range of values and determine if each value in the range is evenly divisible by 3, by 5, or by both 3 and 5
#This program will iterate through every number in the range, printing the active number as well as what it is divisible by if applicable. Rather than showing both 3 and 5, the program shortens this to "Both"








#Starting out with needed inputs
StartVal = int(input('Please enter the starting value: '))
EndVal = int(input('Please enter the ending value: '))

#Creating a function to check the modulo operator
def modulocheck(num):
    result = ''
    if num % 3 == 0:
        result += " -- 3"
    
    if num % 5 == 0:
        result += " -- 5" 
    return result


#Executing the function for every number in the range
for num in range(StartVal, EndVal+1):
    x = modulocheck(num)
    Moutput = (str(x))
    if " -- 3 -- 5" in Moutput:
        Moutput = ' -- Both'  
    output = (str(num)+Moutput)
    print(output)






