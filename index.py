# coding=windows-1251
import SaMatrix
import SA
import matplotlib.pyplot as plt
import time

def printSolution(pos):
    # печатает решение в виде матрицы
    for i in pos:
        for j in range(pos.__len__()):
            if j + 1 in i:
                print(j + 1, end="")
            else:
                print("*", end="")
        print()

# правильное решение для плоскости с q = 2
# Matrix = SaMatrix.Matrix(2)
#
# SaRun = SA.SA(Matrix)

# printSolution(Matrix.Pos)
# MatrixWithSolution = SaMatrix.Matrix(2)
# MatrixWithSolution.SetPos([[1,2,4],[1,3,7],[2,6,7],[1,5,6],[4,5,7],[3,4,6],[2,3,5]])
# print(MatrixWithSolution.Pos)
# print(MatrixWithSolution.FitnessPosSelf())
# print(MatrixWithSolution.FirstAxiom())
# print(MatrixWithSolution.ThirdAxiom())

# правильное решение для плоскости с q=3
# MatrixWithSolution = SaMatrix.Matrix(3)
# MatrixWithSolution.SetPos([[1,2,4,10],[2,3,5,11],[3,4,6,12],[4,5,7,13],
#                            [1,5,6,8],[2,6,7,9],[3,7,8,10],[4,8,9,11],
#                            [5,9,10,12],[1,7,11,12],[2,8,12,13], [1,3,9,13],[6,10,11,13]])
# print(MatrixWithSolution.Pos)
# print(MatrixWithSolution.FitnessPosSelf())
# print(MatrixWithSolution.FirstAxiom())
# print(MatrixWithSolution.ThirdAxiom())

# неправильное решение для плоскости с  q=3
# MatrixWithSolution = SaMatrix.Matrix(3)
# MatrixWithSolution.SetPos([[10, 3, 1, 12], [2, 11, 8, 4], [3, 7, 5, 10],
#                            [5, 2, 4, 12], [7, 11, 6, 4], [13, 1, 9, 11],
#                            [8, 2, 6, 9], [2, 10, 3, 8], [1, 13, 12, 6],
#                            [4, 12, 3, 13], [10, 9, 6, 7], [5, 8, 13, 11], [5, 7, 9, 1]])
# print(MatrixWithSolution.Pos)
# print(MatrixWithSolution.FitnessPosSelf())
# print(MatrixWithSolution.FirstAxiom())
# print(MatrixWithSolution.ThirdAxiom())

#print('compare result',Matrix.CompareLines([1,2,4],[1,2,3]))


Curs = list()
Q = 3 # размерность плоскости
try_count = 0
last_iter_count = 0
while True:
    time_start = time.time()
    Matrix = SaMatrix.Matrix(Q)
    SaRun = SA.SA(Matrix)
    Curs.clear()
    try_count += 1
    iter_count = 0
    for n in range(100000):
        iter_count += 1
        if SaRun.T < 0.000001: break  #ограничение на нижнюю границу тепмпературы
        #print(n)
        cur = SaRun.Run()
        #print("current: ", Matrix.Pos)
        #print("temp: ", SaRun.T)
        Curs.append(Matrix.FitnessPosSelf())
        last_iter_count = n
        if cur == 0:
            print("N:", n)
            print("Solution: ", Matrix.Pos)
            printSolution(Matrix.Pos)

            break

    print(try_count, last_iter_count)
    #вывод номера попытки и количества итераций в ней
    #if try_count == 5: break
    #print("one million!")
    if cur == 0: break


time_exec = time.time() - time_start
print("Execution Time: ", time_exec)
plt.title("q = {0}, alpha = {1}, T = {2}, try={3}, iter={4}".format(Q, SaRun.alpha, SaRun.T0,try_count, iter_count))
plt.figure(1)
plt.plot(Curs)
plt.grid(True)
plt.xlabel("Iterations")
plt.ylabel("Fitness")
plt.show()
