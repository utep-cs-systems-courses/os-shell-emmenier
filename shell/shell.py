#! /usr/bin/env python3
import Helper
import os,sys,re
#loop
while True:
    if 'PS1' in os.environ:
        os.write(1, (os.environ['PS1']).encode())
    else:
        os.write(1, ("$ ").encode())
    args = myGetLine()
    
    if len(args) == 0:
        break

    splitArgs = args.split()

    if splitArgs[0].lower() = "exit":
        sys.exit(1)
        
    execute(args)
    
#execute arguments
def execute(args):
    if len(args)  == 0:
        return
    
    elif args[0] == "cd":
        try:
            if len(args) == 1:
                os.chdir("..")
            else:
                os.chdir(args[1])
        except:
            os.write(1, ("cd %s: No such file or directory" % args[1]).encode())
            pass
    elif "|" in args:
        #insert method here

    else:
        rc = os.fork()
        background = True
        
        if "&" in args:
            args.remove("&")
            background = False
        if rc < 0:
            os.write(2, ("Fork failed, returning %d\n" % rc).encode())
            sys.exit(1)
        elif rc == 0:
            
            if "/" in args[0]:
                prog = args[0]
                try:
                    os.execve(prog, args, os.environ)
                except FileNotFoundError:
                    pass

            elif ">" in args or "<" in args:
                redirect(args)

            else:
                for dir in re.split(":", os.eviron['PATH']):
                    prog = "%s/%s" % (dir, args[0])

                    try:
                        os.execve(prog, args, os.environ)
                    except FileNotFoundError:
                        pass
            os.write(2, ("Command not found\n").encode())
            sys.exit(0)
        else:
            if background:
                childpid = os.wait()
                    
            
def redirect():
    if ">" in args:
        os.close(1)
        os.open(args[args.index(">")+1], os.0_CREAT | os.0_WRONLY)
        os.set_inheritable(1, True)
        args.remove(args[args.index(">") + 1])
        args.remove(">")

    else:
        os.close(0)
        os.open(args[args.index("<") + 1], os.0_RDONLY)
        os.set_inheritable(1, True)
        args.remove(args[args.index("<" +1])
        args.remove("<")

    for dir in re.split(":", os.environ["PATH"]):
        prog = "%s/%s" % (dir, args[0])
        try:
            os.execve(prog, args, os.environ)
        except FileNotFoundError:
            pass
        os.write(2, ("%s: Command not found\n" % args[0]).encode())
        sys.exit(0)

def pipe():
    left = args[0:args.index("|")]
    right = args[args.index("|") + 1:]
    pRead, pWrite = os.pipe()
    rc = os.fork()

    if rc < 0:
        os.write(2, ("Fork failed, returning %d\n" % rc).encode())
        sys.exit(1)
    elif rc == 0:
        os.close(1)
        os.dup(pw)
        os.set_inheritable(1, True)
        for fd in (pRead, pWrite):
            os.close(fd)
        command(left)
        os.write(2, ("Could not exec %s\n" % left[0]).encode())
        sys.exit(1)
    else:
        os.close(0)
        os.dup(pRead)
        os.set_inheritable(0, True)
        for fd in (pWrite, pRead):
            os.close(fd)
        if "|" in right:
            pipe(right)
        command(right)
        os.write(2, ("Could not exec %s\n" % right[0]).encode())
        sys.exit(1)

def command(args):
    if "/" in args[0]:
        prog = args[0]
        try:
            os.execve(prog, args, os.environ)
        except FileNotFoundError:
            pass
    elif ">" in args or "<" in args:
        redirect(args)
    else:
        for dir in re.split(":", os.environ['PATH']):
            prog = "%s%s" % (dir, args[0])
            try:
                os.execve(prog, args, os.environ)
            except FileNotFoundError:
                    pass
                    
