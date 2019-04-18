A = [5,2,4,6,1,3]

def Partition(A,p,r):
	x = A[r]
	i = p - 1
	for j in range(p,r):
		if(A[j]<=x):
			i = i + 1
			temp1 = A[i]
			A[i] = A[j]
			A[j] = temp1
	
	temp2 = A[i+1]
	A[i+1] = A[r]
	A[r] = temp2
	return i+1


def QuickSort(A,p,r):
	if(p<r):
		q = Partition(A,p,r)
		QuickSort(A,p,q-1)
		QuickSort(A,q+1,r)

if __name__ == '__main__':
	QuickSort(A,0,len(A)-1)
	print(A)

