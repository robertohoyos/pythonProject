
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Solution:
    def fizzBuzz(self, n: int):
        array = [str] * n

        for x in range(len(array)):

            if ((x + 1) % 5 == 0) and ((x + 1) % 3 == 0):
                array[x] = "FizzBuzz"
            elif (x+1) % 3 == 0:
                array[x] = "Fizz"
            elif (x+1) % 5 == 0:
                array[x] = "Buzz"
            else:
                array[x] = str(x+1)

        return array

s1 = Solution.fizzBuzz(Solution, 15)
print(s1)
