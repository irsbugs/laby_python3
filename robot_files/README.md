# Notes on robot files

## Python2 - Background Information

The robot file for python2 resides in `/usr/share/laby/mods/python/lib/robot.py`.

When the execute button in the Laby GUI is pressed a /tmp/ant-nnnnn-n folder is created. 
The robot file is processed and a modified robot.py file is placed in the /tmp/ant folder.

For example, the original robot.py file contains this function and variable names like this:
```
def laby_name_left():
laby_name_Void = 0;
```
When robot.py is processed and written to the /tmp/ant folder the function and variable names are now like this:
```
def left():
Void = 0;
```
However, having the inclusion of `laby_name_` does not seem to be necessary in the initial 
`/usr/share/laby/mods/python/lib/robot.py` file. If the initial robot.py defines functions and 
variables without `laby_name_`, then they are written OK to the /tmp/ant folder without modification.

For reference, these two files are included in this github folder as:
* robot_python2.py
* robot_python2_tmp.py

## Python3

The following folder is created to provide support for Python3:
```
/usr/share/laby/mods/python3
```
The files copied into this folder are:
* help
* rules
* skel
and a subfolder named *lib* is created for:
* robot.py

The above files may be copied from the python2 folders `/usr/share/laby/mods/python/`

### python3/skel
The *skel* file should be edited so the first line is changed from:
`from robot import *;`
to have it semi-colon removed:
`from robot import *`

At a later stage you may wish to edit the python code and function calls in the skel file.
This will change the default contents that is loaded into the *Program* window when Laby is launched.

### python3/help
The *help* file does not need to be editied, however it is rather limited in the help and may be enhanced with more examples, etc.

### python3/rules file
The rules file needs to be changed to support python3. Currently the python2 file is as follows:
```
info:
need	python

run:
fetch	robot.py
dump	program.py
spawn	python program.py
```
change it to be:
```
info:
need	python3

run:
fetch	robot.py
dump	program.py
spawn	python3 program.py
```

### python3/lib/robot.py file

The original Python2 `robot.py` file shold work OK with Python3. However there are aspects of the 
this file that may be enhanced. For examples:

* The python code is not [PEP8](https://www.python.org/dev/peps/pep-0008/) compliant.
* The local function `input()` is used which is also the name of a Python3 builtin function.
* The sys module is imported to provide three functions:
  * sys.stdout.write()
  * sys.stdout.flush()
  * sys.stdin.readline()
  These functions may be replaced with the Python3 `input()` function doing the sys.stdin.readline()
  while its *prompt*  feature provides the sys.stdout.write() and sys.stdout.flush(). In doing this 
  the `import sys` line of code may be removed from the file.
* The robot.py file has an extra level of complexity in its look() function. This provides the 
title-case variable names: Void, Wall, Rock, Web and Escape. With the python3 `input()` function
the string that is returned may be used directly. Thus it provides the lowercase names: void, wall, 
rock, web, and escape.
* Only the look() file provided a response via a variable. The other functions, left(), right(), forward()
take(), drop() and escape() return a response to the calling code. Normally the response is *ok* to 
indicate the function has executed.

The file **robot_python3_simple.py** is included as a direct replacement for the python2 robot.py file, 
and includes the above enhancements.
 
As an alternative to the above, the file	**robot_python3_simple_verbose.py** includes a boolean variable 
**verbose** defaulted to **True**. If any function is called, then the response from executing the 
function is displayed in the message window. E.g. `forward: ok`




`

