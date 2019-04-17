### Pseudocode for Insertion Sort

```
A = [5,2,4,6,1,3]
for j = 1 to A.length
  key = A[j]
  i = j-1
  while i>-1 and A[i] > key
    A[i+1] = A[i]
    i = i-1
  A[i+1] = key

Print(A)
```
