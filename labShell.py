#! /usr/bin/env python3

import os, sys, time, re

userInput = input("$")
while userInput != "quit":
    if userInput == "lab1":
        pid = os.getpid()

        os.write(1, ("About to fork (pid:%d)\n" % pid).encode())

        rc = os.fork()

        if rc < 0:
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)

        elif rc == 0:                   # child
            os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" % 
                 (os.getpid(), pid)).encode())
            args = ["wordCountTest.py", "speech.txt","mySpeechKey.txt","speechKey.txt"]
            for dir in re.split(":", os.environ['PATH']): # try each directory in the path
                program = "%s/%s" % (dir, args[0])
                os.write(1, ("Child:  ...trying to exec %s\n" % program).encode())
                try:
                    os.execve(program, args, os.environ) # try to exec program
                except FileNotFoundError:             # ...expected
                    pass                              # ...fail quietly

                os.write(2, ("Child:    Could not exec %s\n" % args[0]).encode())
                sys.exit(1)                 # terminate with error

        else:                           # parent (forked ok)
            os.write(1, ("Parent: My pid=%d.  Child's pid=%d\n" % 
                         (pid, rc)).encode())
            childPidCode = os.wait()
            os.write(1, ("Parent: Child %d terminated with exit code %d\n" % 
                 childPidCode).encode())
            userInput = input("$")

    elif userInput == "fork":
        pid = os.getpid()

        os.write(1, ("About to fork (pid:%d)\n" % pid).encode())

        rc = os.fork()

        if rc < 0:
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)
        elif rc == 0:                   # child
            os.write(1, ("I am child.  My pid==%d.  Parent's pid=%d\n" % (os.getpid(), pid)).encode())
            userInput = input("$")
        else:                           # parent (forked ok)
            os.write(1, ("I am parent.  My pid=%d.  Child's pid=%d\n" % (pid, rc)).encode())
            userInput = input("$")
            
    elif userInput == ">Lab1":
        pid = os.getpid()
        os.write(1, ("About to fork (pid=%d)\n" % pid).encode())

        rc = os.fork()

        if rc < 0:
            os.write(2, ("Fork failed, returning %d\n"% rc).encode())
            sys.exit(1)
        elif rc == 0:
            os.write(1, ("Child: M pid==%d. Parent's pid=%d\n" %
                         (os.getpid(), pid)).encode())
            args = ["wordCountTest.py", "speech.txt","mySpeechKey.txt","speechKey.txt"]

            os.close(1)
            sys.stdout = open("p4-output.txt", "w")
            fd = sys.stdout.fileno()
            os.set_inheritable(fd, True)
            os.write(2, ("Child: opend fd=%d for writing\n" %fd).encode())

            for dir in re.split(":", os.environ['PATH']): # try each directory in path
                program = "%s/%s" % (dir, args[0])
                try:
                    os.execve(program, args, os.environ) # try to exec program
                except FileNotFoundError:             # ...expected
                    pass                              # ...fail quietly 

            os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
            sys.exit(1)                 # terminate with error

        else:                           # parent (forked ok)
            os.write(1, ("Parent: My pid=%d.  Child's pid=%d\n" % 
                 (pid, rc)).encode())
            childPidCode = os.wait()
            os.write(1, ("Parent: Child %d terminated with exit code %d\n" % 
                 childPidCode).encode())
            userInput = input("$")

            

