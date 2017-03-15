from functools import reduce
from operator import mul

print(reduce(lambda x, y, z: x*y*z, [3,4,5]))