import sys

print('--------------------------------------')
print('------EUCLIDEAN ALGORITHM SOLVER------')
print('--------------------------------------\n\n')

num1 = int(input ('Enter the first number: \n'))
num2 = int(input ('Enter the second number: \n'))
count = 0

#Error handling for if zero is given for input
if num1 == 0:
    print('Invalid input for your first number\n')
    sys.exit(0)
if num2 == 0:
    print('Invalid input for your first number\n')
    sys.exit(0)
    
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
            count += 1
    
    num1 = str(num1)
    num2= str(num2)
    newCount = count
    newCount = str(newCount)
    print('Program done.')
    print('The GCF is ' + num1)
    print('Result obtained in: ' + newCount + ' cycles.')
    print('Resulting in a complexity of O(' + newCount + ').')