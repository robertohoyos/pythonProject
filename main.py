# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# estos ejercicios son para la plataforma de soluciones

import statistics
from typing import Optional #para los métodos con parámetros opcionales


class ListNode:
    def __init__(self, val=0, next=None): # por default se crea con uno
        self.val = val
        self.next = next



class SingleLinkedList:
    def __init__(self):
        self.head = none
        self.tail = none
        return



    def add_list_item(self, item):
        "add an item at the end of the list"

        if not isinstance(item, ListNode): #checa si el list item es de la clase ListNode
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return

    def list_length(self):
        "returns the number of list items"

        count = 0
        current_node = self.head

        while current_node is not None:
            # increase counter by one
            count = count + 1

            # jump to the linked node
            current_node = current_node.next

        return count

    def output_list(self):
        "outputs the list (the value of the node, actually)"

        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            # jump to the linked node
            current_node = current_node.next

        return


def generaLista (lista: ListNode) -> SingleLinkedList:

    while Nodo == True:
        print (hola)

    return





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

    # funciona perfecto con enteros, pero cuando hay negativos hay problema
    # para no alterarlo mucho cuando haya un menos sólo poner el signo al final con un if
    def reverse(self, x: int) -> int:
        banderaNegativo = 0
        # checar primero si tiene signo al principio
            # si el número es menor que 0 volverlo absoluto y ponerle un signo al final
        if (x < 0):
            x = abs(x)
            banderaNegativo = True
        # recibe el número y colocalos en una lista
        # voltea la lista
        # convertirla en un int
        listaString = [int(a) for a in str(x)] #convierte a lista de ints
        nuevoNum = [str(integer) for integer in listaString] # reconvierte
        nuevoNum.reverse()
        datoEnString = "".join(nuevoNum) #paraVolverloString

        if banderaNegativo == True:
            datoEnString = "-"+datoEnString

        # para checar que no está fuera de parámetros
        # ponerle la restricción de si es mayor de 32 bit
        if int(datoEnString) > 2 ** 31 or (int(datoEnString)) < -(2 ** 31):
            datoEnString = 0

        return int(datoEnString)



    # Given two strings ransomNote and magazine, return true if ransomNote can be constructed
    # by using the letters from magazine and false otherwise.
    # Each letter in magazine can only be used once in ransomNote.
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # sería fácil si se pueden quitar caracteres de la reviste en una lista para construir el ransonNote
        # iría recorriendo uno a uno el string.
        Resultado = False

        # for x in string note
        for letra in ransomNote:
            if magazine.find(letra) != -1:   # si lo encuentra regresa -1
                Resultado = True
                magazine = magazine.replace(letra,'', 1) # no debe reemplazar todas
            else:
                Resultado = False
                break
        # checa que exista en el magazine
        # si existe, pasa al siguiente y quita una letra
        # marca true, si no, en la primera vez que falle marca false
        return Resultado




    # te da 2 números al revés, sumarlos y regresar el número al revés, en una lista linkeada
    # el reto es que los linked Lists son mucho más primitivos y hay que implementar la funcionalidad
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        print(l1.val)

        Resultado = 0
        # revertir los números y genera un int; puede ser más fácil convertirlos a string y luego a número

        # en el caso del linked list tendríamos que ir nodo por nodo, con un while mientras no sea none
        # y vas generando otra linked list, de tal suerte que los primeros que saques con los últimos en la nueva lista
        # acaso tengo que recorrer la lista para crearla? porque sólo lee el primer valor?
        # lista1 = SingleLinkedList(l1)
        # print (lista1)

        # Nodo = l1.val
        # NuevaLista = []
        # while Nodo is not None:
        #     NuevaLista.append(Nodo.val)
        #     Nodo = l1.next
        # print(NuevaLista)

        # l1.reverse()
        # l2.reverse()

        # usar la función de map una vez que la entienda
        temp1 = ''
        for x in l1:
            temp1 = temp1 + '' + str(x)
        # print (temp1)

        temp2 = ''
        for x in l2:
            temp2 = temp2 + '' + str(x)
        # print(temp2)

        r1 = int(temp1)
        r2 = int(temp2)
        # realizar la suma

        Resultado = r1 + r2
        nuevoResultado = str(Resultado)

        listaRestulado = list(nuevoResultado)
        listaRestulado.reverse()

        # revertir el resultado
        return listaRestulado

    def addTwoNumbersFacil(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Resultado = 0
        # revertir los números y genera un int; puede ser más fácil convertirlos a string y luego a número
        l1.reverse()
        l2.reverse()

        # usar la función de map una vez que la entienda
        temp1 = ''
        for x in l1:
            temp1 = temp1 + '' + str(x)
        # print (temp1)

        temp2 = ''
        for x in l2:
            temp2 = temp2 + '' + str(x)
        # print(temp2)

        r1 = int(temp1)
        r2 = int(temp2)
        # realizar la suma

        Resultado = r1 + r2
        nuevoResultado = str(Resultado)

        listaRestulado = list(nuevoResultado)
        listaRestulado.reverse()

        # revertir el resultado
        return listaRestulado

    # me dan un número romano y tengo que dar un entero
    # para resolverlo tengo que partir el string en componentes
    # asumo que casi todos los caracteres serán el número a sumar (un for), salvo excepciones
    # cuando me llegue un número checar que el que le siga sea menor, si no aplicar las condiciones
    def romanToInt(self, s: str) -> int:
        numerofinal = 0; numeroTemp = 0; numeroAnterior = 0; numero_resta = 0

        for element in s:
            print (numerofinal)
            match element:
                case 'I':
                    numeroTemp = 1
                case 'V':
                    numeroTemp = 5
                case 'X':
                    numeroTemp = 10
                case 'L':
                    numeroTemp = 50
                case 'C':
                    numeroTemp = 100
                case 'D':
                    numeroTemp = 500
                case 'M':
                    numeroTemp = 1000

                # si el número anterior es mayor entonces no hay excepción
            if numeroAnterior < numeroTemp:
                numero_resta = numeroAnterior * -2
                numeroAnterior = numeroTemp
                print(numeroAnterior)
                print(numeroTemp)
                print (numero_resta)

            else:
                numeroAnterior = numeroTemp

            numerofinal = numerofinal + numeroTemp + numero_resta; numero_resta = 0

        return numerofinal

    class RomanToDecimal:
        def __init__(self):
            self.roman_dict = {
                'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }

        def roman_to_decimal(self, roman_numeral):
            decimal_num = 0
            prev_value = 0
            for i in range(len(roman_numeral) - 1, -1, -1):
                current_value = self.roman_dict[roman_numeral[i]]
                if current_value < prev_value:
                    decimal_num -= current_value
                else:
                    decimal_num += current_value
                prev_value = current_value
            return decimal_num


    def lengthOfLongestSubstring(s):
        # Initialize a dictionary to store the last seen position of each character
        char_dict = {}
        # Initialize the starting index of the window
        start = 0
        # Initialize the length of the longest substring
        max_len = 0
        # Iterate over each character in the string
        for i in range(len(s)):
            # If the character is already in the dictionary and its last seen position is after the start of the current window
            if s[i] in char_dict and char_dict[s[i]] >= start:
                # Move the start of the window to the position after the last seen position of the repeated character
                start = char_dict[s[i]] + 1
            # Update the last seen position of the character in the dictionary
            char_dict[s[i]] = i
            # Update the length of the longest substring if the current window is longer
            max_len = max(max_len, i - start + 1)
        # Return the length of the longest substring
        return max_len

# s1 = Solution.addTwoNumbers(Solution, [2,4,3], [5,6,4])
s1 = Solution.lengthOfLongestSubstring('Analiza esto, mal nacido.')
# rtd = RomanToDecimal(); s1 = rtd.roman_to_decimal('MCMXCIV')
# dentro de la clase solución está integrada también la clase de RomanDecimal
print(s1)
