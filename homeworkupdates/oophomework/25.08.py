def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fib(8)))

def primes(n):
    i = 2
    while i < n :
        prime = True
        for a in range(2, i):
            if i % a == 0:
                prime = False
                break
        if prime:
            yield i
        i += 1
res = [x for x in primes(100)]
# print(res)

def infinite_sequence(): #please run
    num = 1
    while True:
        yield num
        num += 1

# print(next(infinite_sequence()))
# print(next(infinite_sequence()))
# print(next(infinite_sequence()))
# print(next(infinite_sequence()))


squares_of_nums = [x**2 for x in range(1,21)]
# for i in squares_of_nums:
    # print(i)
# print(squares_of_nums)

def repeat_element(elem,times):
    n = 0
    while n < times:
        yield elem
        n+=1


print(list(repeat_element(114,5)))

def my_range(start,end,step=0):
    start
    end
    while start <= end:
        yield start
        if step:
            start += step
        start += 1


# print(list(my_range(1,10)))
# for i in my_range(1,15,1):
    # print(i)

evens = (i for i in range(1,51) if i%2 ==0)
# print(list(evens))

def expr_prop(it):
    for i in it:
        yield i
    if i =='error':
        raise ValueError

ls = ['hi','hello','bye']
# print(list(expr_prop(ls)))

def my_zip(*iterables, strict=False):
  iterators = [iter(it) for it in iterables]
  res = []
  while True:
    try:
      res.append(tuple([next(it) for it in iterators]))
    except StopIteration:
      break
  return res

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = my_zip(a, b)
print(x)

def my_map( func, *iterables):
    iterators = [iter(iterator) for iterator in iterables]
    while True:
        try:
            current_tuple = [next(iterator) for iterator in iterators]
            yield func(current_tuple)
        except StopIteration:
            return


numbers = [4,5,6]
# result = my_map(lambda x: x**2, numbers)
# print(list(result))

def my_filter(func,iterable):
    if func is None:
        filtered_items = [i for i in iterable if bool(i)]
    else:
        filtered_items = [i for i in iterable if func(i)]
    for item in filtered_items:
        return item

ages = [5, 12, 17, 18, 24, 32]
adults = filter(lambda x: x >12 ,ages)
print(list(adults))