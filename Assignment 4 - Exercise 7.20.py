# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 20:19:58 2022

@author: Richard Michael
"""

# import random and numpy
import random
import numpy as np

# time the generation of a 1 element list
%timeit rolls_list = [random.randrange(1,7) for i in range(0,1)]

# time the generation of a 1 element array
%timeit rolls_array = np.random.randint(1,7,1)

# time the generation of a 10 element list
%timeit rolls_list = [random.randrange(1,7) for i in range(0,10)]

# time the generation of a 10 element array
%timeit rolls_array = np.random.randint(1,7,10)

# time the generation of a 100 element list
%timeit rolls_list = [random.randrange(1,7) for i in range(0,100)]

# time the generation of a 100 element array
%timeit rolls_array = np.random.randint(1,7,100)

# time the generation of a 1000 element list
%timeit rolls_list = [random.randrange(1,7) for i in range(0,1000)]

# time the generation of a 1000 element array
%timeit rolls_array = np.random.randint(1,7,1000)

# time the generation of a 10000 element list
%timeit rolls_list = [random.randrange(1,7) for i in range(0,10000)]

# time the generation of a 10000 element array
%timeit rolls_array = np.random.randint(1,7,10000)

# time the generation of a 100000 element list
%timeit rolls_list = [random.randrange(1,7) for i in range(0,100000)]

# time the generation of a 100000 element array
%timeit rolls_array = np.random.randint(1,7,100000)

# time the generation of a 1000000 element list
%timeit rolls_list = [random.randrange(1,7) for i in range(0,1000000)]

# time the generation of a 1000000 element array
%timeit rolls_array = np.random.randint(1,7,1000000)