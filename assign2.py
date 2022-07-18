
# factorial .................
# num = int(input("Enter a number: "))    
# factorial = 1    
# if num < 0:    
#    print(" Factorial does not exist for negative numbers")    
# elif num == 0:    
#    print("The factorial of 0 is 1")    
# else:    
#    for i in range(1,num + 1):    
    #    factorial = factorial*i    
#    print("The factorial of",num,"is",factorial)    



# pattern..................
# for z in range(4):
#     for q in range (4):
#         print('*',end=' ')
#     print(' ')

# calculator....................
# value1=int(input('enter the value:'))
# value2=int(input('enter the value:'))



# print('{} + {} = '.format(value1, value2))
# print(value1 + value2)
 
# # Subtraction
# print('{} - {} = '.format(value1, value2))
# print(value1 - value2)
 
# # Multiplication
# print('{} * {} = '.format(value1, value2))
# print(value1 * value2)
 
# # Division
# print('{} / {} = '.format(value1, value2))
# print(value1 / value2)

# prime no.............................
num = int(input("Enter a number: "))

# If number is greater than 1
if num > 1:
   # Check if factor exist  
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
# Else if the input number is less than or equal to 1
else:
   print(num,"is not a prime number")