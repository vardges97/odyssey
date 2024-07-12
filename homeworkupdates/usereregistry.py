import random
users = []

import random
users = []

reserve = ["admin",'root',"boss"]


def createuser():
    use_id = random.randint(1, 5435234)
    name = input('enter your name: ')
    if len(name)>20 or len(name)<5:
        print("username must contain from 5 to 20 characters")
    if not name.isalnum():
        print('name must contain only letters and numbers no special characters')
    for i in reserve:
        if i in reserve == name:
            print('name must not be a reserved name')
    surname = input('enter your surname: ')
    email = input('enter your email: ')
    if "@" and "." not in email:
        print('invalid email')
    password = input('enter your password: ')
    if len(password) < 8:
        print("password must be at least 8 characters long")
    if password.isalnum():
        print('password must contain at least 1 special character')
    phone = input('enter your phone number: ')
    if len(phone)<9 or len(phone)>11:
        print("invalid phone")
    if not phone.isdigit():
        print("invalid phone number")
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