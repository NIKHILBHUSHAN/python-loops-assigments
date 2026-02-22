'''import numpy as np
import time

array=np.arange(1,50001)

List1=list(range(1,50001))

start=time.time()
array_sum=np.sum(array)
numpy_time=time.time()-start

start=time.time()
listsum=sum(List1)
python_time=time.time()-start

print(f"Numpy time:{numpy_time:.4f}seconds")
print(f"Python time:{python_time:.4f}seconds")

speed_up=python_time/numpy_time

print(f"NumPy is {speed_up:.1f}x faster")'''

import numpy as np
import time

# Create 1 million numbers
size = 1_000_000

# Python List approach
python_list = list(range(size))
start = time.time()
result = [x * 2 for x in python_list]
python_time = time.time() - start
print(f"Python list: {python_time:.4f} seconds")

# NumPy approach
numpy_array = np.arange(size)
start = time.time()
result = numpy_array * 2
numpy_time = time.time() - start
print(f"NumPy array: {numpy_time:.4f} seconds")

# Compare
speedup = python_time / numpy_time
print(f"NumPy is {speedup:.1f}x faster!")



