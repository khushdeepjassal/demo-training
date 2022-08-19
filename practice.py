# a=14
# b=20
# c=64
# if(b>c):
#     print('h')
# elif(a>c):
#         print('l')
# elif(b==c):
#     print('r')
# else:
#     print('lh')


# # for x in range (10):
# #     print(x) 


# for x in range (10):
#     for y in range (11,15):
#         print(x,y)


# for z in range(4):
#     for q in range (4):
#         print('*',end=' ')
#     print(' ')

# for h in range(4):
#     for k in range(h+1):
#         print('*',end='')
#     print(' ')    


# for p in range (10):
#     if p==5:
#         break
#         print('hello')
#     print(p)
    

# for p in range (10):
#     if p==5:
#         continue
#         print('hello')
#     print(p) 

         

# print(50<<4)
# print(64>>5)

# a='i am the best'
# print(a)
# if(a[0]=='i'):
#     print('it has sepecific character')
# else:
#      print('not')    

# l=[10,20,30,40]
# print(l)

# l1=['hello',10,20,30,0]
# l1.append(40)
# print(l1)

# t1=(10,20,30,0)
# print(t1)
# print(type(t1))

# for x in range (5):
#     a=input('enter no.')
#     l1.append(a)
#     print(l1)

# s={10,20,40,50,60}
# print(s)
# print(type(s))

# def disp(a=10,b=40,c=56):
#     d=a+b+c
#     print(a,b,c,d)
# disp()

# def sum():
#     print('a+b')
# sum()

# def outerfunction(text):
#     text=text
#     def innerfunction():
#         print(text)
#         innerfunction()

# if_name_=='_main__':
# outerfunction('hey')    


# a=10
# def f1():
#     print('f1 , a')
# def g():

#    a=20
#    print('g',a)
# def h():
#     global a
#     a=30
#     print('h',a)
# print('glo',a)     
# f1()
# print('glo',a)
# g()
# print('glo',a)
# h()
# print('glo',a)


# def f1():
#     a=10
#     def f2():
#         print('hello')
#         nonlocal a 
#         a=40
#         print(a)
#     f2()
# f1()
            
# class demo:
#     def display(self):
#         print('10+20')   
# ob=demo()
# ob.display()         
  
# class A:
#    def __init__(self):
#         print('hello')
#    def f1(self):
#         print('h')
# ob=A()
# ob.f1()

# class A:
#     def __str__(self):
#         return'hello'
# ob=A()
# print(ob)

# import practice 
# practice.f1()
# def f2(): 
#     print('f2')
# f2()

# from datetime import datetime

# today = datetime.now() 
# print("Today's date:", today)


# exception...............
# from abc import abc,abstractmethod
# class student(abc):
#     @abstractmethod
#     def m1(self):
#     pass
# class A(student):
#     def m1(self):
#         print()


# from tkinter import *
# ab =Tk()
# ab.mainloop()

# from threading import*
# class A(Thread):
#     def run(self):
#         for x in range(5):
#             print(x)
# ob=A()
# ob.start()
# class A():
#     def run(self):
#         for x in range(5):
#             print(x) 
# ob=A()
# t1=Thread(target=ob.run) 
# t1.start()                      

# from threading import*
# import time
# def f1(n):
#     for x in range(n):
#         time.sleep(4)
#         print(current_thread().name,x)
# t1=Thread(target=f1,args=[5],name='thread1')
# t1.start()
# def f2():
#     for x in range(6,11):
#         time.sleep(3)
#         print(current_thread().name,x)
#     t2=Thread(target=f2,name='thread2')
#     t2.start()
#     t1.join()
#     t2.join()
#     print(current_thread().name)

# from threading import*
# class A(Thread):
#     def run(self):
#         for x in range(5):
#             print(x)
# ob=A()
# ob.start()

# s='bhwn'
# substrings=[]
# for x in range(len(s)):
#     for y in range(len(s)-x):
#         s.append(s[y:x+y+1])
# print(s)        

# for even in range(422,623):
#    if even % 2 == 0:
#     print(even)



# p = [ [1,1],[3,4],[4,9] ]
# q = [ [1,6,3],[4,5,5] ]


# result = [ [0,0,0],[0,0,0],[0,0,0] ]

# multiplication = []

# for i in range( len(p) ):
   
#    for j in range(len(q[0])):
       
#        for k in range(len(q)):
#            result[i][j] += p[i][k] * q[k][j]
  

# for r in result:
#    print(r)

# pattern = int(input("Enter the side of the square  : "))

# for p in range(5):
#     for q in range(5):
#         if(p == 0 or p == 5 - 1 or q == 0 or q == 5 - 1):
#             print('*', end = ' ')
#         else:
#             print(' ', end = ' ')
#     print()

# n=int(input("Enter n: ")) 
# d={} 
# for i in range(n): 
   
#     name=input("Enter sub  name: ") 

#     marks=int(input("Enter sub marks: ")) 
#     d[name]=[name,marks] 
# for k in d: 
#     if(d[k][1]>75): 
#         print(d[k][0]) 

# d = {}
# for i in range(1,4): 
#     print('student',i)
#     sub='math'
#     d[sub] = {}
#     marks = input("Enter marks : ")
#     d[sub]["marks"] = marks
#     sub='eng'
#     d[sub] = {}
#     marks = input("Enter marks ")
#     d[sub]["marks"] = marks
#     sub='sci'
#     d[sub] = {}
#     marks = input("Enter marks  ")
#     d[sub]["marks"] = marks
#     print(d)




# s='{1}, {0}, and {2}’

# s.format(‘hello’, ‘Hi’, ‘goodday’)

# sum(4,2,3)

# sum([4,4,6])

# def f(x):
#     def f1(*args, **kwargs):
#            print("StepGndec")
#            return x(*args, **kwargs)
#     return f1


# class tester:
#      def __init__(self, id):
#              id = "230"
#              self.id = str(id)
# temp = tester(15)
# print(temp.id)


# class Dog:
#      def walk(self):
#                return "*walking*"
 
#      def speak(self):
#           return "Woof!"
 
# class JackRussellTerrier(Dog):
#       def speak(self):
#          return "Arff!"

#  bobo = JackRussellTerrier()
#  bobo.walk()


























