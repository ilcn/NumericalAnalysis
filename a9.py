from fractions import Fraction

#	Show Matrix
def show(header, mtrx):
	print header, "-------"
	for i in range(0, len(mtrx)):
		for j in range(0, len(mtrx)):
			if mtrx[i][j] == int(mtrx[i][j]):
				print "{0:8d}".format(int(mtrx[i][j])),
			else:
				tmp = Fraction.from_float(mtrx[i][j]).limit_denominator()
				print " "*(7-len(str(tmp))),
				print tmp,
		print ""
	print ""

#	LU decomposition by Crout algorithm [usage: L, U = ludec(A)]
def ludec(A):
	L = [[0.0 for i in range(len(A))] for j in range(len(A))]
	U = [[0.0 for i in range(len(A))] for j in range(len(A))]
	try:
		for i in range(0, len(A)):
			L[i][0] = A[i][0]			#	L:deside 1 column.
			U[0][i] = A[0][i]/A[0][0]	#	U:deside 1 row.
		for k in range(1, len(A)):
			for i in range(0, k):
				L[i][k] = U[k][i] = 0.0	#	initialize the element to be updated.
			for i in range(k, len(A)):
				L[i][k] = A[i][k]
				for m in range(0, k):
					L[i][k] -= L[i][m] * U[m][k]
			U[k][k] = 1.0				#	U:diagonal element is 1
			for i in range(k + 1, len(A)):
				U[k][i] = A[k][i]
				for m in range(0, k):
					U[k][i] -= L[k][m] * U[m][i]
				U[k][i] /= L[k][k]
	except ZeroDivisionError:
		print "This matrix can't do LU Decomposition."
	return L, U

def floatmat(A):
	for i in range(len(A)):
		for j in range(len(A[i])):
			A[i][j] = float(A[i][j])
	return A

A = [
	[2, -1, 0, 0,0],
	[1, 2, -1,0,0],
	[0,2,4,-1,0],
	[0,0,0,2,-1],
	[0,0,0,1,2]
]

show("Original Matrix", floatmat(A))
L, U = ludec(floatmat(A))
show("L", L)
show("U", U)

