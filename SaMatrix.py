import random as rnd


class Matrix:
    def __init__(self, q):
        self.Q = q
        self.N = q * q + q + 1

        self.Pos = self.InitialPos()

    def InitialPos(self):  # установка начальной ситуации 123 234 345 ... 567 671 712...
        Pos = [[0 for x in range(self.Q + 1)] for y in range(self.N)]  # создание матрицы, заполнение нулями
        i = 0
        t = 0
        point_number = 1
        for t in range(self.N):
            for i in range(self.Q + 1):
                Pos[t][i] = point_number % (self.N + 1)
                if Pos[t][i] == 0:
                    Pos[t][i] += 1
                    point_number += 1
                point_number += 1
            point_number -= self.Q
            if (point_number % (self.N + 1) == 0):
                point_number = self.N
            elif point_number % (self.N + 1) < 0:
                point_number = self.N + point_number

        return Pos

    def ChangePos(self):
        # Pos = list(self.Pos)
        # Pos = self.Pos.copy()
        Pos = [[0 for x in range(self.Q + 1)] for y in range(self.N)]
        # создание новой позиции, копирование Pos
        for i in range(self.N):
            for j in range(self.Q + 1):
                Pos[i][j] = self.Pos[i][j]

        i = 0
        j = 0
        # print(set([1,2,2,3]) == set([1,1,2,3]))
        # while i == j or self.CompareLines(self.Pos[i], self.Pos[j]) == self.Q + 1 or set(self.Pos[i]) == set(self.Pos[j]):
        #     i = rnd.randint(0, self.N - 1)
        #     j = rnd.randint(0, self.N - 1)
        while i == j or set(self.Pos[i]) == set(self.Pos[j]):
            # не принимаются строки одинаковые по своему составу например: 1123 и 1223
            i = rnd.randint(0, self.N - 1)
            j = rnd.randint(0, self.N - 1)

        l = 0
        r = 0
        count = 0
        while (self.Pos[i][l] in self.Pos[j] or self.Pos[j][r] in self.Pos[i]) or (self.Pos[i][l] == self.Pos[j][r]):
            # тут обмен самими точками, не принимаются одинаковые точки
            # и точки, которые уже присутствуют на прямой
            r = rnd.randint(0, self.Q)
            l = rnd.randint(0, self.Q)
            count += 1
            if (count == 3): break  # 3 попытки, чтобы не было зацикливания и долгого простаивания

            # таким образом, нет решений с одинаковыми точками на прямой

        if count != 3: Pos[i][l], Pos[j][r] = Pos[j][r], Pos[i][l]

        # print("f",i+1,l+1,"s", j+1,r+1)
        # print(Pos)
        return Pos

    def FitnessPosSelf(self):
        return self.FitnessPos(self)

    def FitnessPos(self, MatrixArg):

        res = 0
        res = MatrixArg.ThirdAxiom()
        return res

    def CompareLines(self, line1, line2):
        #функция принимает массив точек, "прямые". и подсчитывает количество общих элементов
        res = 0
        for elemLine1 in line1:
            # if line2.count(elemLine1) > 0: res += 1
            if elemLine1 in line2: res += 1
        return res
        # if (res < 2): return 0
        #
        # return res

    def FirstAxiom(self):  # нет повторяющихся точек на линии
        res = 0

        for line in self.Pos:
            for j in line:
                if line.count(j) > 1:
                    res += 1
                    break
        return res
        # if res > 0: return 1
        # return 0

    def ThirdAxiom(self):
        # проверяет, что прямые пересекаются не более чем в одной точке;
        # подсчитывает количество нарушения правила

        res = 0
        for i in range(self.N):
            for j in range(self.N):
                if i != j:
                    comp_count = self.CompareLines(self.Pos[i], self.Pos[j])
                    if comp_count > 1: res += 1
                    # res += self.CompareLines(self.Pos[i], self.Pos[j])
                    # if res >= 1:
                    #     print("lines with rep: ",i+1," ", j+1, " lines",self.Pos[i],self.Pos[j])
                    #print("comp:",self.CompareLines([4,13,12,3],[4,12,3,13]))

        return res

    def SetPos(self, pos):
        self.Pos = pos
