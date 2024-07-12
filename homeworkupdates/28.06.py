def myinsert(ls,insert):
    res = ls
    for x,y in insert:
        res = res[:x] + list(y) +res[x:]
    return res

ls = [1,2,3,4,6]
insert1=[(4,'5')]
final = myinsert(ls,insert1)
print(final)

def myremove(ls,i):
    for x in range(len(ls)):
        if x == i:
            del ls[x]
    return ls

# ls =[1,2,34,5,2]
# final = myremove(ls,2)
# print(final)


ls =[1,2,34,5,2]
def mypop(ls):
    return ls[:-1]

z = mypop(ls)

print(z)

def myclear(ls):
    x = len(ls)-1
    for i in range(len(ls)):
        del ls[x]
        x-=1
    return ls

# v = myclear(ls)
# print(v)

# x = [i**2 for i in range(1,11)]
# print(x)
#
# ls = [1,2,3,4,5,6,7,8,9,10]
# y= [i for i in ls if i%2==0]
# print(y)