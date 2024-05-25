#Fibbonacci Series

from functools import reduce #import module

fibonacci = lambda a: reduce(lambda x, _: x + [x[-1] + x[-2]],
                       range(a - 2), [0, 1])
#print the series
print(fibonacci(10))
