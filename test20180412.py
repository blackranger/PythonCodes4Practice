## find a number N
## Both N + 100 and N + 168 are square number

import numpy as np
import math

def check_square(n):
  s_n = int(np.sqrt(n))
  for i in range(s_n - 1, s_n + 1):
    if n == i * i:
      return True
  return False
  
N = 10000
for j in range(1, N):
  if check_square(j + 100) and check_square(j + 168):
    print(j)
    break

