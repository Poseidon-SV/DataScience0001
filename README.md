# DataScience0001
Coffeee Data Science Bootcamp - 0001 Assignments `All Outputs`

In `VS Codes` to get the output of all code (qurestions) : Click at the left side where `'1.'` is written so you can see `|` blinking then scroll to the end and press `Shift` + `Alt` + `left click` and then press `Ctrl` + `/` to uncomment the code and then you can run and enter the inputs (for certain questions)  and proceed to get the output.
(Question 9 is bugged you have to run it separately to get it's output or just comment it to get all the other outputs at once.)
## Outputs of first 1 to 30 questions of assignment

```
1. Write a Python program which accepts the user's first and last name and prints them in reverse order with a space between them.
First name: Shubham
Last name: Verma
Verma Shubham

2.  Write a Python program which accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.
Enter sequence of comma-separated numbers: 2,6,9,7,5
List :  ['2,6,9,7,5']
Tuple :  ('2,6,9,7,5',)

3. Write a Python program to display the first and last colours from the following list.
['Red', 'Green', 'White', 'Black']
First color : Green 
Last color : Black

4. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.


5. Write a Python program to print the calendar of a given month and year.
Input the year : 2022
Input the month : 8
    August 2022
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31


6. Write a Python program to calculate number of days between two dates.
Enter first date in (yyyy, m, d): 2022, 8, 9
Enter second date in (yyyy, m, d): 2022, 9, 10
The number of days are:  32

7. Write a Python program to check whether a specified value is contained in a group of values.
Enter a value to check: 3
True
Enter a value to check: -1
False

8. Write a Python program to create a histogram from a given list of integers.
List: 5,9,2,4,6
________________
|=====] 5
|=========] 9
|==] 2
|====] 4
|======] 6
|

9. Write a Python program to concatenate all elements in a list into a string and return it.
List: 4,gy,8,d,6,3,sv
List in string:  ['4', 'gy', '8', 'd', '6', '3', 'sv']

10. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
color_list_1:  {'Black', 'Red', 'White'}
color_list_2:  {'Green', 'Red'}

Differenct of color_list_1 and color_list_2:
By color_list_1.difference(color_list_2) {'Black', 'White'}

Differenct of color_list_1 and color_list_2:
By color_list_1 - color_list_2 {'Black', 'White'}

11. Write a Python program to check whether a file exists.
File path: .gitattributes
True

12. Write a python program to call an external command in Python.
Write your external commond: ls -l
'ls' is not recognized as an internal or external command,
operable program or batch file.
1

13. Write a Python program to find out the number of CPUs using.
import multiprocessing
print(multiprocessing.cpu_count()): 4

14. Write a Python program to list all files in a directory in Python.     
from os import listdir
print (listdir('File path name'))
['1st.py', 'Data Science - Session 02 - Assignment.pdf', 'DataScience0001']

15. Write a python program to access environment variables.
ALLUSERSPROFILE
----------
C:\ProgramData
====================>
APPDATA
----------
C:\Users\Shubham\AppData\Roaming
====================>
CHOCOLATEYINSTALL
----------
C:\ProgramData\chocolatey
====================>
CHOCOLATEYLASTPATHUPDATE
----------
132840280625927458
====================>
CHROME_CRASHPAD_PIPE_NAME
----------
\\.\pipe\crashpad_6020_RZKQWOZTCVOJZPVC
====================>
COMMONPROGRAMFILES
----------
C:\Program Files\Common Files
====================>
COMMONPROGRAMFILES(X86)
----------
C:\Program Files (x86)\Common Files
====================>
COMMONPROGRAMW6432
----------
C:\Program Files\Common Files
====================>
COMPUTERNAME
----------
DESKTOP-57ADH6O
====================>
COMSPEC
----------
C:\WINDOWS\system32\cmd.exe
====================>
DRIVERDATA
----------
C:\Windows\System32\Drivers\DriverData
====================>
HOMEDRIVE
----------
C:
====================>
HOMEPATH
----------
\Users\Shubham
====================>
LOCALAPPDATA
----------
C:\Users\Shubham\AppData\Local
====================>
LOGONSERVER
----------
\\DESKTOP-57ADH6O
====================>
NUMBER_OF_PROCESSORS
----------
4
====================>
ONEDRIVE
----------
C:\Users\Shubham\OneDrive
====================>
ONEDRIVECONSUMER
----------
C:\Users\Shubham\OneDrive
====================>
ORIGINAL_XDG_CURRENT_DESKTOP
----------
undefined
====================>
OS
----------
Windows_NT
====================>
PATH
----------
C:\Program Files\Common Files\Oracle\Java\javapath;C:\Users\Shubham\AppData\Local\Programs\Python\Python310\Scripts\;C:\Users\Shubham\AppData\Local\Programs\Python\Python310\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\ProgramData\chocolatey\bin;E:\Program Files\Git\cmd;E:\MATLAB\R2016b\runtime\win64;E:\MATLAB\R2016b\bin;E:\MATLAB\R2016b\polyspace\bin;C:\Users\Shubham\AppData\Local\Microsoft\WindowsApps;C:\Users\Shubham\AppData\Local\Programs\Microsoft VS Code\bin;E:\Shubham\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\bin;;C:\ProgramData\Shubham\GitHubDesktop\bin;C:\Users\Shubham\M.app\flutter\bin;C:\Program Files\Android\platform-tools;C:\Program Files\Java\jdk-17.0.2\bin;E:\MATLAB\R2016b\bin\matlab;C:\Users\Shubham\AppData\Local\Android\Sdk;
====================>
PATHEXT
----------
.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW;.CPL
====================>
PROCESSOR_ARCHITECTURE
----------
AMD64
====================>
PROCESSOR_IDENTIFIER
----------
Intel64 Family 6 Model 60 Stepping 3, GenuineIntel
====================>
PROCESSOR_LEVEL
----------
6
====================>
PROCESSOR_REVISION
----------
3c03
====================>
PROGRAMDATA
----------
C:\ProgramData
====================>
PROGRAMFILES
----------
C:\Program Files
====================>
PROGRAMFILES(X86)
----------
C:\Program Files (x86)
====================>
PROGRAMW6432
----------
C:\Program Files
====================>
PSMODULEPATH
----------
C:\Users\Shubham\Documents\WindowsPowerShell\Modules;C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules
====================>
PUBLIC
----------
C:\Users\Public
====================>
PYCHARM COMMUNITY EDITION
----------
E:\Shubham\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\bin;
====================>
SESSIONNAME
----------
Console
====================>
SYSTEMDRIVE
----------
C:
====================>
SYSTEMROOT
----------
C:\WINDOWS
====================>
TEMP
----------
C:\Users\Shubham\AppData\Local\Temp
====================>
TMP
----------
C:\Users\Shubham\AppData\Local\Temp
====================>
USERDOMAIN
----------
DESKTOP-57ADH6O
====================>
USERDOMAIN_ROAMINGPROFILE
----------
DESKTOP-57ADH6O
====================>
USERNAME
----------
Shubham
====================>
USERPROFILE
----------
C:\Users\Shubham
====================>
WINDIR
----------
C:\WINDOWS
====================>
TERM_PROGRAM
----------
vscode
====================>
TERM_PROGRAM_VERSION
----------
1.70.0
====================>
LANG
----------
en_US.UTF-8
====================>
COLORTERM
----------
truecolor
====================>
GIT_ASKPASS
----------
c:\Users\Shubham\AppData\Local\Programs\Microsoft VS Code\resources\app\extensions\git\dist\askpass.sh
====================>
VSCODE_GIT_ASKPASS_NODE
----------
C:\Users\Shubham\AppData\Local\Programs\Microsoft VS Code\Code.exe
====================>
VSCODE_GIT_ASKPASS_EXTRA_ARGS
----------
--ms-enable-electron-run-as-node
====================>
VSCODE_GIT_ASKPASS_MAIN
----------
c:\Users\Shubham\AppData\Local\Programs\Microsoft VS Code\resources\app\extensions\git\dist\askpass-main.js
====================>
VSCODE_GIT_IPC_HANDLE
----------
\\.\pipe\vscode-git-f4b0184178-sock
====================>
16. Write a Python program to get the current username
import os
print(os.environ.get('USERNAME'))
Shubham

17. Write a program to get execution time for a Python method.
1
3
6
10
15
21
28
36
45
Exicution time:0.01699
Exicution time: 0.01698756217956543 seconds

18. Write a Python program to get an absolute file path.
import os
absolute_file_path = os.path.abspath('.gitattributes')
print("Absolute file path: ",absolute_file_path)
Absolute file path:  E:\Shubham\Desktop\AI-ML\Coffeee Data Science Bootcamp - 0001\DataScience0001\.gitattributes

19. Write a Python program to get file creation and modification date/times.
File name: .gitattributes
Last modified: Sun Aug  7 17:32:50 2022
Created: Sun Aug  7 17:32:50 2022

20. Write a Python program to sort three integers without using conditional statements and loops.
Enter 3 integers(n,n,n): 4,8,2
Sorted list: [2, 4, 8]

22. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
This is the name/path of the script:
Number of arguments: 1
Argument List: ['e:/Shubham/Desktop/AI-ML/Coffeee Data Science Bootcamp - 0001/DataScience0001/Data Science - Session 02 - Assignment.py']

23. Write a Python program to find the available built-in modules.
_abc, _ast, _bisect, _blake2, _codecs, _codecs_cn, _codecs_hk, _codecs_iso2022, _codecs_jp, _codecs_kr, _codecs_tw, _collections, _contextvars, _csv, _datetime, _functools, _heapq, _imp, _io, _json, _locale, _lsprof, _md5, _multibytecodec, _opcode, _operator, _pickle, _random, _sha1, _sha256, _sha3, _sha512, _signal, _sre, _stat, _statistics, _string, _struct, _symtable, _thread, _tracemalloc, _warnings, _weakref, 
_winapi, _xxsubinterpreters, array, atexit, audioop, binascii, builtins, cmath, errno, faulthandler, gc, itertools, marshal, math, mmap, msvcrt, nt, sys, time, winreg, xxsubtype, zlib

24. Write a Python program to get the size of an object in bytes.
object:  7
Size of the object is: 28

25. Write a Python program to get the current value of the recursion limit.
Current value of the recursion limit: 1000

26. Write a Python program to count the number occurrence of a specific character in a string.
String: Write a Python program to count the number occurrence of a specific character in a string.
Enter the character to count the number occurrence of it in the given above string: o
The number of 'o' in the above string is: 6

27. Write a Python program to get the system time.
The systen time is: 19:51:53.476940

28. Write a Python program to clear the screen or terminal.
import os
os.system('cls')

29. Write a Python program to get the name of the host on which the routine is running.
import socket
host_name = socket.gethostname()
print("Host name:", host_name)
Host name: DESKTOP-57ADH6O

30. Write a Python program to access and print a URL's content to the console.
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>

```

## Output of all questions (Python data structure - Array, Dictonary, Sets, List, Tuple and Strings) of Assignment

```
1. Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.
array: [1, 2, 3, 4, 5]
array items:
1
2
3
4
5
Enter the index you want to access form the array: 3
4

2. Write a Python program to reverse the order of the items in the array.
array: [1, 2, 3, 4, 5]
Reverse ordered array: [5, 4, 3, 2, 1]

3. Write a Python program to get the number of occurrences of a specified element in an array.
array: [2, 3, 3, 4, 2, 5, 8, 2, 9, 4, 7]
Enter the element to count the number occurrence of it in the given above string : 4
The number of 4's present in array : 2

4. Write a Python program to remove the first occurrence of a specified element from an array.
array: [2, 4, 1, 5, 8, 9]
Enter the element you want to remove from the above array: 5
Here is the array with removed element: [2, 4, 1, 8, 9]

1. Write a Python script to sort (ascending and descending) a dictionary by value.
Dictionary : {'key5': 'value5', 'key1': 'value1', 'key3': 'value3', 'key2': 'value2', 'key4': 'value4'}
Dictionary value in ascending order : {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}
Dictionary value in descending order : {'key5': 'value5', 'key4': 'value4', 'key3': 'value3', 'key2': 'value2', 'key1': 'value1'}

2. Write a Python script to add a key to a dictionary.
Dictionary : {0: 10, 1: 20}
Update dictonary with {2: 30}
Updated dictonary : {0: 10, 1: 20, 2: 30}

Write a Python script to concatenate following dictionaries to create a new one.
Dictonary: {}
dic1 = {1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Concatenated dictonary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

4. Write a Python program to iterate over dictionaries using for loops.
Dictonary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
Iterated dictonary:
1: 10
2: 20
3: 30
4: 40
5: 50
6: 60

5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 5
Dictonary: {}
Dictonary is being updated:
{1: 1}
{1: 1, 2: 4}
{1: 1, 2: 4, 3: 9}
{1: 1, 2: 4, 3: 9, 4: 16}
Updated dictonary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

6. Write a Python program to remove a key from a dictionary.
Dictonary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Enter a key from above dictoanry that you want to remove: 3
Updated dictonary: {1: 1, 2: 4, 4: 16, 5: 25}

7. Write a Python program to print all unique values in a dictionary.
Dictonary; [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]
Unique values: {'S005', 'S009', 'S001', 'S002', 'S007'}

8. Write a Python program to create a dictionary from a string.
String: w3resource
Count of the letters from the string is the value of dictonary
Dictonary: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

9. Write a Python program to print a dictionary in table format.
NAME    AGE   BRANCH
Yash    20    IT
Naman   20    CSE
Bharat  22    CSE

10. Write a Python program to count the values associated with key in a dictionary.
Sample_data = [
    {"id": 1, "success": True, "name": "Lary"},
    {"id": 2, "success": False, "name": "Rabi"},
    {"id": 3, "success": True, "name": "Alex"}
    ]
Dictionaries that have success as True: 2

11. Write a Python program to convert a list into a nested dictionary of keys.
{1: {2: {3: {4: {5: {6: {7: {8: {9: {}}}}}}}}}}

12. Write a Python program to check multiple keys exists in a dictionary.
Dictonary 1: {'id': 1, 'success': True, 'name': 'Lary'}
Multiple keys exists in the dictionary
Dictonary 2: {'id': 1}
Multiple keys does not exists in the dictionary

13. Write a Python program to count number of items in a dictionary value that is a list.
Dictonary: {1: [1, 2], 2: '2', 3: '3', 4: [1, 2, 3, 4]}
print('Number of items in a dictionary value:',sum(map(len, dic.values())))
Number of items in a dictionary value = 8

1. Write a Python program to create a set.
{1, 2, 3, 4, 5}
<class 'set'>

2. Write a Python program to iteration over sets.
my_set = set(['a','s','d','f','g'])
s
a
g
d
f

3. Write a Python program to add member(s) in a set.
my_set = set(['a','s','d'])
{'a', 's', 'd', 1}

4. Write a Python program to remove item(s) from set
my_set: {'a', 1, 'd', 's'}
{'a', 'd', 's'}

5. Write a Python program to remove an item from a set if it is present in the set.
Enter values : iew2i5n
'2' will be removed
{'5', 'w', 'i', 'n', 'e'}

6. Write a Python program to create an intersection of sets.
Original set elements:
{'green', 'blue'}
{'yellow', 'blue'}

Intersection of two said sets:
{'blue'}

7. Write a Python program to create a union of sets

Original sets:
{1, 2, 3, 4, 5}
{1, 2, 3, 6, 7, 8, 9}

Union of above sets:
{1, 2, 3, 4, 5, 6, 7, 8, 9}

8. Write a Python program to create set difference.

Original sets:
{1, 2, 3, 4, 5}
{1, 5, 6, 7, 8, 9}

Difference of setn1 - setn2:
{2, 3, 4}

Difference of setn2 - setn1:
{8, 9, 6, 7}

9. Write a Python program to create a symmetric difference.
Original sets:
{1, 2, 3, 4, 5}
{1, 5, 6, 7, 8, 9}
Symmetric difference of set 1 & set 2:
{2, 3, 4, 6, 7, 8, 9}

10. Write a Python program to clear a set.
{1, 2, 3, 4, 5}
Above set has been cleared
set()

11. Write a Python program to use of frozensets.
False
frozenset({1, 2})
frozenset({1, 2, 3, 4, 5, 6, 7})

12. Write a Python program to find maximum and the minimum value in a set.
{1, 2, 3, 4, 5}
Max value of above set: 5
Min value of above set: 1

1. Write a Python program to sum all the items in a list.
l1: [1, 2, 3], l2: [2, 3, 4], l3: [3, 4, 5]
Sum of the above three list: [1, 2, 3, 2, 3, 4, 3, 4, 5]

2. Write a Python program to multiplies all the items in a list.
List: [1, 5, 3]
Multiplies all the items in the list: 15

3. Write a Python program to get the smallest number from a list.
Enter numbers to ger the smallest value: 98424
list: ['9', '8', '4', '2', '4']
The smallest value from the list: 2

4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
list: ['abc', 'xyz', 'aba', '1221']
Number of strings where the string length is 2 or more and the first and last character are same from a given list of strings: 2

5. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
list: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Sorted list: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

6. Write a Python program to remove duplicates from a list.
List: [2, 5, 3, 7, 4, 5, 4, 3]
Removed duplicate: [2, 3, 4, 5, 7]

7. Write a Python program to clone or copy a list.
List 1: [2, 5, 3, 7, 4, 5, 4, 3]
Clone list:  [2, 5, 3, 7, 4, 5, 4, 3]

8. Write a Python program to find the list of words that are longer than n from a given list of words.
List of words ['Shubham', 'Yash', 'Bharat', 'Naman', 'Raj', 'Nick']
List of words longer then 4 alphabets in above list: ['Shubham', 'Bharat', 'Naman']

9. Write a Python function that takes two lists and returns True if they have at least one common member.
List 1:  [1, 2, 3, 4, 5]
List 2:  [5, 6, 7, 8, 9]
List 3:  ['a', 's', 'd', 'f', 'g']
List 1 compare to List 2: True
List 1 compare to List 3: None

10. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
['Green', 'White', 'Black']

11. Write a Python program to generate all permutations of a list in Python.
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

12. Write a Python program to get the difference between the two lists.
List 1: [1, 2, 3, 4, 5]
List 2: [1, 3, 5, 7]
Difference between the two lists: [2, 4, 7]

13. Write a Python program to append a list to the second list.
List 1: [1, 2, 3, 4, 5]
List 2: [1, 3, 5, 7]
Appended list 1 to the list 2: [1, 2, 3, 4, 5, 1, 3, 5, 7]

14. Write a python program to check whether two lists are circularly identical.
List 1: [1, 1, 2, 2, 1]
List 2: [1, 1, 1, 2, 2]
List 3: [1, 2, 1, 1, 1]
Compare list1 and list2
True
Compare list1 and list3
False

15. Write a Python program to find common items from two lists.
List 1: [1, 2, 3, 4, 5]
List 2: [1, 3, 5, 7]
Common items in list 1 and list 2: [1, 3, 5]

16. Write a Python program to split a list based on first character of word.
Word List: ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think', 'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']
Splited word list based on first character of word:
['a', 'ask']
['b', 'be']
['c', 'call', 'come']
['d', 'do']
['f', 'feel', 'find']
['g', 'get', 'give', 'go']
['h', 'have']
['k', 'know']
['l', 'leave', 'look']
['m', 'make']
['s', 'say', 'see', 'seem']
['t', 'take', 'tell', 'think']
['u', 'use']
['w', 'want', 'work']

17. Write a Python program to remove duplicates from a list of lists.
Original List [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List [[10, 20], [30, 56, 25], [33], [40]]

1. Write a Python program to create a tuple.
Tuple: (1, 2, 3, 4, 5)
<class 'tuple'>

2. Write a Python program to create a tuple with different data types.
Tuple: (2, 'S', 5.3, False)

3. Write a Python program to unpack a tuple in several variables.
Tuple: (1, 2, 3, 4, 5)
a = 1, b = 2, c = 3, d = 4, e = 5

4. Write a Python program to create the colon of a tuple.
('HELLO', 5, [], True)
('HELLO', 5, [25], True)
('HELLO', 5, [], True)

5. Write a Python program to find the repeated items of a tuple.
Tuple: (1, 2, 3, 4, 5, 2, 4)
Repeated item:
2 : 2 times
4 : 2 times

6. Write a Python program to check whether an element exists within a tuple.
Tuple: (1, 2, 3, 4, 5)
Is 5 in tuple: True
Is 6 in tuple: False

7. Write a Python program to convert a list to a tuple.
List: [1, 2, 3, 4, 5]
<class 'list'>
Tuple: (1, 2, 3, 4, 5)
<class 'tuple'>

8. Write a Python program to remove an item from a tuple.
Tuple: (1, 2, 3, 4, 5, 6, 7, 8)
<class 'tuple'>
Number that you want to be removed from the tuple: 6
Updated tuple: (1, 2, 3, 4, 5, 7, 8)
<class 'tuple'>

9. Write a Python program to slice a tuple.
Tuple: (1, 2, 3, 4, 5, 6, 7, 8)
Sliced tuple: (4, 5, 6, 7, 8)

10. Write a Python program to reverse a tuple.
Tuple: (1, 2, 3, 4, 5, 6, 7, 8)
Reverse tuple (8, 7, 6, 5, 4, 3, 2, 1)

1. Write a Python program to calculate the length of a string.
String: Shubham
Length: 7

2. Write a Python program to count the number of characters (character frequency) in a string.
String: google.com
Character frequency: {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
String: restart
Replaced string: resta$t

4. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Enter a string: string
Changed string: stringly

5. Write a Python function that takes a list of words and returns the length of the longest one.
Length of the longest one: 8

6. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
Enter string: Shubham
Upper case string: SHUBHAM
Lower case string shubham

7. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
Enter comma separated sequence of words: red, white, black, red, green, black
 black, green, red, white,red

8. Write a Python program to get the last part of a string before a specified character.
String: aiustdoiwejrfnasoijao
aiustdoiwej
aiust

9. Write a Python program to display formatted text (width=50) as output.

  Lorem Ipsum is simply dummy text of the printing
and typesetting   industry. Lorem Ipsum has been
the industry's standard dummy text   ever since
the 1500s, when an unknown printer took a galley
of type   and scrambled it to make a type specimen
book. It has survived not   only five centuries,
but also the leap into electronic typesetting,
remaining essentially unchanged.


10. Write a Python program to count occurrences of a substring in a string.
String: Write a Python program to count occurrences of a substring in a string.
Number of 'count': 1

11. Write a Python program to reverse a string.
String: Shubham
Reversed string: mahbuhS

12. Write a Python program to lowercase first n characters in a string.
String: SHUBHAM
Updated string: shuBHAM
```
