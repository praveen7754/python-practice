

# #variable
# a=10
# b=11
# c="selvamurugan"
# d=10.2
# e=True
# print(a)
# print(b)



"""
#data types
print(type(a))

print(type(b))
print(type(c))
print(type(d))
print(type(e))
"""
'''
#casting
a=int("10")
v=int("20")
print(a+v)

'''
'''
#concating
a="20"
b="30"
print(a+b)
print(int(a)+int(b))
'''
"""

#input
a=input("enter your number")
print(type(a))
"""

#input type
"""
a=int(input("enter the intiger"))
print(type(a))
"""
#ex1
"""
name=input("enter your name:  ")
age=input("enter your age:  ")
add=input("enter your address:  ")

print("your name is ",name)
print("your age is ",age)
print("this is your address",add)
"""
#ex2
# a=int(input("enter num1:  "))
# b=int(input("enter num2:  "))
# c=int(input("enter num3:  "))

# m=a*b*c
# d=a+b+c
# s=m/d
# print(s)

#ex3
"""
+name=input("enter your name: ")
score=int(input("enter your score: "))
dep=input("enter your dep: ")
op=score/10
print("my name is : ",name)
print("my scoree is",op,"/10")
print("my dep is : ",dep)
"""
#if else:
#ex-1
"""
if (False):
    print("yes")
else:
    print("no")
"""
#ex-2
"""
win="win"
if win=="win":
    print("same")
else:
    print("not same")
"""
#ex-3
"""
megna=input("died")
if megna=="died":
    print("surya meets priya")
else:
    print("surya weds megna")
"""
#for
'''
n="apple"
for i in n:
    print(i)

n=int(input())
c=0
'''
#ex-2
'''
for i in range(1,n+1):
    if i%2==0:
        print("even",i)
        c=c+1
    else:
        print("odd",i)
print("even numbers are: ",c)
print("odd numbers are:",n-c)
'''
#ex-3
"""
num=0
n=10
for i in range(1,n+1):
    print("num=",num,"+",i)
    num=num+i
    
print(num)
"""
#ex-4
"""
n=10
b=[]
for i in range(n):
    a=int(input("enter n"))
    b.append(a)
print(b)
num=0
for i in b:
    num+=i # num=num+i
print(num)
"""
#ex-5
"""
for i in range(3):
    print("week",":",i)
    for j in range(1,3+1):
        print("day",j)
"""
#ex=6
"""
for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()
"""
####while loop:
'''it is used for unkown end
when input went a false it will get stop:'''
#ex-1
"""
i=0
while i<200:
    i=i+10
    print(i)
"""

#5*4*3*2*1
"""
num=1
i=1
n=5
while i<=n:
    print(i)
    num=num*i
    i=i+1
print(num)   
"""

#collection of data
#list------------>[]
##tuple---------->() 
##set------------>{} 
##dictionary----->{key:value}

"""list"""
####a=[1,2,3,4,5,6,7,8,9]

"""
-->insertion order preserved
-->allow duplicate value
-->mutable in nature
-->allow all datatypes"""
####"""add """
######a.append(10)
######print(a)
####
####"""index val find"""
######print(a[0])

####
####"""insert"""
####a.insert(0,12)
########print(a)
####
####"""pop"""#-------> index value
####a.pop(0)
######print(a)


"""tuple"""
"""
-->insertion order preserved
-->allow duplicate value
-->imutable in nature
-->allow all datatypes"""

##a=(1)
##print(type(a))
##a=(1,2,3,4,5)
##print(type(a))

"""set"""
"""
-->insertion order doesn't preserved
-->doesn't allow duplicate value
-->mutable in nature
-->allow all datatypes"""
##a={1,2,3,4,5,6,7}
##b={8,9,10}
##a.update(b)
##print(a)
##a.remove(10)
##print(a)
##a.discard(9)
##print(a)

"""dict"""

##a={
##    "name":"selva",
##    "age":20,
##    "location":"chennai"
##}
##print(a.keys())
##print(a.values())
##print(a.items())
##
##"""update"""
##a.update({"age":5})
##print(a)
##
##"""modify"""
##a["location"]="trichy"
##print(a)
##
##"""can add"""
##a["car"]="bmw"
##print(a)

""".......................function...................."""
# """ex-1"""
def painter():
     print("soldra")
     return "hellow i am painter speaking"
     print("soldra")
print(painter())

# """ex-2"""
# def add():
#    print(10+6)``
# add()
"""ex-3"""
##def add(a,b):
##    print(a,"+",b,"=",a+b)
##   
##add(10,20)
##add(10,29)
##add(20,40)
##add(25,25)
"""ex-4"""
##def evenorodd(a):
##    if a%2==0:
##        print("even")
##    else:
##        print("odd")
##n=5
##evenorodd(n)


def add(a,b):
   return(a+b)

a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
added=add(a,b)
op=added*c
print(op)


"""build in functions in py"""
##abs()
##round()
##sum()
##pow()
##min()
##max()
##any()
##all()
##bool()
##enumerate()
##zip()

"""abs is used to change negative val to pos val"""
##a=abs(-29)
##print(a)

"""round is used ot 5.5 is make whole val"""
##a=round(5.5)
##print(a)

"""it used to sum the val in the list"""
##a=[1,2,3,4,5,6,7,8,9]
##b=sum(a)
##print(b)
##"or"
##print(sum(a))

"""it is make power value"""
##a=pow(2,2)
##print(a)
""" it is used to find minimum val in list"""
##a=[1,2,3,4,5,6,7,8,9]
##print(min(a))

"""it is used to find a maximum val in list"""
##a=[1,2,3,4,5,6,7,8,9]
##print(max(a))

"""any"""
"""any one should be true like or operator"""
##a=[True,True]
##print(any(a))
##
##a=[True,False,True]
##print(any(a))
##
##a=[False,False]
##print(any(a))

"""all"""
"""all val should be trure like and operator"""
##a=[False,False,True]
##print(all(a))
##
##a=[False,False,False]
##print(all(a))
##
##a=[True,True,True]
##print(all(a))

"""bool"""
"""it is used to print it is true or false"""
##a=True
##print(bool(a)) #True
##a=False
##print(bool(a)) #False

"""enumrate"""
# enumerate():
# a=[10,20,30,40]
# for i,j in enumerate(a):
#    print(i,j)


#zip():
# x=[('a',1),('b',2),('c',3)]
# k,v=zip(*x)
# print(k)
# print(v)



"""bytcode"""
##import dis
##dis.dis("5")


"""recursive function"""
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# def per(n):   
#     for i in range(1,n):
#         if n%i==0:
#             return n+per(n-1)
#         else:
#             return 1
# print(per(6))

"""lambda"""
# var=lambda arg :expresion

# add=lambda a,b:a+b
# print(add(10,20))

# add=lambda a:print(a+10)
# add(2)

# great=lambda a,b:"greater" if a>b else "lesser"
# print(great(10,20))

# s=lambda a: a**2
# print(s(4))

# palin=lambda a:"palindrom" if a[::-1]==a else "not pali" 
# print(palin("manam"))

"""map"""
# The map() function applies a given function to all items in an iterable (like a list) and returns
# a map object (which can be converted to a list, tuple, etc.).

# var=map(lambda arg:expression,ittration)
# def mapp():
#     i=[1,2,3,4,5]
#     b=map(lambda c:"even" if c%2==0 else "odd",i)
#     print(tuple(b)) 

# mapp()
"""filter"""

# The filter() function filters elements from an iterable based on a condition defined in a function.
#  It returns only the elements for which the function evaluates to True

# a=[1,2,3,4,5,6]
# d=filter(lambda c:c%2==0,a)
# print(tuple(d))

"""reduce"""

# The reduce() function is used to apply a rolling computation to a sequence of elements.
# It is part of the functools module and must be imported before use.

# from functools import reduce
# var=reduce(lambda arg,arg:express,iter)

# d=reduce(lambda e,f:e+f,a)
# print(d)

# a=[1,2,3,4,5,6,7,8,9,10]
# red=reduce(lambda x,y:x+y,a) 
# print(red)



# d=reduce(lambda e,f:e*f,a)
# print(d)

"""word reverse"""
# from functools import reduce
# a=["i","learn","python"]
# b=reduce(lambda x,y: y+" "+x,a)
# print(b)

"""flatning list use reduce """
"""the concept is concate"""
# from functools import reduce
# a=[[1,2],[3,4],[5,6]]
# b=reduce(lambda x,y:x+y,a)
# print(b)


"""clouser function"""

# def outer():
#     print("outer")
#     def inner():
#         print("inner")
#     inner()
# outer()

# def outer1 ():
#     print("outer1")
#     def inner1():
#         print("inner1")
#     return inner1
# a=outer1()()

# def outer2(a):
#     def inner2(b):
#         return a.count(b)
#     return inner2
# print(outer2("praveen")("e"))

"""-------------------------------scope------------------------------"""
"""local scope"""
"""global scope"""
"""enclosing scope"""

# you can't access out side the function
# def add(b):
#     a=5
#     print(a+b)
#     print(a)
# add(4)
"""global"""
# x=5
# print(x)  #--------->5
# def add1():
#     global x
# add1()
# print(x) #----------->15
"""enclosing"""
# a=5
# def outer():
#     print(a)
#     a=10
#     print(a)
#     def inner():
#         print(a)
#         nonlocal a
#         a=a+10
#         print(a)
#     inner()
# outer()

"""decorator"""
# def logging(a):#add a=add
#     def wrapper():
#         print("start log...")
#         a()
#         print("end log...")
#     return wrapper
# @logging
# def add():
#     print(10+2)
# add()


# def sub():
#     print(10-2)
# a=logging(sub)()

# def logging(name):
#     def msg():
#         print("you transcation is being processing")
#         name()
#         print("transcation is completed")
#     return msg

# @logging #a=logging(add)()
# def add():
#     print("selvamurugan")
# add()

# def logging(func):
#     def wrapper():
#         print("your transcation is started")
#         func()
#         print(" yout transcation is completed ")
#     return wrapper

# def authontication(func):
#     def wrapper():
#         print("your transcation is being processing")
#         func()
#         print("money sent to selva")
#     return wrapper

# a=logging(authontication(add))()

# def add():
#     print(10+2)
# add()

# @logging
# @authontication
# def add():
#     print(10+2)
# add()

"""iterator"""
# a=[1,2,3,4,5]
# b=iter(a)
# print(next(b)) #--->1
# print("selva")
# print(next(b)) #--->2
# print(next(b)) #--->3
# print(next(b)) #--->4
# print(next(b)) #--->5
# print(next(b)) #--->error: stop iteration

# a="selva"
# b=iter(a)
# print(next(b)) --->s
# print(next(b)) -->e
# print(next(b))
# print(next(b))
# print(next(b))

# a={"a":1,"b":2,"c":3}   
# b=iter(a)       
# print(next(b))
# print(next(b))
# print(next(b))
# c=iter(a.values())
# print(next(c))
# print(next(c))
# print(next(c))
# c=iter(a.items())
# print(next(c))
# print(next(c))
# print(next(c))

"""generator"""
# def function():
#     yield "hi"
#     print("selva")
#     yield "bye"
#     print("selva")
# a=function()
# print(next(function()))
# print(next(a)) # hi
# print(next(a)) # selva bye
# print(next(a)) # error


# def func():
#     yield "hi-----y"
#     print("hello")
#     yield "selva-----y"
#     print("smsmsmsm")
#     yield ""
# a=func()
# print(next(a))
# print(next(a))


#file handling
#syntax
##file_object=open("filename","mode")

##there is 3 modes
##read
##write
##append

##a=open("file handilg.txt","r")
##print(a)
##
##"""write"""
##a=open("filehand.txt","w") 
##a.write("hi hello i am here,  ")
##a.close()
##
##a=open("filehand.txt","a") 
##a.write("hi hello i am here,  ")
##a.close()
##
##"""append"""
##a=open("filehand.txt","a")
##a.write("python is high level language")
##a.close()
##
##"""read"""
##b=open("filehand.txt","r")
##print(b.read())
##
##"""read a single line"""
##a=open("filehand.txt","r")
##print(a.readline())
##a.close()
##
##"""readliness"""
##a=open("filehand.txt","r")
##print(a.readlines())
####a.close()
##
##r+=1st read,write,append,readline,readlines
##w+=write,read


"""multithreading"""

"""normal method """
# def a():
#     for i in range(5):
#         print("A")
# def b():
#     for i in range(5):
#         print("bb")
# a()
# b()

"""threading"""
# import threading
# import time
# def msg():
#     for i in range(5):
#         time.sleep(2)
#         print("threading")
# def msg2():
#     for i in range(5):
#         time.sleep(2)
#         print("threading----2")
# t=threading.Thread(target=msg)
# t.start()
# t1=threading.Thread(target=msg2)
# t1.start()
"""give arguments to thread"""

# import threading
# import time

# def A(it,s,val):
#     for i in range(it):
#         time.sleep(s)
#         print(val)
# t=threading.Thread(target=A,args=(5,2,"thread 1"))
# t.start()
# t1=threading.Thread(target=A,args=(5,2,"thread 2"))
# t1.start()

"""set name"""
# import threading
# import time

# def display(x):
#     for i in range(5):
#         time.sleep(0)
#         print(threading.current_thread().getName())
#         print("thread started")
  
# for p in range(5):
#     t=threading.Thread(target=display,args=(p,))
#     t.setName("Thread#"+str(p))
#     t.start()

"""alive"""
# import threading
# import time

# def display(s):
#     time.sleep(s)
#     return 
# t=threading.Thread(target=display,args=(2,),name="threading 1")
# t1=threading.Thread(target=display,args=(2,),name="thread2")
# t.start()
# t1.start()

# for x in range(5):
#     time.sleep(x+0.5)
#     print(time.ctime(),t.name,t.is_alive())
#     print(time.ctime(),t1.name,t1.is_alive())

"""daemonthread"""
# import threading
# import time

# def a():
#     print("thread 1 started")
#     time.sleep(2)
#     print("thread 1 finished")
# def b():
#     print("threading2 started 2")
#     print("threading2 finished 2")

# t=threading.Thread(target=a,daemon=True)
# t2=threading.Thread(target=b)
# t.start()
# t2.start()

# t.join()
# t2.join()

"""current threa"""

# import threading
# import time
# def a():

#     print("threadingstart")
#     print(threading.current_thread())
#     time.sleep(5)
# for i in range(5):
#     t1=threading.Thread(target=a)
#     t1.start()
#     time.sleep(2)

# print(threading.enumerate())
# print(threading.active_count())

# i=0
# while i<10:
#     print(i)
#     i=i+2

#     "alpha":[20,30,40],
#     "beta":[80,50,70],
# }

# for i in a.values():
#     s= sum(i)/len(i)
#     t=float(s)
#     print(t)


# b=[3,4,5,6]
# a=[3,4,5,6]
# print(b)
# a.sort(reverse = True)
# print(a)

# a=[3,4,5,6]
# count=1
# for i in a:
#     b=a[-count]
#     count=count+1
#     c=str(b)*i
#     print(c)
   


#INTERVIEW qUESTION

# def func(n):
#     ones=["","one","two","three","four","five","six","seven","eight","nine"]
#     teens=["","ten","eleven","twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]




