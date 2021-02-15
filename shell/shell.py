#! /usr/bin/env python3
import os,sys,re
#loop
while True:
    if 'PS1' in os.environ:
        os.write(1, (os.environ['PS1']).encode())
    else:
        os.write(1, ("$ ").encode())
    args = os.read(0, 1024)
    if len(args) == 0:
        break
    args = args.decode().splitlines()
    for arg in args:
        execute(arg.split())

#execute progs
def execute(args):
    if len(args)  == 0:
        return
    elif args[0].lower() == "exit":
        syst.exit(0)
        
    else:
        rc = os.fork()
        background = True

        if rc < 0:
            os.write(2, ("Fork Failed, Returning %d\n" % rc).encode())
            sys.exit(1)
        elif rc == 0:
            if "/" in args[0]:
                prog = args[0]
                try:
                    os.execve(prog, args, os.environ)
                    try:
                        os.execve(prog, args, os.environ)
                    except FileNotFoundError:
                        pass
            else:
                for dir in re.split(":", os.environ['PATH']:
                    prog = "%s/%s" % (dir, args[0])
                    try:
                        os.execve(prog, args, os.environ)
                    except FileNotFoundError:
                        pass
            os.write(2, ("Invalid command\n").encode())
            sys.exit(0)
        else:
            if background:
                childpid = os.wait()
                                    
                        
