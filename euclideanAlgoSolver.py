print('--------------------------------------')
print('------EUCLIDEAN ALGORITHM SOLVER------')
print('--------------------------------------\n\n')

num1 = int(input ('Enter the first number: \n'))
num2 = int(input ('Enter the second number: \n'))

#Error handling for if zero is given for input
if num1 == 0:
    print('Invalid input for your first number\n')
if num2 == 0:
    print('Invalid input for your first number\n')
else:
    #Error handling for if numbers are mispositioned
    if num2 > num1:
        tempVar = num1
        num1 = num2
        num2 = tempVar
    
    #Euclid's Algorithm
    else:
        while num2 != 0:
            temp1 = num2
            temp2 = num1 % num2
            num2 = temp2
            num1 = temp1
    
    num1 = str(num1)
    num2= str(num2)
    print('Program done.')
    print('The GCF is ' + num1)
