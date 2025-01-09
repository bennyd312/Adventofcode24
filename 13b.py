import numpy as np

def PennyPinch(equations):
    tokens = 0
    for equation in equations:
        tokens += CalculateTokens(equation)

    return tokens
def CalculateTokens(equation):
    A, B = EvaluateEquation(equation)
    tokens = 0
    if A!=-1 and B!=-1:
        tokens += 3*A + B

    return tokens

def EvaluateEquation(equation):
    Matrix = np.array([equation[0],
                  equation[1]])
    RHS = np.array([equation[2][0]+10000000000000,
                  equation[2][1]+10000000000000])
    sol = np.round(np.linalg.solve(Matrix,RHS))

    A = np.round(sol[0],5)
    B = np.round(sol[1],5)
    rules = [equation[0][0]*A+equation[0][1]*B == RHS[0],
             equation[1][0]*A+equation[1][1]*B == RHS[1]]
    if all(rules):
        return A,B
    else:
        return -1, -1

def TextToSystem(filenamestring):
    equations = []
    f = open(filenamestring,'r')
    equation = [[],[],[]]
    for line in f:
        stripped_line = line.rstrip()
        stripped_line = stripped_line.split(sep=' ')
        if stripped_line[0] == "Button":
            coeffs = [int(stripped_line[2][2:][:-1]),int(stripped_line[3][2:])]
            equation[0].append(coeffs[0])
            equation[1].append(coeffs[1])
        elif stripped_line[0] == "Prize:":
            coeffs = [int(stripped_line[1][2:][:-1]),int(stripped_line[2][2:])]
            equation[2].append(coeffs[0])
            equation[2].append(coeffs[1])
            equations.append(equation)
            equation = [[],[],[]]
        else:
            continue

    f.close()

    return equations

equations = TextToSystem('input.txt')
print(int(PennyPinch(equations)))
