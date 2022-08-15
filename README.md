# DataScience0001
Coffeee Data Science Bootcamp - 0001 Assignments

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
