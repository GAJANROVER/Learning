import sys
#
# print(sys.version)
#
# # Python uses indentation to indicate a block of code.
#
# # This also comment
# """This is a comment
# written in
# more than just one line"""
#
# # if 5 > 2:
#     # print('hey gajan')
#     # print('poda')
#
# # -------------- variables
# # Python has no command for declaring a variable.
# # A variable is created the moment you first assign a value to it.
# x = 5
# # print(x)
#
# y = int(3)  #If you want to specify the data type of a variable, this can be done with casting.
# # print(type(y))  # You can get the data type of a variable with the type() function.
#
# """
# ----------- Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords. """
#
#
# # Camel Case
# # Each word, except the first, starts with a capital letter:
# # myVariableName = "John"
# #
# # # Pascal Case
# # # Each word starts with a capital letter:
# # MyVariableName = "John"
# #
# # # Snake Case
# # # Each word is separated by an underscore character:
# # my_variable_name = "John"
# #
# # # Many Values to Multiple Variables
# # # Python allows you to assign values to multiple variables in one line:
# # x, y, z = "Orange", "Apple", "Banana"
# # # print(x)
# # # print(y)
# # # print(z)
# #
# # # One Value to Multiple Variables
# # # And you can assign the same value to multiple variables in one line:
# # x = y = z = "Orange"
# # # print(x, y ,z)
# #
# # g = 'hey'
# # # print(g, x)
# #
# # # Global Variable
# # # If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
# # # To create a global variable inside a function, you can use the global keyword.
# # # def myFunc():
# # #     global a
# # #     a = 'developer'
# # #     g = 'gajan'
# # #     print(g + ' gtr')
# # #
# # # myFunc()
# # #
# # # print(g + ' gajan')
# # # print(g + " " +  a)
# #
# # # Data Types
# # x= 5
# # y = 1j
# # z = 3+5j
# # zz = -5j
# # f = 2.9
# # y = int(2.9)
# # x = float(1)
# # x = str("s1")
# # a = 'hey gajan'
# #
# # # print(a[0])
# # # for x in a:
# # #     print(x)
# #
# # # print("gajan1" in a)
# #
# # # F-Strings
# # # we can combine strings and numbers by using f-strings or the format() method!
# # # age = 29
# # # txt = f'my age is {age}'
# # # print(txt)
# #
# # # if(2==2) & (3==3):
# # #     print(True)
# # # else:
# # #     print(False)
# #
# # # ----------- list
# # thislist = ["apple", 34, True]
# # tropical = ["mango", "pineapple", "papaya"]
# # # print(type(thislist))
# # # print(thislist[-3 : -1])
# # # if "apple" in thislist:
# # #     print("yes")
# #
# # # thislist.extend(tropical)
# # # print(thislist)
# #
# # # loop in list
# # thislist = ["apple", "banana", "cherry", "orange"]
# # # for x in thislist:
# # #     print(x)
# #
# # # print(len(thislist))
# #
# # # Looping Using List Comprehension
# # # List Comprehension offers the shortest syntax for looping through lists:
# # # [print(x) for x in thislist]
# #
# # # copy list
# # # thislist1 = thislist.copy()
# # # thislist2 = thislist[:]
# # # print(thislist2)
# #
# #
# # # ----- tuples
# # # To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# # thistuple = ("apple", "orange", "banana", "cherry", "cherry")
# #
# # # To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# # thistuple1 = ("apple",)
# # print(thistuple1)
#
# #
# # if "apple" in thistuple:
# #     print("yes")
#
# # for x in thistuple:
# #     print(x)
#
#
#
# # ----- Sets
# # thisset = {"apple", "banana", "cherry"}
# # thisset2 = {"google", "microsoft", "apple"}
# # # print("apple" in thisset)
# #
# # # Once a set is created, you cannot change its items, but you can add new items.
# # thisset.add("orange")
# # thisset.update(["orange", "mango", "grapes"])
# # thisset.remove("banana") # Note: If the item to remove does not exist, remove() will raise an error.
# # thisset.discard("banana") # Note: If the item to remove does not exist, discard() will NOT raise an error.
#
# # for x in thisset:
# #     print(x)
#
# # Keep ONLY the duplicates
# # The intersection() method will return a new set, that only contains the items that are present in both sets.
# test1 = thisset.intersection(thisset2)
# # print(test1)
#
# # --- Dictionaries
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# # print(thisdict.keys())
# # for x in thisdict:
# #     print(thisdict[x])
#
# # for x in thisdict.values():
# #     print(x)
#
# # Loop through both keys and values, by using the items() method:
# # for x, y in thisdict.items():
# #     print(x, y)
#
# # nested dictionaties
# # myfamily = {
# #   "child1" : {
# #     "name" : "Emil",
# #     "year" : 2004
# #   },
# #   "child2" : {
# #     "name" : "Tobias",
# #     "year" : 2007
# #   },
# #   "child3" : {
# #     "name" : "Linus",
# #     "year" : 2011
# #   }
# # }
# #
# # for x,obj  in myfamily.items():
# #     print(x)
# #
# #     for y in obj:
# #         print(y + " : " , obj[y])
#
#
#
# # IF ELSE
#
# a = 34
# b = 33
# # if b > a:
# #   print("b is greater than a")
# # elif a == b:
# #   print("a and b are equal")
# # else :
# #   print("a is greater than b")
#
# # print("A") if a > b else print("B")
#
# # ------------- function
#
# # def myfunction():
# #   print("hello I am software engineer")
# #
# # myfunction()
#
#
#
# # def tri_recursion(k):
# #   if(k > 0):
# #     result = k + tri_recursion(k - 1)
# #     print(result)
# #   else:
# #     result = 0
# #   return result
# #
# # print("Recursion Example Results:")
# # tri_recursion(6)
#
# # Python Lambda
#
# # x = lambda a : a + 15
# # print(x(10))
#
# # def myfunc(n):
# #   return lambda a : a * n
# #
# # mytripler = myfunc(3)
# #
# # print(mytripler(11))
#
#
#
#
# #If you want to print multiple words on the same line, you can use the end parameter:
# # print("Hello World!", end="-")
# # print("I will print on the same line.")
#
# # You can combine text and numbers in one output by separating them with a comma:
# # print("hey", "I am", "Gajan", 29, "years old")
#
# # x = int(3)
# # print(type(x))
#
# # x, y,z = ["apple", "banana", "cherry"]
# # print(y)
#
# # To create a global variable inside a function, you can use the global keyword.
# # def myfunc():
# #   global x
# #   x = "fantastic"
#
# # myfunc()
#
# # print("Python is " + x)