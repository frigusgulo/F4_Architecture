
def Main():
    pass

def goto(labelname):
    return "@" + str(labelname) + "\n0;JMP\n"

def if_goto(labelname):
    # pop_D() = "@SP\nAM=M-1\nD=M\nM=0\n"
    return "@SP\nAM=M-1\nD=M\nM=0\n" + "@" + str(labelname) + "\nD;JGT\n"
    # my understanding is if-goto jumps if top of stack is -1 (true) i.e. pop_D() + D=D+1 + D;JEQ

def label(labelname):
    return "(" + str(labelname) + ")\n"

callnum = -1
def callFunction(FunctionName, nArgs):
    # TODO push_D() "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
    callnum += 1
    str = "@" + str(FunctionName) + callnum + "\nD=A\n" + "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
    str += saveFrame(LCL) + saveFrame(ARG) + saveFrame(THIS) + saveFrame(THAT)
    str += "@SP\nD=M\n@5\nD=D-A\n@" + int(nArgs) + "\nD=D-A\n@ARG\nM=D\n"
    str += "@SP\nD=M\n@LCL\nM=D\n"
    str += goto(str(FunctionName))
    str += "(" + str(FunctionName) + callnum + ")\n"

    return str

def saveFrame(name):
    # TODO push_D() "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
    return "@" + str(name) + "\nD=A\n" + "@SP\nA=M\nM=D\n@SP\nM=M+1\n"

def makeFunction(FunctionName, nVars):
    # TODO push_D() "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
    str = label(FunctionName)
    for i in range(nVars):
        str += "D=0\n" + "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
    # label(FunctionName) + nVars * (D=0 + push_D())
    return str

def return():
    # TODO push_D() "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
    str = "@LCL\nD=M\n@endFrame\nM=D\n"
    str += "@5\nD=A\n@endFrame\nD=M-D\n@returnAddress\nM=D\n"
    str += "@SP\nA=M\nM=D\n@SP\nM=M+1\n" + "@ARG\nM=D\n"
    str += "@SP\nM=D+1\n"
    str += "@endFrame\nD=M\n@THAT\nDM=D-1\n" + "@THIS\nDM=D-1\n" + "@ARG\nDM=D-1\n" + "@LCL\nM=D-1\n"
    str += goto(returnAddress)
    return str

if __name__ == '__main__':
    main()
