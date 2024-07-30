def my_zip(*iterables, strict=False):
    iterators = [iter(i) for i in iterables]
    while True:
        try:
            current_tuple = (next(it) for it in iterators)
            yield current_tuple
        except StopIteration:
            break

ls1 = [1,2,3,4]
ls2 = ("a",'b','c','d')
# print(list(my_zip(ls1,ls2)))

def my_enum(iterable, start=0):
    for item in iterable:
        yield start, item
        start +=1
# print(list(my_enum(ls2)))

def my_map(func:'any function you apply',*iterables:'the items you want to apply the function'):
    iterators = [iter(i) for i in iterables]
    while True:
        try:
            result = [next(it) for it in iterators]
            yield func(result)
        except StopIteration:
            return

# print(list(my_map(lambda x: x*2,ls1)))
# print(my_map.__annotations__)

def my_filter(func,*iterables):
    if func is None:
        filtered = [ i for i in iterables if bool(i)]
    else:
        filtered = [i for i in iterables if func(i)]
    for item in filtered:
        return item

num = [1,2,3,4,5,6]
#res = my_filter(lambda x: x%2 == 0,num), """shows errors please check"""
# print(list(res))

# numbers = iter(num)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))


list1 = [4,9,57,13,27]
def get_nth_elem(it,number_of_it):
    iterator = iter(it)
    itr = 0
    for i in iterator:
        if number_of_it == itr:
            return i
        else:
            itr += 1

# x=get_nth_elem(list1,3)
# print(x)

def apply_function(func,it):
    ls = []
    for i in it:
        res = func(i)
        ls.append(res)
    return ls

nums = [1,2,3]
x = apply_function(lambda x: x*2,nums)
print(x)