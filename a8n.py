import copy

def pprint(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            A[i][j] = float(A[i][j])
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")


def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        forcheck = copy.deepcopy(A)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp
        if forcheck!=A:
            #print("row interchange")
            pprint(A)

        # Make all rows below this one 0 in current column
        forcheck = copy.deepcopy(A)
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
        if forcheck != A: pprint(A)
        

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        if float(A[i][i]) == 0.0:
            print("no unique solution")
            break
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


if __name__ == "__main__":
    #p372 6a
    #A = [[0.0,1.0,-2.0,4],[1.0,-1.0,1.0,6.0],[1.0,0.0,-1.0,2.0]]
    
    #p372 6b
    #A = [[1,-.5,1.0,0,3],[2.0,-1.0,-1.0,1,5.0],[1.0,1.0,0.5,0,2.0],[1,-.5,1,1,5]]

    #p373 8d
    #A = [[1,1,-1,1,-1,2],[2,2,1,-1,1,4],[3,1,-3,-2,3,8],[4,1,-1,4,-5,16],[16,-1,1,-1,-1,32]]

    A = [[1,2,3,4],[2,1,-1,1],[-3,2,0,1],[0,5,2,6]]
    # Print input
    pprint(A)

    # Calculate solution
    x = gauss(A)

    # Print result
    line = "Result:\t"
    for i in range(0, len(A)):
        line += str(x[i]) + "\t"
    print(line)
