#!/usr/bin/python
# Solving rubiks cube

print "#####  Rubiks cube solver  #####"

w = 48
tempMatrix = [0 for x in range(w)]
workingMatrix = [0 for x in range(w)]
startMatrix = [0 for x in range(w)]
checkMatrix = [0 for x in range(w)]


def R(workingMatrix):
    tempMatrix[0] = workingMatrix[0]
    tempMatrix[1] = workingMatrix[1]
    tempMatrix[2] = workingMatrix[34]
    tempMatrix[3] = workingMatrix[35]
    tempMatrix[4] = workingMatrix[36]
    tempMatrix[5] = workingMatrix[5]
    tempMatrix[6] = workingMatrix[6]
    tempMatrix[7] = workingMatrix[7]
    tempMatrix[8] = workingMatrix[14]
    tempMatrix[9] = workingMatrix[15]
    tempMatrix[10] = workingMatrix[8]
    tempMatrix[11] = workingMatrix[9]
    tempMatrix[12] = workingMatrix[10]
    tempMatrix[13] = workingMatrix[11]
    tempMatrix[14] = workingMatrix[12]
    tempMatrix[15] = workingMatrix[13]
    tempMatrix[16] = workingMatrix[44]
    tempMatrix[17] = workingMatrix[17]
    tempMatrix[18] = workingMatrix[18]
    tempMatrix[19] = workingMatrix[19]
    tempMatrix[20] = workingMatrix[20]
    tempMatrix[21] = workingMatrix[21]
    tempMatrix[22] = workingMatrix[42]
    tempMatrix[23] = workingMatrix[43]
    tempMatrix[24] = workingMatrix[24]
    tempMatrix[25] = workingMatrix[25]
    tempMatrix[26] = workingMatrix[26]
    tempMatrix[27] = workingMatrix[27]
    tempMatrix[28] = workingMatrix[28]
    tempMatrix[29] = workingMatrix[29]
    tempMatrix[30] = workingMatrix[30]
    tempMatrix[31] = workingMatrix[31]
    tempMatrix[32] = workingMatrix[32]
    tempMatrix[33] = workingMatrix[33]
    tempMatrix[34] = workingMatrix[22]
    tempMatrix[35] = workingMatrix[23]
    tempMatrix[36] = workingMatrix[16]
    tempMatrix[37] = workingMatrix[37]
    tempMatrix[38] = workingMatrix[38]
    tempMatrix[39] = workingMatrix[39]
    tempMatrix[40] = workingMatrix[40]
    tempMatrix[41] = workingMatrix[41]
    tempMatrix[42] = workingMatrix[2]
    tempMatrix[43] = workingMatrix[3]
    tempMatrix[44] = workingMatrix[4]
    tempMatrix[45] = workingMatrix[45]
    tempMatrix[46] = workingMatrix[46]
    tempMatrix[47] = workingMatrix[47]

    return tempMatrix


def U(workingMatrix):
    tempMatrix[0] = workingMatrix[8]
    tempMatrix[1] = workingMatrix[9]
    tempMatrix[2] = workingMatrix[10]
    tempMatrix[3] = workingMatrix[3]
    tempMatrix[4] = workingMatrix[4]
    tempMatrix[5] = workingMatrix[5]
    tempMatrix[6] = workingMatrix[6]
    tempMatrix[7] = workingMatrix[7]
    tempMatrix[8] = workingMatrix[16]
    tempMatrix[9] = workingMatrix[17]
    tempMatrix[10] = workingMatrix[18]
    tempMatrix[11] = workingMatrix[11]
    tempMatrix[12] = workingMatrix[12]
    tempMatrix[13] = workingMatrix[13]
    tempMatrix[14] = workingMatrix[14]
    tempMatrix[15] = workingMatrix[15]
    tempMatrix[16] = workingMatrix[24]
    tempMatrix[17] = workingMatrix[25]
    tempMatrix[18] = workingMatrix[26]
    tempMatrix[19] = workingMatrix[19]
    tempMatrix[20] = workingMatrix[20]
    tempMatrix[21] = workingMatrix[21]
    tempMatrix[22] = workingMatrix[22]
    tempMatrix[23] = workingMatrix[23]
    tempMatrix[24] = workingMatrix[0]
    tempMatrix[25] = workingMatrix[1]
    tempMatrix[26] = workingMatrix[2]
    tempMatrix[27] = workingMatrix[27]
    tempMatrix[28] = workingMatrix[28]
    tempMatrix[29] = workingMatrix[29]
    tempMatrix[30] = workingMatrix[30]
    tempMatrix[31] = workingMatrix[31]
    tempMatrix[32] = workingMatrix[32]
    tempMatrix[33] = workingMatrix[33]
    tempMatrix[34] = workingMatrix[34]
    tempMatrix[35] = workingMatrix[35]
    tempMatrix[36] = workingMatrix[36]
    tempMatrix[37] = workingMatrix[37]
    tempMatrix[38] = workingMatrix[38]
    tempMatrix[39] = workingMatrix[39]
    tempMatrix[40] = workingMatrix[46]
    tempMatrix[41] = workingMatrix[47]
    tempMatrix[42] = workingMatrix[40]
    tempMatrix[43] = workingMatrix[41]
    tempMatrix[44] = workingMatrix[42]
    tempMatrix[45] = workingMatrix[43]
    tempMatrix[46] = workingMatrix[44]
    tempMatrix[47] = workingMatrix[45]

    return tempMatrix


def F(workingMatrix):
    tempMatrix[0] = workingMatrix[6]
    tempMatrix[1] = workingMatrix[7]
    tempMatrix[2] = workingMatrix[0]
    tempMatrix[3] = workingMatrix[1]
    tempMatrix[4] = workingMatrix[2]
    tempMatrix[5] = workingMatrix[3]
    tempMatrix[6] = workingMatrix[4]
    tempMatrix[7] = workingMatrix[5]
    tempMatrix[8] = workingMatrix[46]
    tempMatrix[9] = workingMatrix[9]
    tempMatrix[10] = workingMatrix[10]
    tempMatrix[11] = workingMatrix[11]
    tempMatrix[12] = workingMatrix[12]
    tempMatrix[13] = workingMatrix[13]
    tempMatrix[14] = workingMatrix[44]
    tempMatrix[15] = workingMatrix[45]
    tempMatrix[16] = workingMatrix[16]
    tempMatrix[17] = workingMatrix[17]
    tempMatrix[18] = workingMatrix[18]
    tempMatrix[19] = workingMatrix[19]
    tempMatrix[20] = workingMatrix[20]
    tempMatrix[21] = workingMatrix[21]
    tempMatrix[22] = workingMatrix[22]
    tempMatrix[23] = workingMatrix[23]
    tempMatrix[24] = workingMatrix[24]
    tempMatrix[25] = workingMatrix[25]
    tempMatrix[26] = workingMatrix[32]
    tempMatrix[27] = workingMatrix[33]
    tempMatrix[28] = workingMatrix[34]
    tempMatrix[29] = workingMatrix[29]
    tempMatrix[30] = workingMatrix[30]
    tempMatrix[31] = workingMatrix[31]
    tempMatrix[32] = workingMatrix[14]
    tempMatrix[33] = workingMatrix[15]
    tempMatrix[34] = workingMatrix[8]
    tempMatrix[35] = workingMatrix[35]
    tempMatrix[36] = workingMatrix[36]
    tempMatrix[37] = workingMatrix[37]
    tempMatrix[38] = workingMatrix[38]
    tempMatrix[39] = workingMatrix[39]
    tempMatrix[40] = workingMatrix[40]
    tempMatrix[41] = workingMatrix[41]
    tempMatrix[42] = workingMatrix[42]
    tempMatrix[43] = workingMatrix[43]
    tempMatrix[44] = workingMatrix[26]
    tempMatrix[45] = workingMatrix[27]
    tempMatrix[46] = workingMatrix[28]
    tempMatrix[47] = workingMatrix[47]

    return tempMatrix


def L(workingMatrix):
    tempMatrix[0] = workingMatrix[40]
    tempMatrix[1] = workingMatrix[1]
    tempMatrix[2] = workingMatrix[2]
    tempMatrix[3] = workingMatrix[3]
    tempMatrix[4] = workingMatrix[4]
    tempMatrix[5] = workingMatrix[5]
    tempMatrix[6] = workingMatrix[46]
    tempMatrix[7] = workingMatrix[47]
    tempMatrix[8] = workingMatrix[8]
    tempMatrix[9] = workingMatrix[9]
    tempMatrix[10] = workingMatrix[10]
    tempMatrix[11] = workingMatrix[11]
    tempMatrix[12] = workingMatrix[12]
    tempMatrix[13] = workingMatrix[13]
    tempMatrix[14] = workingMatrix[14]
    tempMatrix[15] = workingMatrix[15]
    tempMatrix[16] = workingMatrix[16]
    tempMatrix[17] = workingMatrix[17]
    tempMatrix[18] = workingMatrix[38]
    tempMatrix[19] = workingMatrix[39]
    tempMatrix[20] = workingMatrix[32]
    tempMatrix[21] = workingMatrix[21]
    tempMatrix[22] = workingMatrix[22]
    tempMatrix[23] = workingMatrix[23]
    tempMatrix[24] = workingMatrix[30]
    tempMatrix[25] = workingMatrix[31]
    tempMatrix[26] = workingMatrix[24]
    tempMatrix[27] = workingMatrix[25]
    tempMatrix[28] = workingMatrix[26]
    tempMatrix[29] = workingMatrix[27]
    tempMatrix[30] = workingMatrix[28]
    tempMatrix[31] = workingMatrix[29]
    tempMatrix[32] = workingMatrix[0]
    tempMatrix[33] = workingMatrix[33]
    tempMatrix[34] = workingMatrix[34]
    tempMatrix[35] = workingMatrix[35]
    tempMatrix[36] = workingMatrix[36]
    tempMatrix[37] = workingMatrix[37]
    tempMatrix[38] = workingMatrix[6]
    tempMatrix[39] = workingMatrix[7]
    tempMatrix[40] = workingMatrix[20]
    tempMatrix[41] = workingMatrix[41]
    tempMatrix[42] = workingMatrix[42]
    tempMatrix[43] = workingMatrix[43]
    tempMatrix[44] = workingMatrix[44]
    tempMatrix[45] = workingMatrix[45]
    tempMatrix[46] = workingMatrix[18]
    tempMatrix[47] = workingMatrix[19]

    return tempMatrix


def B(workingMatrix):
    tempMatrix[0] = workingMatrix[0]
    tempMatrix[1] = workingMatrix[1]
    tempMatrix[2] = workingMatrix[2]
    tempMatrix[3] = workingMatrix[3]
    tempMatrix[4] = workingMatrix[4]
    tempMatrix[5] = workingMatrix[5]
    tempMatrix[6] = workingMatrix[6]
    tempMatrix[7] = workingMatrix[7]
    tempMatrix[8] = workingMatrix[8]
    tempMatrix[9] = workingMatrix[9]
    tempMatrix[10] = workingMatrix[36]
    tempMatrix[11] = workingMatrix[37]
    tempMatrix[12] = workingMatrix[38]
    tempMatrix[13] = workingMatrix[13]
    tempMatrix[14] = workingMatrix[14]
    tempMatrix[15] = workingMatrix[15]
    tempMatrix[16] = workingMatrix[22]
    tempMatrix[17] = workingMatrix[23]
    tempMatrix[18] = workingMatrix[16]
    tempMatrix[19] = workingMatrix[17]
    tempMatrix[20] = workingMatrix[18]
    tempMatrix[21] = workingMatrix[19]
    tempMatrix[22] = workingMatrix[20]
    tempMatrix[23] = workingMatrix[21]
    tempMatrix[24] = workingMatrix[42]
    tempMatrix[25] = workingMatrix[25]
    tempMatrix[26] = workingMatrix[26]
    tempMatrix[27] = workingMatrix[27]
    tempMatrix[28] = workingMatrix[28]
    tempMatrix[29] = workingMatrix[29]
    tempMatrix[30] = workingMatrix[40]
    tempMatrix[31] = workingMatrix[41]
    tempMatrix[32] = workingMatrix[32]
    tempMatrix[33] = workingMatrix[33]
    tempMatrix[34] = workingMatrix[34]
    tempMatrix[35] = workingMatrix[35]
    tempMatrix[36] = workingMatrix[30]
    tempMatrix[37] = workingMatrix[31]
    tempMatrix[38] = workingMatrix[24]
    tempMatrix[39] = workingMatrix[39]
    tempMatrix[40] = workingMatrix[10]
    tempMatrix[41] = workingMatrix[11]
    tempMatrix[42] = workingMatrix[12]
    tempMatrix[43] = workingMatrix[43]
    tempMatrix[44] = workingMatrix[44]
    tempMatrix[45] = workingMatrix[45]
    tempMatrix[46] = workingMatrix[46]
    tempMatrix[47] = workingMatrix[47]

    return tempMatrix


def D(workingMatrix):
    tempMatrix[0] = workingMatrix[0]
    tempMatrix[1] = workingMatrix[1]
    tempMatrix[2] = workingMatrix[2]
    tempMatrix[3] = workingMatrix[3]
    tempMatrix[4] = workingMatrix[28]
    tempMatrix[5] = workingMatrix[29]
    tempMatrix[6] = workingMatrix[30]
    tempMatrix[7] = workingMatrix[7]
    tempMatrix[8] = workingMatrix[8]
    tempMatrix[9] = workingMatrix[9]
    tempMatrix[10] = workingMatrix[10]
    tempMatrix[11] = workingMatrix[11]
    tempMatrix[12] = workingMatrix[4]
    tempMatrix[13] = workingMatrix[5]
    tempMatrix[14] = workingMatrix[6]
    tempMatrix[15] = workingMatrix[15]
    tempMatrix[16] = workingMatrix[16]
    tempMatrix[17] = workingMatrix[17]
    tempMatrix[18] = workingMatrix[18]
    tempMatrix[19] = workingMatrix[19]
    tempMatrix[20] = workingMatrix[12]
    tempMatrix[21] = workingMatrix[13]
    tempMatrix[22] = workingMatrix[14]
    tempMatrix[23] = workingMatrix[23]
    tempMatrix[24] = workingMatrix[24]
    tempMatrix[25] = workingMatrix[25]
    tempMatrix[26] = workingMatrix[26]
    tempMatrix[27] = workingMatrix[27]
    tempMatrix[28] = workingMatrix[20]
    tempMatrix[29] = workingMatrix[21]
    tempMatrix[30] = workingMatrix[22]
    tempMatrix[31] = workingMatrix[31]
    tempMatrix[32] = workingMatrix[38]
    tempMatrix[33] = workingMatrix[39]
    tempMatrix[34] = workingMatrix[32]
    tempMatrix[35] = workingMatrix[33]
    tempMatrix[36] = workingMatrix[34]
    tempMatrix[37] = workingMatrix[35]
    tempMatrix[38] = workingMatrix[36]
    tempMatrix[39] = workingMatrix[37]
    tempMatrix[40] = workingMatrix[40]
    tempMatrix[41] = workingMatrix[41]
    tempMatrix[42] = workingMatrix[42]
    tempMatrix[43] = workingMatrix[43]
    tempMatrix[44] = workingMatrix[44]
    tempMatrix[45] = workingMatrix[45]
    tempMatrix[46] = workingMatrix[46]
    tempMatrix[47] = workingMatrix[47]

    return tempMatrix


def Ri(workingMatrix):
    R(workingMatrix)
    R(workingMatrix)
    R(workingMatrix)

    return tempMatrix


def Ui(workingMatrix):
    U(workingMatrix)
    U(workingMatrix)
    U(workingMatrix)

    return tempMatrix


def Fi(workingMatrix):
    F(workingMatrix)
    F(workingMatrix)
    F(workingMatrix)

    return tempMatrix


def Li(workingMatrix):
    L(workingMatrix)
    L(workingMatrix)
    L(workingMatrix)

    return tempMatrix


def Bi(workingMatrix):
    B(workingMatrix)
    B(workingMatrix)
    B(workingMatrix)

    return tempMatrix


def Di(workingMatrix):
    D(workingMatrix)
    D(workingMatrix)
    D(workingMatrix)

    return tempMatrix


def initialize():
    startMatrix[0] = 0
    startMatrix[1] = 0
    startMatrix[2] = 0
    startMatrix[3] = 0
    startMatrix[4] = 0
    startMatrix[5] = 0
    startMatrix[6] = 0
    startMatrix[7] = 0
    startMatrix[8] = 1
    startMatrix[9] = 1
    startMatrix[10] = 1
    startMatrix[11] = 1
    startMatrix[12] = 1
    startMatrix[13] = 1
    startMatrix[14] = 1
    startMatrix[15] = 1
    startMatrix[16] = 2
    startMatrix[17] = 2
    startMatrix[18] = 2
    startMatrix[19] = 2
    startMatrix[20] = 2
    startMatrix[21] = 2
    startMatrix[22] = 2
    startMatrix[23] = 2
    startMatrix[24] = 3
    startMatrix[25] = 3
    startMatrix[26] = 3
    startMatrix[27] = 3
    startMatrix[28] = 3
    startMatrix[29] = 3
    startMatrix[30] = 3
    startMatrix[31] = 3
    startMatrix[32] = 4
    startMatrix[33] = 4
    startMatrix[34] = 4
    startMatrix[35] = 4
    startMatrix[36] = 4
    startMatrix[37] = 4
    startMatrix[38] = 4
    startMatrix[39] = 4
    startMatrix[40] = 5
    startMatrix[41] = 5
    startMatrix[42] = 5
    startMatrix[43] = 5
    startMatrix[44] = 5
    startMatrix[45] = 5
    startMatrix[46] = 5
    startMatrix[47] = 5

    workingMatrix = startMatrix[:]
    return workingMatrix


def check(workingMatrix, checkMatrix):
    checker = True
    for x1 in range(0, 48):
        if((checkMatrix[x1] != -1) and (workingMatrix[x1] != checkMatrix[x1])):
            checker = False
    return checker


def iterate(workingMatrix, checkMatrix, steps, moves, alg):
    checker_flg = None
    if (steps >= 1):
        for move1 in moves:
            tempMatrix = move1(workingMatrix)
            checker_flg = check(tempMatrix, checkMatrix)
            if checker_flg:
                alg.append(str(move1))
                break
            iterate(workingMatrix, checkMatrix, steps-1, moves, alg)
    else:
        for move1 in moves:
            tempMatrix = move1(workingMatrix)
            #print("cube representation " + str(move1))
            #print(tempMatrix)
            #workingMatrix = tempMatrix[:]
            checker_flg = check(workingMatrix, checkMatrix)
            if checker_flg:
                alg.append(str(move1))
                break
    return alg


algorithm = []
alg = []
moves = [R, U, L, B, F, D, Ri, Ui, Li, Bi, Fi, Di]
workingMatrix = initialize()
checkMatrix[0] = 1
checkMatrix[1] = -1
checkMatrix[2] = -1
checkMatrix[3] = -1
checkMatrix[4] = -1
checkMatrix[5] = -1
checkMatrix[6] = -1
checkMatrix[7] = -1
checkMatrix[8] = -1
checkMatrix[9] = -1
checkMatrix[10] = -1
checkMatrix[11] = -1
checkMatrix[12] = -1
checkMatrix[13] = -1
checkMatrix[14] = -1
checkMatrix[15] = -1
checkMatrix[16] = -1
checkMatrix[17] = -1
checkMatrix[18] = -1
checkMatrix[19] = -1
checkMatrix[20] = -1
checkMatrix[21] = -1
checkMatrix[22] = -1
checkMatrix[23] = -1
checkMatrix[24] = -1
checkMatrix[25] = -1
checkMatrix[26] = -1
checkMatrix[27] = -1
checkMatrix[28] = -1
checkMatrix[29] = -1
checkMatrix[30] = -1
checkMatrix[31] = -1
checkMatrix[32] = -1
checkMatrix[33] = -1
checkMatrix[34] = -1
checkMatrix[35] = -1
checkMatrix[36] = -1
checkMatrix[37] = -1
checkMatrix[38] = -1
checkMatrix[39] = -1
checkMatrix[40] = -1
checkMatrix[41] = -1
checkMatrix[42] = -1
checkMatrix[43] = -1
checkMatrix[44] = -1
checkMatrix[45] = -1
checkMatrix[46] = -1
checkMatrix[47] = -1

for step in range(1, 3):
    algorithm = iterate(workingMatrix, checkMatrix, step, moves, alg)

print(algorithm)
