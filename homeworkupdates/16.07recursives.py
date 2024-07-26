def print_one_to_n(n):
    if n > 0:
        print_one_to_n(n-1)
        print(n)

# print(print_one_to_n(5))

def print_n_to_one(n):
    if n > 0:
        print(n)
        print_n_to_one(n-1)

# print(print_n_to_one(5))

def factoral(n):
    if n ==1:
        return n
    else:
        return n * factoral(n-1)

# print(factoral(5))

def sum_of_nums(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_nums(n-1)

# print(sum_of_nums(5))

def print_list(ls):
    if len(ls)==0:
        return ""
    else:
        print(ls[0])
        return print_list(ls[1:])

# print(print_list([1,2,3,4]))

def recursive_list_len(ls):
    if ls:
        return 1+recursive_list_len(ls[1:])
    return 0

ls = [1,2,3,4,5,7]

# print(recursive_list_len(ls))

def recursive_word_reverser(str):
    if len(str) == 0:
        return str
    else:
        return recursive_word_reverser(str[1:])+str[0]

# print(recursive_word_reverser("hello"))

def fibonacci(n):
    if n ==2 or n==3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))

def recursive_word_printer(str):
    if len(str) == 0:
        print('*')
    else:
        print(str[len(str)-1])
        recursive_word_printer(str[0:len(str)-1])

# print(recursive_word_printer("hello"))

def recursive_palindrome(str):
    if len(str)<=1:
        return True
    if str[0]==str[len(str)-1]:
        return recursive_palindrome(str[1:len(str)-1])

print(recursive_palindrome("anana"))

def recursive_numsum(num):
    if num ==0:
        return 0
    return (num % 10 + recursive_numsum(int(num/10)))

print(recursive_numsum(1234))