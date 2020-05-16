# Notes on robot files

## Python2

The robot file for python2 resides in */usr/share/laby/mods/python/lib/robot.py*

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

## Python3




`

