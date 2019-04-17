from array import array
import time

ticks1 = time.time()
A = [5,2,4,6,1,3]

for j in range(1, len(A)):
	key = A[j]
	i = j-1
	while (i>-1 and A[i] < key):
		A[i+1] = A[i]
		i = i-1
	A[i+1] = key
ticks2 = time.time();
print(A)
print("Time spent", ticks2-ticks1)