import random as rnd
import SaMatrix
import math as mth
import numpy as nmp

class SA:
    def __init__(self, SaMatrix):
        self.Matrix = SaMatrix

        self.T = 100
        self.T0 = self.T
        self.alpha = 0.99
        self.C = 0.995   #эксперимент, дополнительное изменение температуры

    def Run(self):
        # print("pos before change:", self.Matrix.Pos) #позиция до изменения
        Pos = self.Matrix.ChangePos()
        # print("generated pos", Pos)  #сгенерированная позиция, пойдет дальше не проверку

        NewMatrix = SaMatrix.Matrix(self.Matrix.Q)
        NewMatrix.SetPos(Pos)
        ds = self.Matrix.FitnessPos(NewMatrix) - self.Matrix.FitnessPosSelf() #выводит разницу функций приспособленности
        ds = NewMatrix.FitnessPosSelf() - self.Matrix.FitnessPosSelf()
        # print("ds:{0} and p:{1}".format(ds, nmp.exp(-ds/self.T))) #полученная вероятность
        if ds <= 0:
            self.Matrix.SetPos(Pos)
        else:
            # print("Temp for prop", self.T)  # текущая температура
            p = nmp.exp(-ds/self.T)
            rnd_num = rnd.random()
            # print("Random:", rnd_num)   #сгенерированное случайное число
            if p > rnd_num:

                # print("Changed!")   # позиция сменилась
                self.Matrix.SetPos(Pos)
                self.T = self.T * self.C

        self.T = self.alpha * self.T

        return self.Matrix.FitnessPosSelf()