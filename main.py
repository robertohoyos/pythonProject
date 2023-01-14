# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import statistics


class Solution:
    def fizzBuzz(self, n: int):
        array = [str] * n

        for x in range(len(array)):

            if ((x + 1) % 5 == 0) and ((x + 1) % 3 == 0):
                array[x] = "FizzBuzz"
            elif (x + 1) % 3 == 0:
                array[x] = "Fizz"
            elif (x + 1) % 5 == 0:
                array[x] = "Buzz"
            else:
                array[x] = str(x + 1)

        return array

    def numberOfSteps(self, num):
        contadorPasos = 0
        # cuando es even, divide y me quedo con la división de 2
        # (es decir divisible módulo 2)
        # si no es, restarle 1
        # cuando llegue a cero termina el programa

        # mientras que sea mayor que 0, que ejecute; en 0 termina
        while num > 0:
            # si es divisible entre 2, me quedo con el resultado
            if num % 2 == 0:
                num = num / 2
            else:  # si no le resto 1, solamente
                num = num - 1  # asumimos que no es par
            contadorPasos = contadorPasos + 1
            # voy actualizando el contador
        return contadorPasos

    # le ingresan dos listas
    def findMedianSortedArrays(self, nums1, nums2):
        # sumarlas, luego aplicarle el mecanismo
        listaNums = nums1 + nums2  # listas concatenadas
        numeroFloat = float(statistics.median(listaNums))
        return numeroFloat


numsa = [1, 3, 4]
numsb = [9]
s1 = Solution.findMedianSortedArrays(Solution, numsa, numsb)
print(s1)
