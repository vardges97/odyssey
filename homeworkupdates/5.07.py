set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union = set1 | set2
diff = set1 ^ set2
sames = set2 & set1

# print(union,diff,sames)
users = []
import random
def createuser():
    use_id = random.randint(1, 5435234)
    name = input('enter your name: ')
    surname = input('enter your surname: ')
    email = input('enter your email: ')
    password = input('enter your password: ')
    phone = int(input('enter your phone number: '))
    user_info ={
        'id' :  use_id,
        "name": name,
        "surname": surname,
        "email":email,
        "password":password,
        'phone':phone
    }
    users.append(user_info)
    print('user added')

print(createuser())
print(users)