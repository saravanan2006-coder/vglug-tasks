
a  = [[38,12],[96,30]]
b = [[53,8],[37,81]]
c = [[0,0],[0,0]]

for i in range(2):
	for j in range(2):
		for k in range(2):
			c[i][j] = c[i][j] + a[i][k] * b[k][j]
for result_matrix in c:
	print(result_matrix)
