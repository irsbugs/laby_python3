#!/usr/bin/env python3
# robot.py
#
# This is a version of robot.py that is modified for use with python3.
# It contains the original set of functions: 
# look, left, right, forward, take, drop, escape and say.
#
# Sub-functions output and input have been removed and replaced with python3
# builtin function input(). This resulted in the sys module no longer being 
# used, so it is not imported.
#
# There appears to be an issue with OCaml processing a "look\n" command. 
# As a work-around look() function is always performed twice.
# 
# Pre-requisites:
#
# 1. The Program window is loaded with code from /usr/share/laby/mods/python/skel
# Edit this skel and remove the semicolon on the first line "robot import *;"
#
# 2. Edit /usr/share/laby/mods/python/rules and change python to python3. i.e.
# need	python3
# spawn	python3 program.py
#
# Ian Stewart. 2020_05_16
#
def look():
    """
    look() needs to be performed twice. First time it may return "ok"
    Responses from look(): void, wall, rock, web, exit, unknown
    """
    response = input("look\n")
    response = input("look\n")
    if response == "quit":
        exit()
    return response


def left():
    response = input("left\n")
    return response


def right():
    response = input("right\n")
    return response


def forward():
    response = input("forward\n")
    return response


def take():
    response = input("take\n")
    return response


def drop():
    response = input("drop\n")
    return response


def escape():
    response = input("escape\n")
    return response


def say(s):
    "Prompt data is returned as the input. Displays in the Messages window."
    input("say " + s + "\n")


# Main program starts
response = input("start\n")
say("Ant is: {}".format(response))
