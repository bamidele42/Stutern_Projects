import numpy as np
list1 = np.arange(5.5, 20.5)
list2 = [int(x) for x in list1 ]

even_number = len(list(filter(lambda x: x%2 == 0, list2)))
odd_number = len(list(filter(lambda x: x%2 != 0, list2)))
print(even_number)
print(odd_number)

square = list(map(lambda x: x**2, list2))
cube = list(map(lambda x: x**3, list1))
print(square)
print(cube)

