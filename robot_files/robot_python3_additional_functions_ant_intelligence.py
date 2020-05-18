#!/usr/bin/env python3
# robot.py
#
# Saved as: robot_python3_additional_functions_ant_intelligence.py
# Ian Stewart. 2020-05-17
#
# The Program window is loaded with code from /usr/share/laby/mods/python/skel
# Edit this skel and remove the semicolon on the first line "robot import *;"
#
# Edit /usr/share/laby/mods/python/rules and change python to python3. i.e.
# need	python3
# spawn	python3 program.py
#
# Importing
import sys
import os
import time
import shutil

verbose = True

# === Original 7 x Robot functions start === 
# Functions modified to use python3 input() instead of sys.stdout / sys.stdin

def look():
    """
    look may need to be performed twice. First time it may return "ok"
    Maybe a timing issue?
    Responses from look(): void, wall, rock, web, exit, unknown
    """
    #response = input("look\n")
    response = input("look\n")
    if verbose: say("look: " + response) 
    if response == "quit":
        exit()
    return response


def left():
    response = input("left\n")
    if verbose: say("left: " + response)
    return response


def right():
    response = input("right\n")
    if verbose: say("right: " + response)
    return response


def forward():
    response = input("forward\n")
    if verbose: say("forward: " + response)
    return response


def take():
    response = input("take\n")
    if verbose: say("take: " + response)
    return response


def drop():
    response = input("drop\n")
    if verbose: say("drop: " + response)
    return response


def escape():
    response = input("escape\n")
    if verbose: say("escape: " + response)
    return response


def say(s):
    """
    The prompt data is returned as the input. Displays in the Messages window.
    """
    input("say " + s + "\n")


# === Original robot 7 x function calls end ===

# === Ant Official Intelligence start === 

def ant_official_intelligence(direction="right"):
    """
    This function in conjunction with drop_rock() and left_check() or 
    right_check() should allow the ant to pass through many labyrinth designs. 
    The ant will adhere to the following rules:

    Always check in one direction. See if there is a way forward having turned 
    in this direction. This may require removing a rock or destroying a web.

    Always carry a rock, if possible. If you come across another rock, drop
    the rock you have and get the new rock.
    """
    # Start without a rock
    rock = False

    # Main loop
    while True:

        # Check in the defined direction
        # What's on the right? Might be able to escape???  
        if direction == "right":
            rock = right_check(rock) 
        else:
            rock = left_check(rock)
        # Can ant go forward? May have just turned right.

        # If its an exit, have to drop rock to get out.
        if look() == "exit":
            if rock:
                drop_rock(rock)
                escape()
                sys.exit()
            else:
                escape()
                sys.exit()
        
        # If there is void in front, then go forward.  
        if look() == "void":
            forward()
            continue
         
        # Always take the rock in front, even if have to drop a rock behind
        if look() == "rock":
            # say("Have rock: " + str(rock))
            if rock:
                drop_rock(rock)
                take()
                rock = True
                forward()  # OK to go forward
                continue
            else:
                take()
                rock = True
                forward()  # OK to go forward
                continue
          
        if look() == "web":
            #say("Have rock: " + str(rock))
            if rock:
                # Throw a rock at the web, then pickup rock. Creates void.
                drop(), 
                take()       
                forward()  # OK to go forward
                continue
            else:
                # No rock to throw at web. Turn back and run away.
                if direction == "right":
                    left()
                else:
                    right()
                continue 
            
        # Hmmm all blocked up going forward or desired direction. 
        # Try turning in other direction to keep going.
        # say("Got to point where I need to turn away from desired direction")
        if direction == "right":
            left()
        else:
            right()

    sys.exit(say("Too hard. I give up!"))


def drop_rock(rock=True, rotate="right"):
    """
    If the ant has a rock then it will rotate right (or left) checking for 
    the first occurence of a void. The rock is dropped into this void and the
    ant returns to its original position.
    If a web is in front of an ant then the rock is dropped on the web and
    picked up again. 
    Could call gps_update(gps, action="right"), but after routine back to 
    original gps, so not really necessary?
    """
    if not rock:
        say("No rock to drop")
        return

    if look() == "web":
        # If a Web in front, destroy web and pick up again.
        drop()
        take()
        return

    # Get rid of rock via turns to the right:
    if rotate == "right":
        right()
        if look() == "void":
            drop()
            left()
            return
        else:
            right()
            if look() == "void":
                drop()
                left()
                left()
                return    
            else:
                right()
                if look() == "void":
                    drop()
                    right()
                    return              

    # Get rid of rock via turns to the left:
    if rotate == "left":
        left()
        if look() == "void":
            drop()
            right()
            return
        else:
            left()
            if look() == "void":
                drop()
                right()
                right()
                return    
            else:
                left()
                if look() == "void":
                    drop()
                    left()
                    return   


def right_check(rock):
    # Turn right and check out what ant is looking at
    # Drop through the checks with each thing it is not
    right()
 
    #say("Turned right and have Rock: " + str(rock))        

    # Is it an exit? If it was then escaped
    if look() == "exit":
        # If have rock, drop it then escape rock.
        if rock:
            rock = drop_rock(rock)
            escape()
            sys.exit()
  
    if look() == "wall":
        # A Wall. Turn back to original direction ready to go forward
        left()
        return rock

    if look() == "void":
        # A void. If so its the new road we want. Don't turn back
        return rock 

    if look() == "rock":
        # A Rock. Taking rock creates a void. But if carrying a rock drop it first.
        if rock:
            # Already have a rock. Drop it and get another one
            drop_rock(rock)
            take()
            return True
        else:
            take()
            return True

    if look() == "web":
        # Throw a rock at the web, then pickup rock and created void, etc
        if rock:
            drop()
            take()       
            return rock
        else:
            # No rock to throw at web. Turn back ...and run away.
            left()
            return rock

def left_check(rock):
    # Turn right and check out what ant is looking at
    # Drop through the checks with each thing it is not
    left()
 
    #say("Turned right and have Rock: " + str(rock))        

    # Is it an exit? If it was then escaped
    if look() == "exit":
        # If have rock, drop it then escape rock.
        if rock:
            rock = drop_rock(rock, "left")
            escape()
            sys.exit()
  
    if look() == "wall":
        # A Wall. Turn back to original direction ready to go forward
        right()
        return rock

    if look() == "void":
        # A void. If so its the new road we want. Don't turn back
        return rock 

    if look() == "rock":
        # A Rock. Taking rock creates a void. But if carrying a rock drop it first.
        if rock:
            # Already have a rock. Drop it and get another one
            drop_rock(rock, "left")
            take()
            return True
        else:
            take()
            return True

    if look() == "web":
        # Throw a rock at the web, then pickup rock and created void, etc
        if rock:
            drop()
            take()       
            return rock
        else:
            # No rock to throw at web. Turn back ...and run away.
            right()
            return rock

# === Ant Official Intelligence end ===

# === Grid related start ===

def create_grid(grid_max = 21):
    """ 
    Create in memory a list array called grid
    Fill it with * data to show its empty
    In the middle at the 0,0 coordinates place a "0"
    """
    # Start with an empty grid - i.e. *
    data = "*"

    grid = [[data for i in range(grid_max)] 
                  for j in range(grid_max)]

    # Insert the starting point in the middle at 0,0
    offset = grid_max // 2
    grid[0 + offset][0 + offset] = "0"
    return grid


def xaxis_label(grid_max):
    """
    Called by rotate_grid(grid). Uses global grid max
    Create the X-Axis labelling. For example -10 to +10
    0 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 0 
    1 - - - - - - - - -                     1 
    -                                         
                                              
    X Axis
    """
    x_axis_label = "X Axis"

    xaxis_postive_range = (grid_max // 2) + 1  # 11
    xaxis_negative_range = (grid_max // 2) * -1 # -10
    s = ""
    t = ""
    u = ""
    v = ""
    for value in range(xaxis_negative_range, xaxis_postive_range):
        string = "{: >4}".format(value)
        print(string)
        s += "{} ".format(string[-4:-3])
        t += "{} ".format(string[-3:-2])
        u += "{} ".format(string[-2:-1])
        v += "{} ".format(string[-1:])

    return v + "\n" + u + "\n" + t + "\n" + s + "\n" + x_axis_label + "\n"

def rotate_grid(grid, grid_max):
    """
    # Grid list is rotated 90 degree anti-clockwise 
    # Requires grid_max value which is odd for -, 0, +
    """
    y_axis_label = ["Y", " ", "A","x","i","s"]
    offset = grid_max // 2

    s = ""
    count = offset * -1
    for k in range(grid_max):
        grid_row_list = []
        for i in reversed(range(grid_max)):
            j = (grid_max - 1) - k
            grid_row_list.append(grid[i][j])

        # Reverse the temp row list
        grid_row_list = list(reversed(grid_row_list))   
        for index in range(grid_max):
            s += "{} ".format(grid_row_list[index])

        if k < 6:
            s1 = y_axis_label[k]
        else:
            s1 = ""

        s += "{: >3} {}\n".format(count, s1)
        count += 1

    # Build the X Axis labelling
    s += xaxis_label(grid_max)
    return s


def write_grid(grid_string):
    with open(grid_full_path_file, "w") as fout:
        fout.write(grid_string)    


def get_look():
    """
    Use look to find what is in front.
    Return symbol for use in ploting the grid
    """
    found = look()
    if found == "void":
        return "."
    elif found == "wall":
        return "o"
    elif found == "rock":
        return "r"
    elif found == "web":
        return "w"
    elif found == "exit":
        return "x"
    else:
        return "?"


def plot_360(grid, gps, grid_max):
    """
    Uses the gps position relative to the offset

    The ant rotates 4 times 90 degrees to get a look() at each square NESW of
    current position. 
    """
    # Don't replot current position unless its 0,0 = start
    #if x == 0 and y == 0:
    #  grid[x + o][y + o] = "s"
    # Look around and get four points onto grid
    
    # Get x and y 
    x = gps[0]
    y = gps[1]
    #  Determine the offset for the grid
    o = grid_max // 2
    # Get current direction
    direction = gps[2]
    # Ensure ant is facing "north"
    if direction == 0:
        pass
    if direction == 1:
        left()
    if direction == 2:
        left(), left()
    if direction == 3:
        left(), left(), left()  

    # Update the grid on the 4 x surrounding squares 
    grid[x + o][y + o + 1] = get_look()
    right()

    grid[x + o + 1][y + o] = get_look()  
    right()

    grid[x + o][y + o -1] = get_look()  
    right()

    grid[x + o -1][y + o] = get_look() 
    #Back to facing in original north position  
    right()

    # Restore original direction
    if direction == 0:
        pass
    if direction == 1:
        right()
    if direction == 2:
        right(), right()
    if direction == 3:
        right(), right(), right() 
    
    # Put in start each time, it might get over-ridden
    grid[0 + o][0 + o] = "s"
    return grid

def ant_position(gps, grid_max):
    #place the ant in the grid
    # Allow for grid is 90 rotated
    # Get x and y 
    x = gps[0]
    y = gps[1]
    d = gps[2]
    #  Determine the offset for the grid
    o = grid_max // 2
    # Get current direction
    # With python3 should be able to use arrows chr(8592) to chr(8595)
    if d == 0:
      ant = "↑"
    if d == 1:
      ant = "→"
    if d == 2:
      ant = "↓"
    if d == 3:
      ant = "←"
    # Update ant position on grid    
    grid[x + o][y + o] = ant
    #write_grid(grid)  
    #grid_string = rotate_grid(grid, grid_max)
    #write_grid(grid_string)
    

# === Grid related end

# === GPS start ===

def gps_update(gps, action="forward", verbose=False, log=False):
    """
    Receive the gps [x,y,d] list and update it based on the action supplied.
    Return the updated gps list.
    """
    # Define constants for index into the gps list
    X = 0
    Y = 1
    D = 2
	 # Direction Values: North, East, South and West
    N = 0
    E = 1
    S = 2
    W = 3
	 # Escape action is equivalent to forward
    if action == "escape":
        action = "forward"
 
    if action == "forward":
        if gps[D] == N:  # North   
            gps[Y] += 1
        elif gps[D] == E:  # East
            gps[X] += 1
        elif gps[D] == S:  # South
            gps[Y] -= 1
        elif gps[D] == W:  # West 
            gps[X] -= 1     
                    
    elif action == "left":
        gps[D] -= 1
        if gps[D] == -1:
            gps[D] = 3

    elif action == "right":
        gps[D] += 1
        if gps[D] == 4:
            gps[D] = 0

    else:
        say("Warning: {} is an invalid action to pass to gps_update function.".
            format(action))

    if verbose:
        say("gps = [" + str(gps[X]) + ", " 
                      + str(gps[Y]) +", " 
                      + str(gps[D]) + "]")   

    if log:
        gps_log(gps)
                                              
    return gps


def gps_log(gps):
    """
    Log the gps list data [x, y and direction] as comma seperated values
    in gps_data file.
    """
    with open(gps_full_path_file, mode="a") as fout:
        s = ""
        for item in gps:
            s = s + str(item) + ", "
        fout.write(s[:-2] + "\n")

# === GPS end ===

# === Backup ===
def backup(verbose=False):
    """
    Upon clicking the "Execute" button, the code you have written is copied
    to and ant folder off /tmp. Use os.getcwd() to identify the /tmp folder.
    The code is copied to the file program.py.
    This backup function copies the program.py file to folder: ~/laby_data/.
    The file name includes a timestamp. E.g.  program_2020-12-31_23:59.py
    Requires: shutil, os modules 
    """        
    if os.path.isfile("program.py"):
        shutil.copy2("program.py", program_dest_path_file)
        if verbose:
            say("program.py backed up to: " + program_dest_path_file)
    else:
        say("Backup failed")


# === Platform check ===
def platform_check():
    """
    Must be on a linux platform
    """
    if sys.platform != 'linux':
        say("Error: Only supported on the Linux platform. Exiting")
        time.sleep(1)
        sys.exit()


# === Python check
def python_check():
    """
    Check the version of python. Exit if on Version 2
    """
    if sys.version_info < (3,):
        say("Error: Python 3 is required.")
        say("Edit: /usr/share/laby/mods/python/rules")
        say("Change python to python3")
        say("Exiting")
        time.sleep(1)
        sys.exit()


# ===== Main program begins =====
response = input("start\n")
say("Ant is: {}".format(response))

# Checks
platform_check()
python_check()

# Establish path constants
# Create directory ~/laby_data/ for program.py and gps.csv data
# Filenames include a timestamp.
ts = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

home_path = os.path.expanduser("~")
dir_name = "laby_data"
full_path = home_path + os.sep + dir_name

if not os.path.exists(full_path):
    os.makedirs(full_path)


# For backups
program_file_name = "program_" + ts + ".py"
program_dest_path_file = full_path + os.sep + program_file_name

# For laby data. Either new name each time, or overwrite gps.csv
#gps_file_name = "gps_" + ts + ".csv"
gps_file_name = "gps.csv"
gps_full_path_file = full_path + os.sep + gps_file_name

# Create new blank gps data file, overwrite old
with open(gps_full_path_file, mode="w"): pass

# For grid. Either new name each time, or overwrite gps.csv
#gps_file_name = "gps_" + ts + ".csv"
grid_file_name = "grid"
grid_full_path_file = full_path + os.sep + grid_file_name


