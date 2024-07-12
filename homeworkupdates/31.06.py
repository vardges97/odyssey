def set_checker(set1,set2):
    if set1 == set2:
        print('sets are the same')
    else:
        print("sets are not the same")

set1 = [1,2,3,4,5]
set2 = [1,2,3,5,4]

# print(set_checker(set1,set2))

def set_indexes():
    sett = []
    while len(sett) < 5:
        item = int(input('enter the set items: '))
        sett.append(item)
    x = max(sett)
    y = min(sett)
    indexmax = sett.index(x)
    indexmin = sett.index(y)
    res = indexmax-indexmin
    print(x,y,res)

# print(set_indexes())

mat = [[i +(j*3) for i in range(1,5)]for j in range(0,4)]


def matprimary(mat):
    sum = 0
    for i in range(len(mat)):
        sum += mat[i][i]
    return sum

def matsecondary(mat):
    sum = 0
    for i in range(len(mat)):
        sum += mat[i][len(mat)-i-1]
    return sum

# print(mat)
# print(matprimary(mat))
# print(matsecondary(mat))

def max_for_nonsquare(row,col,mat):
    m = row
    n = col
    MxN = [m,n]
    max = 0
    for i in range(MxN[0]):
        for j in range(MxN[1]):
            if mat[i][j]> max:
                max = mat[i][j]
    return max

arr = [[0, 3, 2, 4],
       [2, 3, 6, 5],
       [7, 1, 2, 3]]

print(max_for_nonsquare(row=3,col=4,mat=arr))