mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]


transposed = [[i[j] for i in mat]for j in range(len(mat[0]))]
print(transposed)

mat2 = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

def rotatemat180(mat,n):
    i = n -1
    while i>=0:
        j = n-1
        while j >= 0:
            print(mat[i][j],end = " ")
            j = j-1
        print()
        i = i-1
print(rotatemat180(mat2,4))