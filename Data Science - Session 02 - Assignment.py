"1."
# print("\n1. Write a Python program which accepts the user's first and last name and prints them in reverse order with a space between them.")
# first_name = input("First name: ")
# last_name = input("Last name: ")
# print(last_name,first_name)

"2."
# print('\n2.  Write a Python program which accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.')
# user_data = input("Enter sequence of comma-separated numbers: ")
# user_data = user_data.split(', ')
# user_list = list(user_data)
# user_tuple = tuple(user_data)
# print('List : ',user_list)
# print('Tuple : ',user_tuple)

"3."
# print('\n3. Write a Python program to display the first and last colours from the following list.')
# color_list = ["Red", "Green", "White", "Black"]
# print(color_list)
# print('First color :',color_list[1],'\n' 'Last color :',color_list[-1])

"4."
# import builtins
# print("\n4. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).")
""" print(abs(-34))
    print(abs.__doc__)   """
# help(builtins.abs)

# print(builtins.abs(-34))

"5."
# print('\n5. Write a Python program to print the calendar of a given month and year.')
# import calendar
# year = int(input("Input the year : "))
# month = int(input("Input the month : "))
# print(calendar.month(year, month))

"6."
# print('\n6. Write a Python program to calculate number of days between two dates.')
# from datetime import date

# ay_1 = input("Enter first date in (yyyy, m, d): ")
# ay_2 = input("Enter second date in (yyyy, m, d): ")

# ay_1_value = ay_1.split(', ')
# ay_2_value = ay_2.split(', ')
# ay_1_list = list(ay_1_value)
# ay_2_list = list(ay_2_value)

# for ate in range(0, len(ay_1_list)):
# ay_1_list[ate] = int(ay_1_list[ate])

# for ate in range(0, len(ay_2_list)):
# ay_2_list[ate] = int(ay_2_list[ate])


""" y_1 = day_1_list[0]
    m_1 = day_1_list[1]
    d_1 = day_1_list[2] """

"from datetime import date"
# day_1 = date(ay_1_list[0], ay_1_list[1], ay_1_list[2])
# day_2 = date(ay_2_list[0], ay_2_list[1], ay_2_list[2])

# day = day_2 - day_1

# print("The number of days are: ",day.days)

"7."
# print('\n7. Write a Python program to check whether a specified value is contained in a group of values.')
# l = [1,5,8,3]
# value = int(input('Enter a value to check: '))
# if value in l:
# print('True')
# else :
# print('False')
# value = int(input('Enter a value to check: '))
# if value in l:
# print('True')
# else :
# print('False')

"8."
# print('\n8. Write a Python program to create a histogram from a given list of integers.')
# l = input('List: ')
# l = l.split(',')
# list = list(l)
# for l in range(0,len(list)):
# list[l] = int(list[l])

# print('_' * max(list) + '_______')
# for l in range(0,len(list)):
# print('|'+'=' * list[l] + ']', list[l])
# print('|')

"9."
# print('\n9. Write a Python program to concatenate all elements in a list into a string and return it.')
# list_u = list(input('List: ').split(','))
# for l in range(0,len(list_u)):
#     list_u[l] = str(list_u[l])

# print('List in string: ',list_u)

"10."
# print('\n10. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.')

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# print('color_list_1: ',color_list_1,'\n' 'color_list_2: ',color_list_2)
# print("\nDifferenct of color_list_1 and color_list_2:")
# print('By color_list_1.difference(color_list_2)',color_list_1.difference(color_list_2))

# print("\nDifferenct of color_list_1 and color_list_2:")
# print('By color_list_1 - color_list_2',color_list_1 - color_list_2)

"11."
# print('\n11. Write a Python program to check whether a file exists.')
# import os.path
# file_path = input('File path: ')
# file_exists = os.path.exists(file_path)

# print(file_exists)

"12."
# print('\n12. Write a python program to call an external command in Python.')
# import os
# commond = input('Write your external commond: ')
# print(os.system(commond))

"13."
# print('\n13. Write a Python program to find out the number of CPUs using.')
# import multiprocessing
# print('import multiprocessing \nprint(multiprocessing.cpu_count()):', multiprocessing.cpu_count())

"14."
# print('\n14. Write a Python program to list all files in a directory in Python.')
# from os import listdir
# print("from os import listdir \nprint (listdir('File path name'))")
# print (listdir('E:\Shubham\Desktop\AI-ML\Coffeee Data Science Bootcamp - 0001'))

"15."
# print('\n15. Write a python program to access environment variables.')
# import os
# for data in os.environ:
#    print(data)
#    print('-'*10)
#    print(os.environ[data])
#    print('='*20+'>')

"16."
# print('16. Write a Python program to get the current username')
# print('''import os
# print(os.environ.get('USERNAME'))''')
# import os
# print(os.environ.get('USERNAME'))

"17."
# print('\n17. Write a program to get execution time for a Python method.')
# import time
# start_time = time.time()
# t = 0
# for i in range(1,10):
# t = t + i
# print(t)
# end_time = time.time()

# print('Exicution time:{:.5f}'.format(end_time-start_time) )
# print('Exicution time:',end_time-start_time, 'seconds')

"18."
# print('\n18. Write a Python program to get an absolute file path.')
# print('''import os
# absolute_file_path = os.path.abspath('.gitattributes')
# print("Absolute file path: ",absolute_file_path)''')
# import os
# absolute_file_path = os.path.abspath('.gitattributes')
# print("Absolute file path: ",absolute_file_path)

"19."
# print('\n19. Write a Python program to get file creation and modification date/times.')
# import os.path, time
# file_name = '.gitattributes'
# print("File name:", file_name)
# print("Last modified:", time.ctime(os.path.getmtime(file_name)))
# print("Created:", time.ctime(os.path.getctime(file_name)))

"20."
# print('\n20. Write a Python program to sort three integers without using conditional statements and loops.')
# int_list = input('Enter 3 integers(n,n,n): ')
# int_list = int_list.split(',')
# for l in range(0,len(int_list)):
# int_list[l] = int(int_list[l])
# int_list.sort()
# print('Sorted list:',int_list)

"21."


"22."
# print('\n22. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.')
# import sys
# print("This is the name/path of the script:"),sys.argv[0]
# print("Number of arguments:",len(sys.argv))
# print("Argument List:",str(sys.argv))

"23."
# print('\n23. Write a Python program to find the available built-in modules.')
# import sys
# module_name = ', '.join(sys.builtin_module_names)
# print(module_name)

"24."
# print('\n24. Write a Python program to get the size of an object in bytes.')
# import sys
# obj = 7
# size = sys.getsizeof(obj)
# print('object: ', obj)
# print('Size of the object is:', size)

"25."
# print('\n25. Write a Python program to get the current value of the recursion limit.')
# import sys
# print("Current value of the recursion limit:", sys.getrecursionlimit())

"26."
# print('\n26. Write a Python program to count the number occurrence of a specific character in a string.')
# string = "Write a Python program to count the number occurrence of a specific character in a string."
# print("String:", string)
# char = input('Enter the character to count the number occurrence of it in the given above string: ')
# print(f"The number of '{char}' in the above string is:",string.count(char))

"27."
# print('\n27. Write a Python program to get the system time.')
# import datetime
# print("The systen time is:", datetime.datetime.now().time())

"28."
# print('\n28. Write a Python program to clear the screen or terminal.')
# import os
"os.system('cls')"
# print('''import os
# os.system('cls')''')

"29."
# print('\n29. Write a Python program to get the name of the host on which the routine is running.')
# print('''import socket
# host_name = socket.gethostname()
# print("Host name:", host_name)''')
# import socket
# host_name = socket.gethostname()
# print("Host name:", host_name)

"30."
# print("\n30. Write a Python program to access and print a URL's content to the console.")
# import requests
# data = requests.get('https://example.com')
# print(data.text)

"""Python Data Structure
        Array:  An array is a vector containing homogeneous elements i.e. belonging to the same data type."""

# "1."
print('\n1. Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.')
# 
ar = [1,2,3,4,5]
print('array:',ar)
print('array items:')
for elements in range(0, len(ar)):
    print(ar[elements])
# 
inx = int(input("Enter the index you want to access form the array: "))
print(ar[inx])
# 
# 
# "2."
print('\n2. Write a Python program to reverse the order of the items in the array.')
# 
ar = [1,2,3,4,5]
print('array:',ar)
ar.sort(reverse= True)
print('Reverse ordered array:',ar)
# 
# "3."
# 
print('\n3. Write a Python program to get the number of occurrences of a specified element in an array.')
ar = [2,3,3,4,2,5,8,2,9,4,7]
print('array:',ar)
ele = int(input('Enter the element to count the number occurrence of it in the given above string : '))
print(f"The number of {ele}'s present in array :",ar.count(ele))
# 
# "4."
print('\n4. Write a Python program to remove the first occurrence of a specified element from an array.')
ar = [2,4,1,5,8,9]
print('array:',ar)
ele = int(input('Enter the element you want to remove from the above array: '))
if ele in ar:
    ar.remove(ele)
    print('Here is the array with removed element:',ar)
else:
    print(f"'{ele}' is not in above aaray.")
# 
# 
# """     Dictionary      """
# 
# "1."
print('\n1. Write a Python script to sort (ascending and descending) a dictionary by value.')
dic = {
'key5': 'value5',
'key1': 'value1',
'key3': 'value3',
'key2': 'value2',
'key4': 'value4'
}
print('Dictionary :', dic)
sorted_dic_a = {k:v for k, v in sorted(dic.items())}
print('Dictionary value in ascending order :',sorted_dic_a)
sorted_dic_d = dict( sorted(dic.items(), reverse=True))
print('Dictionary value in descending order :',sorted_dic_d)
# 
# "2."
print('\n2. Write a Python script to add a key to a dictionary.')
dic = {0: 10, 1: 20}
print('Dictionary :', dic)
print('Update dictonary with {2: 30} ')
# dic[2] = 30
dic.update({2:30})
print('Updated dictonary :',dic)
# 
# "3."
print('\nWrite a Python script to concatenate following dictionaries to create a new one.')
dic = {}
print('Dictonary:',dic)
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic.update(dic1)
dic.update(dic2)
dic.update(dic3)
print('''dic1 = {1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}''')
print('Concatenated dictonary:',dic)
# 
# "4."
print('\n4. Write a Python program to iterate over dictionaries using for loops.')
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print('Dictonary:',dic)
print('Iterated dictonary:')
for k in dic:
    print(f'{k}:',dic[k])
# 
# "5."
print('\n5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).')
dic = {}
print('n = 5')
print('Dictonary:',dic)
print('Dictonary is being updated:')
for x in range(1,6):
    if x != 5:
        dic.update({x:x*x})
        print(dic)
    else:
        dic.update({x:x*x})
        print('Updated dictonary:',dic)
# 
# "6."
print('\n6. Write a Python program to remove a key from a dictionary.')
dic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print('Dictonary:',dic)
key = int(input('Enter a key from above dictoanry that you want to remove: '))
dic.pop(key)
print('Updated dictonary:',dic)
# 
# "7."
print('\n7. Write a Python program to print all unique values in a dictionary.')
# dic = {"V":"S001", "V": "S002", "VI": "S001", "VI": "S005", "VII":"S005", "V":"S009","VIII":"S007"}
# print(dic)
# for x in range(0,len(dic)):
#     print(x,dic)
my_dic = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print('Dictonary;',my_dic)
print('Unique values:',set(value for dic in my_dic for value in dic.values()))
# 
# "8."
print('\n8. Write a Python program to create a dictionary from a string.')
string = 'w3resource'
print('String:',string)
print('Count of the letters from the string is the value of dictonary')
st_dic = {}
for i in range(0, len(string)):
    key = string[i]
    value = string.count(key)
    st_dic.update({key:value})
# 
print('Dictonary:',st_dic)
# 
# "9."
print('\n9. Write a Python program to print a dictionary in table format.')
dic = {1: ["Yash", 20, 'IT'],
         2: ["Naman", 20, 'CSE'],
         3: ["Bharat", 22, 'CSE'],
         }
# 
print("{:<7} {:<5} {}".format('NAME', 'AGE', 'BRANCH'))
# 
for key, value in dic.items():
    name, age, course = value
    print("{:<7} {:<5} {}".format(name, age, course))
# 
# 
# "10."
print(
    "\n10. Write a Python program to count the values associated with key in a dictionary."
)
# 
Sample_data = [
    {"id": 1, "success": True, "name": "Lary"},
    {"id": 2, "success": False, "name": "Rabi"},
    {"id": 3, "success": True, "name": "Alex"},
]
print('''Sample_data = [
    {"id": 1, "success": True, "name": "Lary"},
    {"id": 2, "success": False, "name": "Rabi"},
    {"id": 3, "success": True, "name": "Alex"}
    ]''')
print('Dictionaries that have success as True:',sum(d['success'] for d in Sample_data))
# 
# "11."
print('\n11. Write a Python program to convert a list into a nested dictionary of keys.')
l = [1,2,3,4,5,6,7,8,9]
n_dic = c_dic =  {}
for n in l:
    c_dic[n] = {}
    c_dic = c_dic[n]
# 
print(n_dic)
# 
# "12."
print("\n12. Write a Python program to check multiple keys exists in a dictionary.")
# 
dic = {"id": 1, "success": True, "name": "Lary"}
print("Dictonary 1:", dic)
if len(dic) > 0:
    print("Multiple keys exists in the dictionary")
dic_2 = {"id": 1}
print("Dictonary 2:", dic_2)
if len(dic_2) <= 1:
    print("Multiple keys does not exists in the dictionary")
# 
# "13."
print('\n13. Write a Python program to count number of items in a dictionary value that is a list.')
dic = {1:[1,2], 2:"2", 3:"3", 4:[1,2,3,4]}
print('Dictonary:',dic)
print("print('Number of items in a dictionary value:',sum(map(len, dic.values())))")
print('Number of items in a dictionary value =',sum(map(len, dic.values())))
# 
# 
# """     Sets      """
# 
# "1."
print('\n1. Write a Python program to create a set.')
my_set = set([1,2,3,4,5])
print(my_set)
print(type(my_set))
# 
# "2."
print('\n2. Write a Python program to iteration over sets.')
my_set = set(['a','s','d','f','g'])
print("my_set = set(['a','s','d','f','g'])")
for i in my_set:
    print(i)
# 
# "3."
print('\n3. Write a Python program to add member(s) in a set.')
my_set = set(['a','s','d'])
print("my_set = set(['a','s','d'])")
add = 1
my_set.add(add)
print(my_set)
# 
# "4."
print('\n4. Write a Python program to remove item(s) from set')
my_set = {'a', 1, 's', 'd'}
print('my_set:',my_set)
my_set.remove(1)
print(my_set)
# 
# "5."
print('\n5. Write a Python program to remove an item from a set if it is present in the set.')
my_set = set(input('Enter values : '))
remove = '2'
print("'2' will be removed")
my_set.remove(remove)
print(my_set)
# 
# "6."
print('\n6. Write a Python program to create an intersection of sets.')
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx & sety
print(setz)
# 
# "7."
print('\n7. Write a Python program to create a union of sets')
setn1 = set([1, 2, 3, 4, 5])
setn2 = set([1, 2, 3, 6, 7, 8, 9])
print("\nOriginal sets:")
print(setn1)
print(setn2)
print("\nUnion of above sets:")
setn = setn1.union(setn2)
print(setn)
# 
# "8."
print('\n8. Write a Python program to create set difference.')
setn1 = set([1, 1, 2, 3, 4, 5])
setn2 = set([1, 5, 6, 7, 8, 9])
print("\nOriginal sets:")
print(setn1,f'\n{setn2}')
print("\nDifference of setn1 - setn2:")
print(setn1.difference(setn2))
print("\nDifference of setn2 - setn1:")
print(setn2.difference(setn1))
# 
# "9."
print('\n9. Write a Python program to create a symmetric difference.')
setn1 = set([1, 1, 2, 3, 4, 5])
setn2 = set([1, 5, 6, 7, 8, 9])
print("Original sets:")
print(setn1)
print(setn2)
print("Symmetric difference of set 1 & set 2:")
print(setn1.symmetric_difference(setn2))
# 
# "10."
print('\n10. Write a Python program to clear a set.')
setn1 = set([1, 1, 2, 3, 4, 5])
print(setn1)
setn1.clear()
print('Above set has been cleared')
print(setn1)
# 
# "11."
print('\n11. Write a Python program to use of frozensets.')
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
print(x.isdisjoint(y))
print(x.difference(y))
print(x | y)
# 
# "12."
print('\n12. Write a Python program to find maximum and the minimum value in a set.')
set_1 = set([1, 1, 2, 3, 4, 5])
print(set_1)
print('Max value of above set:',max(set_1))
print('Min value of above set:',min(set_1))
# 
# 
# """     List      """
# 
# "1."
print('\n1. Write a Python program to sum all the items in a list.')
# 
l = [1,2,3]
l2 = [2,3,4]
l3 = [3,4,5]
print(f'l1: {l}, l2: {l2}, l3: {l3}')
l_s = l + l2 +l3
print('Sum of the above three list:', l_s)
# 
# "2."
print('\n2. Write a Python program to multiplies all the items in a list.')
# 
l = [1,5,3]
t = 1
for i in l:
    t *= i
print('List:',l)
print('Multiplies all the items in the list:', t)
# 
# "3."
print('\n3. Write a Python program to get the smallest number from a list.')
# 
l = list(input('Enter numbers to ger the smallest value: '))
print('list:',l)
print('The smallest value from the list:',min(l))
# 
# "4."
print('\n4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.')
l = ['abc', 'xyz', 'aba', '1221']
print('list:',l)
r = 0
for i in l:
    i = list(i)
    if len(i) >= 2 and i[0] == i[-1]:
        r += 1
# 
print('Number of strings where the string length is 2 or more and the first and last character are same from a given list of strings:',r)
# 
# "5."
print('\n5. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.')
l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print('list:',l)
def last(n):
    return n[-1]
sorted(l, key = last)
# 
print('Sorted list:', l)
# 
# "6."
print('\n6. Write a Python program to remove duplicates from a list.')
l = list((2,5,3,7,4,5,4,3))
print('List:',l)
l = set(l)
l = list(l)
print('Removed duplicate:',l)
# 
# "7."
print('\n7. Write a Python program to clone or copy a list.')
l_1 = list((2,5,3,7,4,5,4,3))
l_2 = l_1
print('List 1:',l_1)
print('Clone list: ', l_2)
# 
# "8."
print('\n8. Write a Python program to find the list of words that are longer than n from a given list of words.')
list_of_words = ["Shubham","Yash","Bharat","Naman","Raj","Nick"]
print('List of words',list_of_words)
list_of_words_longer_then_n = []
for i in list_of_words:
    if len(i) > 4 :
        list_of_words_longer_then_n.append(i)
# 
print('List of words longer then 4 alphabets in above list:',list_of_words_longer_then_n)
# 
# "9."
print('\n9. Write a Python function that takes two lists and returns True if they have at least one common member.')
l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]
l3 = ['a','s','d','f','g']
# 
print('List 1: ',l1)
print('List 2: ',l2)
print('List 3: ',l3)
# 
def trueList(l1,l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
# 
print('List 1 compare to List 2:',trueList(l1,l2))
print('List 1 compare to List 3:',trueList(l1,l3))
# 
# "10."
print('\n10. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.')
l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(l) if i not in (0,4,5)]
print(color)
# 
# "11."
print('\n11. Write a Python program to generate all permutations of a list in Python.')
from itertools import permutations
l = list(permutations([1,2,3]))
print(l)
# 
# "12."
print('\n12. Write a Python program to get the difference between the two lists.')
l1 = [1,2,3,4,5]
l2 = [1,3,5,7]
print('List 1:',l1)
print('List 2:',l2)
ld1 = list(set(l1) - set(l2))
ld2 = list(set(l2) - set(l1))
ld = ld1 + ld2
print('Difference between the two lists:',ld)
# 
# "13."
print('\n13. Write a Python program to append a list to the second list.')
l1 = [1,2,3,4,5]
l2 = [1,3,5,7]
print('List 1:',l1)
print('List 2:',l2)
for i in l2:
    l1.append(i)
print('Appended list 1 to the list 2:',l1)
# 
# "14."
print('\n14. Write a python program to check whether two lists are circularly identical.')
list1 = [1, 1, 2, 2, 1]
list2 = [1, 1, 1, 2, 2]
list3 = [1, 2, 1, 1, 1]
print('List 1:',list1)
print('List 2:',list2)
print('List 3:',list3)
print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))
# 
# "15."
print('\n15. Write a Python program to find common items from two lists.')
l1 = [1,2,3,4,5]
l2 = [1,3,5,7]
cl = []
print('List 1:',l1)
print('List 2:',l2)
for i in l1:
    for j in l2:
        if j == i:
            cl.append(i)
# 
print('Common items in list 1 and list 2:', cl)
# 
# "16."
print('\n16. Write a Python program to split a list based on first character of word.')
from itertools import groupby
from operator import itemgetter
# 
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
print('Word List:',word_list)
print('Splited word list based on first character of word:')
for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    char = []
    char.append(letter)
    for word in words:
        char.append(word)
# 
    print(char)
# 
# "17."
print('\n17. Write a Python program to remove duplicates from a list of lists.')
import itertools
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", num)
num.sort()
new_num = list(num for num,_ in itertools.groupby(num))
print("New List", new_num)
# 
# 
# """     Tuple      """
# 
# "1."
print('\n1. Write a Python program to create a tuple.')
t = tuple([1,2,3,4,5])
print('Tuple:',t)
print(type(t))
# 
# "2."
print('\n2. Write a Python program to create a tuple with different data types.')
t = tuple([2,'S',5.3,False])
print('Tuple:',t)
# 
# "3."
print('\n3. Write a Python program to unpack a tuple in several variables.')
t = tuple([1,2,3,4,5])
print('Tuple:',t)
a,b,c,d,e = t
print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}')
# 
# "4."
print('\n4. Write a Python program to create the colon of a tuple.')
from copy import deepcopy
tuplex = ("HELLO", 5, [], True)
print(tuplex)
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(25)
print(tuplex_colon)
print(tuplex)
# 
# "5."
print('\n5. Write a Python program to find the repeated items of a tuple.')
t = tuple([1,2,3,4,5,2,4])
s = set({})
print('Tuple:',t)
for i in t:
    c =t.count(i)
    if c > 1:
        s.add(i)
print('Repeated item:')
for j in s:
    print(j,':',t.count(j),'times')
# 
# "6."
print('\n6. Write a Python program to check whether an element exists within a tuple.')
t = tuple([1,2,3,4,5])
print('Tuple:',t)
print('Is 5 in tuple:',5 in t)
print('Is 6 in tuple:',6 in t)
# 
# "7."
print('\n7. Write a Python program to convert a list to a tuple.')
l = list([1,2,3,4,5])
print('List:',l)
print(type(l))
t = tuple(l)
print('Tuple:',t)
print(type(t))
# 
# "8."
print('\n8. Write a Python program to remove an item from a tuple.')
t = (1,2,3,4,5,6,7,8)
print('Tuple:',t)
print(type(t))
r = int(input('Number that you want to be removed from the tuple: '))
print('Updated tuple:',t[:r-1]+t[r:])
print(type(t))
# 
# "9."
print('\n9. Write a Python program to slice a tuple.')
t = (1,2,3,4,5,6,7,8)
print('Tuple:',t)
print('Sliced tuple:',t[3:])
# 
# "10."
print('\n10. Write a Python program to reverse a tuple.')
t = (1,2,3,4,5,6,7,8)
print('Tuple:',t)
print('Reverse tuple', tuple(reversed(t)))
# 
# 
# """     String      """
# 
# "1."
print('\n1. Write a Python program to calculate the length of a string.')
s = "Shubham"
print('String:',s)
print('Length:',len(s))
# 
# "2."
print('\n2. Write a Python program to count the number of characters (character frequency) in a string.')
s ='google.com'
print('String:',s)
c = {}
for i in s:
    c.update({i:s.count(i)})
# 
print('Character frequency:',c)
# 
# "3."
print("\n3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.")
s = 'restart'
print('String:',s)
r = s.replace('r','$')
print('Replaced string:','r'+r[1:])
# 
# "4."
print("\n4. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.")
s = input('Enter a string: ')
if len(s) > 2 :
    if s[-3:] == 'ing':
        print('Changed string:',s+'ly')
    else:
        print('Changed string:',s+'ing')
else:
    print(s)
# 
# "5."
print('\n5. Write a Python function that takes a list of words and returns the length of the longest one.')
s = ['asdfa','aergteg','tym','poityjmn']
l = []
for i in s:
    l.append(len(i))
# 
print('Length of the longest one:',max(l))
# 
# "6."
print('\n6. Write a Python script that takes input from the user and displays that input back in upper and lower cases.')
s = input('Enter string: ')
print('Upper case string:',s.upper())
print('Lower case string',s.lower())
# 
# "7."
print('\n7. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).')
word = input('Enter comma separated sequence of words: ')
words = [word for word in word.split(",")]
print(",".join(sorted(list(set(words)))))
# 
# "8."
print('\n8. Write a Python program to get the last part of a string before a specified character.')
s = 'aiustdoiwejrfnasoijao'
print('String:',s)
print(s.rsplit('r', 1)[0])
print(s.rsplit('d', 1)[0])
# 
# "9."
print("\n9. Write a Python program to display formatted text (width=50) as output.")
import textwrap
# 
text = """
 Lorem Ipsum is simply dummy text of the printing and typesetting 
 industry. Lorem Ipsum has been the industry's standard dummy text 
 ever since the 1500s, when an unknown printer took a galley of type 
 and scrambled it to make a type specimen book. It has survived not 
 only five centuries, but also the leap into electronic typesetting, 
 remaining essentially unchanged.
  """
print()
print(textwrap.fill(text, width=50))
print()
# 
# "10."
print('\n10. Write a Python program to count occurrences of a substring in a string.')
s = 'Write a Python program to count occurrences of a substring in a string.'
print('String:',s)
print("Number of 'count':",s.count('count'))
# 
# "11."
print('\n11. Write a Python program to reverse a string.')
s = 'Shubham'
print('String:',s)
r = ''
index = len(s)
while index > 0:
    r += s[ index - 1 ]
    index = index - 1
print('Reversed string:',r)
# 
# "12."
print('\n12. Write a Python program to lowercase first n characters in a string.')
s = 'SHUBHAM'
print('String:',s)
print('Updated string:',s[:3].lower() + s[3:])
# 