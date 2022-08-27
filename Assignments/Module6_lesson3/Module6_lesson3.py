import numpy as np
from numpy import random

numbers = np.arange(1, 101)
even_numbers=list(filter(lambda x: x%2 ==0, numbers))
print(even_numbers)
lcm_of_even_numbers = np.lcm.reduce(even_numbers)
print(lcm_of_even_numbers)
