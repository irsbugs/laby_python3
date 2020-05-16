import sys


def output(s):
    sys.stdout.write(s + "\n")
    sys.stdout.flush()


def input():
    line = sys.stdin.readline()
    if line == "quit\n":
        sys.exit(say("Quit"))
    return line


def left():
    output("left")
    input()


def right():
    output("right")
    input()


def forward():
    output("forward")
    input()


def take():
    output("take")
    input()


def drop():
    output("drop")
    input()


def escape():
    output("escape")
    input()


def say(s):
    output("say " + s)
    input()


Void = 0
Wall = 1
Rock = 2
Web = 3
Exit = 4
Unknown = 5


def look():
    output("look")
    ans = input()
    if (ans == "void\n"):
        return Void
    if (ans == "wall\n"):
        return Wall
    if (ans == "rock\n"):
        return Rock
    if (ans == "web\n"):
        return Web
    if (ans == "exit\n"):
        return Exit
    return Unknown


output("start")
input()
