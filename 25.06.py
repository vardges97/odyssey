word ='gazebo'
def zfinder(str):
    for i in range(len(str)):
        if str[i] == 'z':
            return i
        else:
            print('z not found')
# print(zfinder(word))

def changetoupper(text):
    new_text = ""
    for i in text:
        # i = ord(i) - 32
        new_text += chr(ord(i)-32)
    return new_text

print(changetoupper(word))

sentance='hello there, general kenobi !'

def changefirsttoupper(text):
    x = text.split()
    new_text = []
    for i in x:
        if len(i) > 1:
            upper_char = chr(ord(i[0]) - 32)
            res = upper_char + i[1:]
            new_text.append(res)
    y = " ".join(new_text)
    return y
x = changefirsttoupper(sentance)
print(x)

def reverser(str):
    return str[::-1]

word='hello'
# print(reverser(word))

def palindrometester(str):
    pal = str[::-1]
    if str == pal:
        return "yes"
    else:
        return "no"
wrd = 'radar'
# print(palindrometester(wrd))

def concater(str1,str2):
    return str1 + " " + str2

wrd1 = 'hello'
wrd2 = 'there'

# print(concater(wrd1,wrd2))

def replacer(str):
    changed = ''
    for i in str:
        if i == 'a':
            i = 'x'
        changed += i
    return changed
# print(replacer('banana'))
