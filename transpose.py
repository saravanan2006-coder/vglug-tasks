#Transpose

a = [[7,2,9],[4,5,8]]
b = [[0,0],[0,0],[0,0]]
for i in range(2):
	for j in range(3):
		b[j][i] = a[i][j]
for t in b:
	print(t)
