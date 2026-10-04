#Functions
#1
def greet():                              #defining a function
    print("yo wassup man")

greet()                                   #calling it out
greet()
greet()

#2
def profile(name,age,salary):                #function defines with arguements
    print('your name is:',name,',your age is:',age,'and your salary is:',salary)

profile('Atharva',18,100000)

#3
def add(a,b):                              #function definition with a return value
    return a+b

c=add(20,50)
print(c)

#4
def Area_of_rectangle(Width,Height):
    return Width*Height

print(Area_of_rectangle(Width=50,Height=20))

#Arguement predefiened functions
#1.
def say(msg,time=1):                    #As time is already defines the msg is wrote ones.
    print(msg*time)
say('hello')

say('ssup man\n',5)                     #This time the value overwrites for 'time' and print the msg 5 times.

#2.
def prnum(a,b=5,c=6):
    print('a is:',a,'b is:',b,'c is:',c)

prnum(10)                               #b and c are already defined so no need to call them
prnum(10,c=9)                           #changing c with a different number
prnum(10,c=46,b=78)                     #changing both b and c with a different number

#Global variable vs Local variable
x=50                                    #Assigning a global variable
def global_vs_local(x):
    print('x is:',x)                    #prints the value assigned to x before

    x=2                                 #global variable changed the local variable inside the function which will be printed only if we call the function
    print('global changed to local inside the function i.e.:',x)        #The output changes

global_vs_local(x)

print('but x is still:',x,'outside the function')                #Outside the function the variable value is still 50

#Multiple arguements using a '*' and for loop
def func1(*arg):                                                 #Defining function using '*' and arguement name
    for i in arg:                                                #for loop
        print(i)
func1('lol1','lol2','lol3','lol4','lol5','lol6')                 #calling of function with infinite multiple arguements

#Multiple areguements in a key-value pair using '**' and for loop
def func2(**data):                                              #defining function using '**' and arguement name
    print(type(data))                                          # data type is dictionary
    for x,y in data.items():                                       #using .items() function to access the items inside the dictionary
        print(x,'is',y)

func2(Name='Atharva Bauskar',Branch='Computer Science',Div=3,CGPA=8,Class_no=103)         #Calling the function

#Combining Every Condition
def func3(initial,*midnum,**keywords):
    count=initial
    for num in midnum:
        count+=num
        for value in keywords:
            count+=keywords[value]
    print(count)
func3(50,10,20,30,lol1=20,lol2=30,lol3=40)