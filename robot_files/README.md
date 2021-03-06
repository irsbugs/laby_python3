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

### Program failing to execute last function.

It has been observed that there are times when the last function in the program you write will not execute. 
For example if the last line of code is escape() then the program appears to have a race condition and
the ant is note displayed as having escaped before the program halts. A work-around is to add the following 
two lines of code  after the escape() function to add some delay:
```
import time
time.sleep(1)
```

## Python3 Additional Functions to robot.py file

In the Laby Program window the code you write may include functions. These functions could tend to clutter up
this Program window. To help overcome this issue the function that you write may be added to the robot.py
module. Also you may add to robot.py code that you want executed every time the program is started.

For example if you wanted to check the version of python each time your program starts you could insert 
the following into robot.py

```
import sys
def get_python_version():
    return sys.version
```
In your program you could enter the line of code:
```
say(get_python_version())
```
In the message box it will display the python version.

Another option is to place at the bottom of the robot.py module the code `say(get_python_version())`
and the version will be displayed every time the program starts.

The file **robot_python3_additional_functions.py** contains a selection of functions and code that
executes at startup that may be useful in the programs that you write. 

Top-level variables that are declared in robot.py may be read by functions in robot.py. This 
may provide a handy way of providing variable to multiple functions without having to directly
pass the variable via the function call.

Below is a description of additional functions that have been included:

### platform_check()

The *platform_check()* function is designed so that it is called every time the program starts.
If the platform is "linux", then the program continues, otherwise it displays an error message
and halts. At this stage this code has only been tested on a linux platform. If you wish to try
running Laby and python3 on another platform, then comment out or modify this checking function.

### python_check()

The *python_check()* is also run every time your program is started. At the moment it allows any
version of python3 from 3.0. i.e. `if sys.version_info < (3,):` then display error message and
exit. If you add functions that use features added to python3 since 3.0, then you will need to 
modify this functions to block early minor releases of python3 from being able to continue to run.
E.g. `if sys.version_info < (3,4,)`: will block running the program if using a version of python 
less than 3.4.

### Launch time stamp

Every time the program starts it *import time* and will create a time stamp variable, *ts*, that 
contains the local time. The syntax is:`ts = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())` 
which will create a string like *2020-05-16_20-29-04*. This string may then be incorporated into
filenames to make them unique, etc.


### Establish a local folder for data

When the program runs you may wish to gather data in a local folder. The folder `~/laby_data/` is 
created if it does not already exist. The name *full_path* is given to the variable that holds
the `~/laby_data/` string.

### Backup of the program.py file: backup(verbose=True)

Upon pressing the *execute* button on the Laby GUI the code you have written in the Program window
is dumped to the `/tmp/ant-nnnnn-n` folder. The function *backup()* maybe called by your
program. It will copy from the `/tmp/ant` folder the file program.py to the `~/laby_data/` folder and
give the file a time stamped name. For example: *program_2020-05-16_20-29-04.py*. Should you shutdown 
your computer then when you restart you can cut and paste the content from the latest backup file
into your Laby Program window to continue from where you left off.

If you wish this backup operation to be displayed in the Messages window, then call the function with
*backup(verbose=True)*


### Drop rock: drop_rock(have_rock=True, rotate="right")

A common scenario is that the ant is carrying a rock and comes across another rock that is blocking 
his way. The ant can not carry two rocks so he needs to turn around till he finds a void space
and drop the rock. He then turns back to the direction he was originally facing where he can proceed 
by picking up the new rock that is blocking him. 

Whether or not the ant is carrying a rock is something that your program needs to track. 

The function *drop_rock(have_rock=True, rotate="right")* defaults to assuming the ant has a rock 
and to start making 90 degree turns to the right looking for a the first void place to drop the rock. 
Once the rock has been droped the function turns the ant back to the original direction was facing.

If you want the ant to start looking for a void space in an anti-clockwise direction then call the 
function with *drop_rock(True, "left")*

### GPS update: gps_update(gps, action="forward", verbose=False, log=False):

The direction that the ant is facing may be determined by looking the the Laby GUI display, but is
not available through a function call. A simple integer based direction system can be used, where 0
is north or up the screen, 1 is East or heading to the right, 2 is South and 3 is West.

The ant can only move forward one space at a time in the direction that he is facing. Thus an integer
system of coordinates can be updated to relatively keep track of where the ant is.

Thus at the beginning of the program, if the ant is facing north, then the x coordinate, y coordinate 
and direction number are assigned as a list to the name space gps. i.e. `gps = [0, 0, 0]` for \[x, y, d].
If the ant was facing South you would initialize gps as \[0, 0, 2].

When forward(), right() or left() functions have been executed, you can then, for example call the function 
*gps = gps_update(gps, "forward")*. The gps x/y coordinates and the direction will be updated and the
gps list will be returned.

The *gps_update()* call can include *log=True*. This will then call the gps_log() function described below.

### GPS log: gps_log(gps):

Whenever the program starts, it will create an empty csv file in the *~/laby_data/* folder called *gps.csv*. 
The gps_log(gps) function will write the contents of the gps list to the csv file. At the beginning of the
program if the ant is facing east then you might wish to execute the code, `gps = [0, 0, 1]` and log this
with gps_log(gps). The first line of the gps.csv file will then become: `0,0,1`

Potentially this file could be analyzed after running your program to investigate the efficiency of the ant.

### Create Grid: create_grid(grid_max = 21)

The *create_grid* function along with 5 other functions allows the ant to explore the labyrinth he is
in and map its contents.

The grid is comprised of lists that make a two dimensional array that is accessed by X and Y coordinates.
With the grid_max argument at its default value of 21, the grid in both X and Y axis will be from -10 to +10.
The contents of positions on the grid are entered as `grid[X][Y] = string value`. The string value is a single 
character. Thus if you wanted to use *s* for *starting point*, then the entry would be `grid[0][0] = "s"`.
As the grid has equal amounts of negative and positive axis, then an offset must be applied to so that when
x=0 and y=0 then this is offset to be the centre of the grid.

The *create_grid* function creates this list array called *grid* where each point in the grid represents one
square in the labyrinth and the surrounding area.

### Plot 360: plot_360(grid, gps, grid_max)

The *plot_360* function requests the ant to turn through 360 degrees. Every 90 degrees the ant performs a 
*get_look()* and what is observed (void, wall, rock, web or exit) is recorded in the grid using single 
characters: void is ., wall is o, rock is r, web is w and exit is x. Note that these are the same characters 
used in the map section of the laby files.

### Get look: get_look()

This is normally an internal function that is only used by *plot_360*. It returns the single characters
of what it sees with the look() function.

### Ant position: ant_position(gps, grid_max)

The *ant_position* function will place an arrow character pointing in the direction the ant is facing
into the grid at the current location of the ant

### Rotate grid: rotate_grid(grid, grid_max)

The grid that is a list array if converted to a string in a simple way will result in a grid that displays
as rotated 90 degrees clockwise. The *rotate_grid* function rotates the grid 90 degrees aanti-clockwise, and 
then creates a string of data that is the contents of the grid.

Creating the label for the X axis is a rather complex, so a seperate internal function is used to perform this.

This string could then be written to the Message window with the say() function.

### Write Grid: write_grid(grid_string)

The string of data collected by *rotate_grid* may be passed to *write_grid* where it is written to the
file *grid* in the *~/laby_data* folder.

### Ant Official Intelligence: ant_official_intelligence(direction="right"):

This function will provide the ant with enough *intelligence* to get through many labyrinth designs.

This function calls additional functions, drop_rock() and left_check() or right_check()

The ants official inteligence is based around the concept that if you enter a labyrinth and pick one 
hand to keep brushing along against the wall, then you will eventually get to the exit.

Along the way the ant adheres to the following rule: 

After moving forward, always check in the assigned direction to see if it provides a way forwards. 
This way the ant attempts to keep brushing along the specified wall. Among other reasons, this stops 
the ant from going right past an exit door.

This function defaults to the ant always checking on its right. If "left" is entered as the argument 
the ant always checks on his left.

### Check right: check_right(rock):

The rock argument is a boolean value to indicate if the ant is carrying a rock.

The ant will turn 90 degrees to his right and after reviewing the situation decide on an action, as follows:
* if there is an exit, then escape.
* if there is an exit, but carrying a rock, then drop rock and escape
* if there is a wall turn back 90 degrees to the left
* if there is a rock pick it up.
* if there is a rock, and already have a rock, drop the one that is being carried, pick up the new rock.
* if there is a web, and have a rock, drop rock and destroy web, then pick up rock.
* if there is a web and don't have rock, turn back 90 degrees to the left.

### Check left: check_left(rock):

The rock argument is a boolean value to indicate if the ant is carrying a rock.

The ant will turn 90 degrees to his left and after reviewing the situation decide on an action, as follows:
* if there is an exit, then escape.
* if there is an exit, but carrying a rock, then drop rock and escape
* if there is a wall turn back 90 degrees to the right
* if there is a rock pick it up.
* if there is a rock, and already have a rock, drop the one that is being carried, pick up the new rock.
* if there is a web, and have a rock, drop rock and destroy web, then pick up rock.
* if there is a web and don't have rock, turn back 90 degrees to the right.


### Making your own labyrinths

The Laby distribution includes 13 laby files with different labyrinth designs. 
These are in the folder `/usr/share/laby/levels/`. These text files commence with a map. for example

```
map:
o o o o o o
o w . . . x
o . . . . o
o . . . . o
o . ↑ . r o
o o o o o o
```

Where o is a wall, . is void, r is rock, w is web, x is exit. There are four arrow characters to indicate
the ant and the direction it is facing.

These files may be edited and additional files created, that contain your own labyrinth designs.







`

