
#palindrome.................

#  num=int(input('enter the value :'))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print('the value is a palindrome!')
# else:
#     print('the value is not palindrome!')        
 

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


# num = int(input("Enter a number: "))

# # If number is greater than 1
# if num > 1:
#    # Check if factor exist  
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#    else:
#        print(num,"is a prime number")
       
# # Else if the input number is less than or equal to 1
# else:
#    print(num,"is not a prime number")# fiboonic............

# def Fibonacci(n):
   
#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")
 
#     # Check if n is 0
#     # then it will return 0
#     elif n == 0:
#         return 0
 
#     # Check if n is 1,2
#     # it will return 1
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
 
# # Driver Program
# print(Fibonacci(9))


# Armstrong Number Program In Python..............

# number = 153
# temp = number
# add_sum = 0
# while temp!=0:
#     k = temp%10
#     add_sum +=k*k*k
#     temp = temp//10
# if add_sum==number:
#     print('Armstrong Number')
# else:
#     print('Not a Armstrong Number')

# Leap Year Program...........

# def CheckLeap(Year):  
#   # Checking if the given year is leap year  
#   if((Year % 400 == 0) or  
#      (Year % 100 != 0) and  
#      (Year % 4 == 0)):   
#     print("Given Year is a leap Year");  
#   # Else it is not a leap year  
#   else:  
#     print ("Given Year is not a leap Year")  
# # Taking an input year from user  
# Year = int
# (input("Enter the number: "))  
# # Printing result  
# CheckLeap(Year)  

# Program To Find Area......................

# l = float(input('Enter the length of a Rectangle: '))
# b = float(input('Enter the breadth of a Rectangle: '))
# Area = l * b
# print("Area of a Rectangle is: %.2f" %Area)

# reverse a list...........

# lst = [10, 11, 12, 13, 14, 15]
# lst.reverse()
# print("Using reverse() ", lst)
 
# print("Using reversed() ", list(reversed(lst)))


# find  sum of all elements in list......................


# numlist = ['2','4','2','5','7','9','23','4','5']
# # Calculate sum of list
# numsum=0
# for i in numlist:
#     numsum+=int(i)
# print('Sum of List: ',numsum)


# average, max, min  of list elements......................

 
# print("Maximum of 4,12,43.3,19 and 100 is : ",end="")
#print (max( 4,12,43.3,19,100 ) )
# print("Minimum of 4,12,43.3,19 and 100 is : ",end="")
# print (min( 4,12,43.3,19,100 ) )



#13..................
# def grouping_dictionary(l):
#     result = {}
#     for k, v in l:
#          result.setdefault(k, []).append(v)
#     return result
# colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# print("Original list:")
# print(colors)
# print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
# print(grouping_dictionary(colors))


#  check if a set is a subset of another set...................
# 
# test_list = [9, 4, 5, 8, 10]
# sub_list = [10, 5]
 
# # printing original lists
# print("Original list : " + str(test_list))
# print("Original sub list : " + str(sub_list))
 
# # using issubset() to
# # check subset of list
# flag = 0
# if(set(sub_list).issubset(set(test_list))):
#     flag = 1
 
# # printing result
# if (flag):
#     print("Yes, list is subset of other.")
# else:
#     print("No, list is not subset of other.")

# create a symmetric difference and set difference..............................

# set_A = {"ram", "rahim", "ajay", "rishav", "aakash"}
# set_B = {"aakash", "ajay", "shyam", "ram", "ravi"}
# print(set_A ^ set_B)

# remove an empty tuple(s) from a list of tuples......................

# def Remove(tuples):
#     tuples = [t for t in tuples if t]
#     return tuples
 
# # Driver Code
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
#           ('krishna', 'akbar', '45'), ('',''),()]
# print(Remove(tuples))