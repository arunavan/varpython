import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

import numpy as np

arr = np.array([1, 2, 3, 4, 5,99,88,77,66,77,897,765,456])
print(arr[2:6])  # 2,6-1
print(arr[3:7])
print(arr[2:8:2])
print(arr[:2])
print(arr[4:])

"""
x = arr.view()
arr[0] = 42
print(arr)
print(x)
x[1]=43
print(arr)
print(x)


"""