#PYTHON learning running notes
#1. Variable name
num lol= 10          #gives an error because of the space in the variable name
num$=5               #gives an error because of the special character '$' in the variable name
5num=15              #gives an error because variable name cannot start with a number
num_lol=20           #valid variable name with underscore and not space
car2s=30             #valid variable name with number at the end

#2. Variable assignments
new_car='car'          #assigning a string value to a variable
new_vehicle="vehicle"  #assigning a string value to a variable using double quotes
new_number=100             #assigning an integer value to a variable
alpha=hi               #gives an error because 'hi' is not defined as a string (missing quotes)
a=10;b=5               #assigning multiple variables in a single line using semicolon

#3. Operators
x=10;y=20
z=x+y               #addition operator
z+=x               #increment operator: it is an alternative to z=z+x
z-=y               #decrement operator: it is an alternative to z=z-y
#Every other operator like *, /, %, **, // can also be used in the same way as above
#Python follows PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction) order of operations.

#4. Membership operators
print("car" in new_car)      #returns True because 'car' is present in the string 'new_car'
print("bike" not in new_vehicle)  #returns True because 'bike' is not present in the string 'new_vehicle'
print("y" in new_number)      #returns False because 'y' is not present in the integer value of 'new_number'
print("P" in "Pushpa")        #returns True because 'P' is present in the string 'Pushpa'
print("p" in "Python")        #returns False because 'p' is not present in the string 'Python'. Python is case-sensitive.
Python is python              #returns False because 'Python' is not equal to 'python'. Python is case-sensitive.
print(1 is 1)                #returns True because both are the same object
#while using "is" operator, both the strings or objects should be exactly the same, including case sensitivity.
print("hi hello" is not "hello hi")  #returns True because both strings are not the same, including case sensitivity.

#4. String operations
beginner='Python is a programming language. It is widely used for web development, data analysis, artificial intelligence, and more. Python is known for its simplicity'
print(beginner,'\n')  #prints the string value of the variable 'beginner' followed by a new line just to increase readability. It gives space between the string so that it looks clean.
print('datatype is',type(beginner))  #prints the datatype of the variable 'beginner' which is a string
print(len(beginner))  #prints the length of the string value of the variable 'beginner'. Displays a number which is the total number of characters in the string including spaces and punctuation marks.
print(beginner[0])  #prints the first character of the string value of the variable 'beginner' which is 'P'. Indexing starts from 0.
print(beginner[3])  #prints the fourth character of the string value of the variable 'beginner' which is 'h'. Indexing starts from 0.
print(beginner[-1]) #prints the last character of the string value of the variable 'beginner' which is 'y'. Indexing starts from 0.
#This is known as indexing.

print(beginner[2:8]) #prints the characters from index 2 to index 7 of the string value of the variable 'beginner' which is 'thon i'. The character at index 8 is not included.
print(beginner[-8:-1]) #prints the characters from index -8 to index -2 of the string value of the variable 'beginner' which is 'simplici'. The character at index -1 is not included.
#This is known as slicing.
print(len('name')) #prints the length of the string 'name' which is 4. It counts the number of characters in the string.

var1='Hello World!'
print(var1+'Python') #prints the concatenation of the string value of the variable 'var1' and the string 'Python' which is 'Hello World!Python'. It combines both strings into one.
print(var1[:6]+'Python') #prints the concatenation of the first 6 characters of the string value of the variable 'var1' and the string 'Python' which is 'Hello Python'. It combines both strings into one.
#This is known as string concatenation. It combines two or more strings into one string.

print('Hello \nWorld') #prints the string 'Hello' followed by a new line and then the string 'World'. The '\n' is an escape character that represents a new line.

c='atharva'
print(c.center(30))    #prints the string value of the variable 'c' centered in a string of length 30. It adds spaces on both sides of the string to center it.
print(len(c.center(50)))
print(c.rjust(20))      #prints the string value of the variable 'c' right-justified in a string of length 20. It adds spaces on the left side of the string to right-justify it.
print(c.ljust(20))      #prints the string value of the variable 'c' left-justified in a string of length 20. It adds spaces on the right side of the string to left-justify it.
lol="aeiouaeiouaeiouaeiou"
print(lol.count("a",7,20))  #prints the count of the character 'a' in the string value of the variable 'lol' from index 7 to index 19. The character at index 20 is not included.
string='alpha123'
print(string.isalum())  #prints True because the string value of the variable 'string' is alphanumeric. It contains both letters and numbers.
print(string.isalpha())  #prints False because the string value of the variable 'string' is not alphabetic. It contains both letters and numbers.
print(string.isnum())  #prints False because the string value of the variable 'string' is not numeric. It contains both letters and numbers.
string2='aplha romeo'
print(string2.isalnum())  #prints False because the string value of the variable 'string2' is not alphanumeric. It contains a space which is not a letter or a number.
str1='ATHarva'
print(str1.captialize())  #prints the string value of the variable 'str1' with the first character capitalized and the rest of the characters in lowercase which is 'Atharva'.
print(str1.upper())  #prints the string value of the variable 'str1' in uppercase which is 'ATHARVA'.
print(str1.lower())  #prints the string value of the variable 'str1' in lowercase which is 'atharva'.
print(str1.swapcase())  #prints the string value of the variable 'str1' with the case of each character swapped which is 'athARVA'.
str2='you are a good boy. I am proud of you. \nYou have done a great job.'
print(str2.replace('you','I'))  #prints the string value of the variable 'str2' with all occurrences of the substring 'you' replaced with the substring 'I'. It replaces all occurrences of 'you' with 'I'.
print(str2.split())  #prints the string value of the variable 'str2' split into a list of substrings using whitespace as the delimiter. It splits the string into a list of words.
print(str2.split(' ',1))  #prints the string value of the variable 'str2' split into a list of substrings using whitespace as the delimiter, but only splits at the first occurrence of whitespace.
print(str2.split(' ',5))

#5. Lists
list1=[1,'lolbro',5.5,True,3+5j,[1,'nobro',7.89,False]]  #creates a list with different data types including an integer, a string, a float, a boolean, and another list. Lists can contain elements of different data types.
print(list1)
print(list1[5])
print(list1[1])
print(list1[5][2])  #prints the third element of the list of the nested list. It accesses the nested list and retrieves the value at index 2.
print(list1[1:3])   #prints the elements of the list from index 1 to index 2. The element at index 3 is not included. It retrieves a sublist from the original list.
list1[2]=6.5  #modifies the value of the element at index 2 of the list to 6.5. It updates the value of the list at the specified index.
print(list1)
list2=['a','bc','deg',4,5,6.3,True,[1,2,3,'r']]
list2.append('new')  #adds the string 'new' to the end of the list. It modifies the original list by adding a new element.
print(list2)
list2.pop()  #removes the last element from the list. It modifies the original list by removing the last element.
list2.pop(0) #removes the first element from the list. It modifies the original list by removing the element at index 0.
print(list2)
list2.insert(0,'new')
list2.insert(3,'new2')  #inserts the string 'new2' at index 3 of the list. It modifies the original list by adding a new element at the specified index.
list3=['j','k','l',8,9,10]
list2.append(list3)  #adds the list 'list3' to the end of the list. It modifies the original list by adding a new element which is another list.
print(list2)
list2.extend(list3)  #adds the elements of the list 'list3' to the end of the list. It modifies the original list by adding multiple new elements which are not the list this time.
print(list2)
#.extend vs .append:
#.append adds its argument as a single element to the end of a list. The length of the list itself will increase by one, regardless of how many elements are in the argument.
#.extend iterates over its argument adding each element to the list, extending the list. The length of the list will increase by however many elements were in the iterable argument.
list2.reverse()  #reverses the order of the elements in the list. It modifies the original list by reversing the order of its elements.
print(list2)
list4=[5,3,9,7,8,1,4,8,6,9,3,2,1,4,5,7,8,9,0]
list4.sort()
print(list4)
print(list4.count(9))  #prints the count of the number of occurrences of the element 9 in the list. It counts how many times the specified element appears in the list.
print(list4.index(7))  #prints the index of the first occurrence of the element 7 in the list. It retrieves the index of the specified element in the list.
list5=list4+list3  #prints the concatenation of the list 'list4' and the list 'list3'. It combines both lists into one list.
print(list5)
list6=[1,2,3,4,5,6,7,8,9]
print(list6*2)  #prints the concatenation of the list 'list6' with itself. It repeats the elements of the list twice.
tup1=('a','b','c',1,2,3,4.5,True,[1,2,3]) #tuples are immutable.
tup1=(1,2,3,4,5,6,7,8,9)     #But you can reassign a new tuple to the same variable name. It creates a new tuple and assigns it to the variable 'tup1'.
tup1[0]=10               #gives an error because tuples are immutable. You cannot change the value of an element in a tuple once it is created.
print(tup1[1:5])         #All those operations which are valid for lists are also valid for tuples except for those which modify the tuple.
del(tup1)                  #deletes the entire tuple. It removes the variable 'tup1' from memory.

#5. Sets
set1={1,2,3,4,5,6,7,8,9}  #creates a set with unique elements. Sets are unordered collections of unique elements.
set2=set(['a','b','c',5,6,7,8])  #creates a set from a list. It converts the list into a set, removing any duplicate elements.
print(set2)
list7=[4,4,5,5,6,6,7,7,8,8,9,9]
set3=set(list7)  #creates a set from a list. It converts the list into a set, removing any duplicate elements.
print(set3)
intersection_set=set1.intersection(set2)  #creates a new set with the common elements of set1 and set2. It finds the intersection of the two sets.
print(intersection_set)
union_set=set1.union(set2)    #creates a new set with all the elements existing in both the sets. Takes union of 2 sets
print(union_set)
set3.clear()
print(set3)

#6. Dictionaries
dict1={'name':'Atharva','Age':18,'Bike':'Splendor'}
print(dict1['name'])
dict1['School']='SSDPS'
dict1['name']='Bauskar'
print(dict1)
print(dict1.values())
print(dict1.keys())
print(dict1.items())
dict2={'k1':'lolbro','k2':[1,2,3,4,5],'k3':{'inside_key':'nobro','inside_key2':'okbro'}}  #nested dictionary
print(dict2['k3']['inside_key2'])
