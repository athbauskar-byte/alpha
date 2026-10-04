snacks=['pizza','shawarma','burger','franky']
for snack in snacks:
    print('current snack:',snack)                       #for loop in list
lst=list(range(0,5))
print(lst)
for i in range(0,5,2):                                 #the 2 represent gap between consecutive numbers/elements.
    print(i)
numbers=[1,2,3,4,5]                                     #sum of numbers in list
sum=0
for num in numbers:
    sum+=num
print(sum)
getsum=[i+2 for i in numbers]
print(getsum)                                           #list comprehension. prints modified list with every element increased by 2.
getsum2=[i+2 for i in numbers if i<5]
print(getsum2)                                          #list comprehension. prints modified list with every element increased by 2 with a condition where 5 is not included now.

#Finding factorial:
factorial=1
num=int(input('Enter number:'))
if num<0:
    print('number should be positive')
elif num==0:
    print('factorial=',factorial)
else:
    for i in range(1,num+1):
        factorial*=i
    print(factorial)

#Contrtol Statements
#"Continue"
names=['Rishu','Ayush','Ram','Nalla','Pappa']           #"Continue" goes back to the loop continuing while skiping the next line.
for i in names:
    if len(i)==3:
        continue
    else:
        print('My name is:',i)

#"Pass"
names=['Rishu','Ayush','Ram','Nalla','Pappa']           #"Pass"; passes it and nothing happens; the code runs to the next line
for i in names:
    if len(i)==3:
        pass
    else:
        print('My name is:',i)

#"Break" 1
names=['Rishu','Ayush','Ram','Nalla','Pappa']           #"Break"; Completely breaks the loop and code stops running.
for i in names:
    if len(i)==3:
        break
    else:
        print('My name is:',i)

#"Break" 2
numbers=[1,3,5,6,7,8,9]
for x in numbers:
    if x%2==0:
        print('it consists of even numbers')
        break
    else:
        print('it consists of odd numbers')

#"Enumerate"
list1=['lol1','lol2','lol3','lol4','lol5','lol6','lol7']        #it displayes the element with it's index number
list2=list(enumerate(list1))
print(list2)

for i,j in list2:
    print('on index number:',i,';The element is:',j)

#Alternative
list3=['lol7','lol6','lol5','lol4','lol5','lol6','lol7']
for i,j in enumerate(list3):
    print('On index number:',i,';The element is:',j)