def n_to_zero(n):
    while n > 0:
        print(n)
        n=n-1

# print(n_to_zero(7))

def zero_to_n(n):
    m = 0
    while n+1 > m:
        print(m)
        m+=1

# print(zero_to_n(5))

def printlist(ls):
    for i in ls:
        print(i)

ls1 = [1,2,3,4,5,15,7,6]

# print(printlist(ls1))

def sum_of_num(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

# print(sum_of_num(123))

def first_capital(str):
    for i in range(0,len(str)):
        if(str[i].isupper()):
            return str[i]

print(first_capital('hello There'))


def get_max(ls):
    max = 0
    for i in ls:
        if i > max:
            max = i
    return max

print(get_max(ls1))
