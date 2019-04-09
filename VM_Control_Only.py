
def Main():
    pass
# VM Control

def goto(labelname):
    return "@" + str(labelname) + "\n0;JMP\n"

def if_goto(labelname):
    return pop_D() + "D=D+1\n@" + str(labelname) + "\nD;JGT\n"
    # my understanding is if-goto jumps if top of stack is -1 (true) i.e. pop_D() + D=D+1 + D;JEQ

def label(labelname):
    return "(" + str(labelname) + ")\n"

RETURN_ADDRESSES = []

callnum = -1
def callFunction(FunctionName, nArgs):
    callnum += 1
    RETURN_ADDRESS = str(FunctionName) + str(callnum)
    RETURN_ADDRESSES.append(RETURN_ADDRESS)
    str = "@" + RETURN_ADDRESS + "\nD=A\n" + push_D()
    str += saveFrame(LCL) + saveFrame(ARG) + saveFrame(THIS) + saveFrame(THAT)
    str += "@SP\nD=M\n@" + (5 + int(nArgs)) + "\nD=D-A\n@ARG\nM=D\n"
    str += "@SP\nD=M\n@LCL\nM=D\n"
    str += goto(str(FunctionName))
    str += "(" + RETURN_ADDRESS + ")\n"
    return str

# Helper function for callFunction
def saveFrame(name):
    return "@" + str(name) + "\nD=M\n" + push_D()

def makeFunction(FunctionName, nVars):
    str = label(str(FunctionName))
    for i in range(nVars):
        str += "D=0\n" + push_D()
    return str

def return_control():
    str = "@LCL\nD=M\n@endFrame\nM=D\n"
    str += "@5\nD=A\n@endFrame\nD=M-D\n@returnAddress\nM=D\n"
    str += pop_D() + "@ARG\nM=D\n"
    str += "@SP\nM=D+1\n"
    str += "@endFrame\nD=M\n" + "@THAT\nDM=D-1\n" + "@THIS\nDM=D-1\n" + "@ARG\nDM=D-1\n" + "@LCL\nM=D-1\n"
    str += goto(RETURN_ADDRESSES[-1])
    RETURN_ADDRESSES.pop()
    return str

if __name__ == '__main__':
    main()
