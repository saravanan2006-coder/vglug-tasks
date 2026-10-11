#addition of two matrices

a = [[4,7],[9,5]]
b = [[8,1],[12,6]]
c = [[0,0],[0,0]]
for i in range(2):
	for j in range(2):
		c[i][j]=a[i][j]+b[i][j]
for result_matrix in c:
	print(result_matrix)
