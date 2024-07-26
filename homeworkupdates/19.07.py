ls =[1,[2,[3,4],5],6,[7,8]]
result = []

def unpacker(ls):
    for i in ls:
        if type(i) == list :
            unpacker(i)
        else:
            result.append(i)
    return result

print(unpacker(ls))

ls2 = [1,2,3,4]

def sum_of_list(ls):
    if len(ls) == 0:
        return 0
    else:
        return ls[0] + sum_of_list(ls[1:])

# print(sum_of_list(ls2))


def sorted_list(ls):
    if len(ls) < 1:
        return True
    return ls[0] <= ls[1] and sorted_list(ls[1:])

def prime_checker(num):
    for i in range(2,(num//2)):
        if num % i ==0:
            return False
        else:
            return True

# print(prime_checker())


def max_returner(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(max_returner(1,5,3))

def fibonacci(n):
    if n <=1 :
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
def print_fib(n):
    for i in range(n):
        print(fibonacci(i))

# print(print_fib(8))

def sqr_of_two(n):
    if n & (n-1) ==0:
        return True
    else:
        return False
print(sqr_of_two(6))