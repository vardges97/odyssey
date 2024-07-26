def greeter(name,surname,message='salutations'):
    print(name,surname,message)

# x = greeter('john','johnson')

def itemprice(eggs,ham,cheese,tax='no aditional tax because its not america and sales taxes are '
                                  'included in the price',muller=0.05):
    final_price=ham+eggs+cheese+((eggs+ham+cheese)*muller)
    print(f"total is: {final_price},tax is: {tax}")

# print(itemprice(5,15,12))


def userprinter(name,surname,age=int,city=str):
    return name,surname,age,city

# print(userprinter('john','doe',age=25,city='new york'))

def dataprocessing(a,b,c,operation='sum'):

    if operation=="mul":
        return a*b*c
    if operation == "sub":
        return a-b-c
    if operation == 'div':
        a/b/c
    else:
        return a + b + c
# print(dataprocessing(5,6,7))


def personprinter(name,surname,age):
    print(f"{name},{surname} is {age} years old ")

person={"name":"john","surname":"doe","age":46}
# personprinter(**person)

def reportgen(name,age,location='default'):
    print(name,age,location)

# print(reportgen("bob",15))

def logger(*args,**kwargs):
    return args,kwargs
print(logger('bob','dillan',timestamp=1941,age=83))

