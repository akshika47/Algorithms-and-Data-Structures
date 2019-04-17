Pseudocode for Exercise 2.1-4

```
A = B = [n]
C = [n+1]{0}

for i = 0 to A.length
  v = A[i] + B[i] + C[1]
  if(v>1)
    C[i+1] = 1
  
  C[i] = v%2
  
```
