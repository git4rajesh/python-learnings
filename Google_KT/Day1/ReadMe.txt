To Do:
a. Modules and using different calls.
b. PEP8 


Read Eval interpreter in Python

A

2. NameError : name A is not defined


a = 'Hello' +6

3. TypeError

4.Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    wrk14 = Wrk14()
    comp = wrk14.compare()
	
	The reason that the if __name__ == "__main__": block is called boilerplate in this case is that it replicates a functionality that is automatic in many other languages. In Java or C++, among many others, when you run your code it will look for a main() method and run it, and even complain if it's not there. Python runs whatever code is in your file, so you need to tell it to run the main() method; a simple alternative would be to make running the main() method the default functionality
	
5. ARGV in Python		
		
import sys

print(sys.argv)	

6. To get all the methods in the module.	
a. dir(sys) 
b. help(sys)

7. Google standards is 2 spaces indentation

8. Logical Connectors in Python are Letters say "or" , "and"

9. num = 0
	if(num) --> False
 num = 5
    if(num) --> True

0 number is boolean False and any other value is True.
"" Empty string is boolean False and any other value is True

10. Python only checks the line, when it runs the line. So we can very well call a method() without having to define it in else-part.

11. a = "isn't" or a = 'isn"t' . Both correct  but single quote is Pythonic way.

12. String functions:
	string = 'Hello'
	string.find('e') returns 1 (The index of e)
	
13. What are unicode strings


14. Concatenating a String:
	
	>>> str1 = 'Hello %s %s' % ('there','\n')
	>>> str2 = 'How are %s %s' % ('you', '\n')
	>>> print(str1 + str2)
		Hello there 
		How are you 



14. Slicing a String
		string = 'Hello'
		string[1:3] = el (starts from index 1 and ends at 2. 3 is not included)
		string[0:] = Hello
		string[:2] = He
		
		
		
		
		
		
15. Negative indexing of a String
			
			string = 'Hello'
			string[-1] ='o'
			string[-5] = 'H'
			
			
16. None is the null value in Python			
			
16. A list can be Hetrogeneous	

			my_list = [1,2,'Ram']
			
17. A list can be concatenated as below:
				>>> a = [1,2,3]
				>>> b =[5,6]
				>>> c = a + b
				>>> c
				[1, 2, 3, 5, 6]
				
18. Reference Copy of a List:
	========================
	a =[1,2,3]
	b = a
	Now both b and a refers to that list.
	This can be checked by
	a[1] ='a'
	print(b)
	[1,'a',3]
	
	So in Python when u do a copy, its just a Reference Copy.
	
19. Physical copy of a List:
	======================
	a = [1,2,3]
	b = a[:]
	
    b[1] = 'a'
    print(b)
	[1, 'a', 3]
	print(a)
	[1, 2, 3]
			
20. Value in List:
	=============
	
	var =14
	a = [1,2,3]
	
	if var in a:
		print ("Present")
	else:
		print('Not Present')
		
		
	o/p : Not Present

21. Appending a List:
	================
	
	>>> a
	[1, 2, 3]
	>>> a.append("I")
	>>> a
	[1, 2, 3, 'I']
	
	
22.Shouldnt append like this:
   ==========================
	a = [1,2]
	a = a.append(3)
	
	print(a)
	
	This gives None

22. Pop an element from a List:
	==========================
		>>> a =[1,2,3]
		>>> a.pop()
		3
		>>> a
		[1, 2]
		
		a.pop(0)
		a
		[2]
		
		So from a list we can pop an element from both begining and end. 
		If just pop(), it removes the element from end . If a subscript is given, it pops the element at that index.
		>>> a
			[1, 2, 3]
		>>> a.pop(1)
			2
		>>> a
		[1, 3]
		
23. Delete :
	--------
	a =10
	del a
	
	del can be used in List and Dictionary too
	
24. Sorting:
	--------
	>>> a = [6,5,4]
	>>> sorted(a)
	[4, 5, 6]
	>>> a
	[6, 5, 4]


	>>> sorted(a)
	[1, 2, 4, 6]
	>>> sorted(a,reverse=False)
	[1, 2, 4, 6]
	>>> sorted(a,reverse=True)
	[6, 4, 2, 1]
	
	
25.Custom sorting in Python:
----------------------------


Providing key function which is a 1-arguement function.

>>> my_lst = ['aaa','c','bb','dddd']
>>> sorted(my_lst,key=len)
	['c', 'bb', 'aaa', 'dddd']
	
	
Example 2: To sort a list based on last character in it
	my_lst = ['aaz','c','bb','dddd']
	
	>>> def last_char(string): return string[-1]


 op = sorted(my_lst, key=last_char)
 print(op)
 ['bb', 'c', 'dddd', 'aaz']
 
 
 
 26. JOIN
 --------
 ex1:
	>>> '1'.join(op)
	'bb1c1dddd1aaz'
	
ex2:
	>>> op
	['bb', 'c', 'dddd', 'aaz']
	>>> '-end'.join(op)
	'bb-endc-enddddd-endaaz
	
	
27.SPLIT:
---------

ex1. str.split(',')	

28. We cant modify a list when we are looping through the list.

29. We can put a tupule into a list as below

 my_lst = [(1,a),(2,b),(3,c)]
 
 
30. Dictionary:

KeyError: got when we look for key thats not there in a dictionary

31.File handling and suppresing the new line:

a) Reading file line by line

f = open(filename, 'rU')
The 'U' here sorts out dos or unix files

for line in f:
	print(line,)
	
f.close()	
	The trailing ',' suppresses the new line.
	
	
32. readlines()
b. Reading file as list of lines
f = open(filename,'rU')

lines = f.readlines()

The whole file is read as List of lines	

33. Reading files as one single String:

	file_string = f.read()
	
34. Use sys.exit(0) or return often while coding.This helps in checking the code before continuing further.

35. Use Doc String inside a Class or a Function:
Optional documentation string (docstring) to describe what the function does

def greet(name):
   """This function greets to the person passed in as
   parameter"""
   print("Hello, " + name + ". Good morning!")
   

36. A function can return None.

37.global variables using the keyword global.

38. Default Arguments:
	def greet(name, msg = "Good morning!"):
	
39. Keyword Arguments:
		greet(name = "Bruce",msg = "How do you do?")    # 2 keyword arguments
		
40. Arbitrary Arguments:
			def greet(*names):
   """This function greets all the person in the names tuple."""
   
   greet("Monica","Luke","Steve","John")
			These arguments get wrapped up into a tuple before being passed into the function. Inside the function, we use a for loop to retrieve all the arguments back.
			
41. Python Modules:
				
	
	
 
 
	
		
