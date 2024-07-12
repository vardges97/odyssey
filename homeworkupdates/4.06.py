# students = {"bob":85,'rob':65,'lob':75}
#
# students['mac'] = 68
# print(students)
# students['rob'] = 75
# print(students)
# del students['rob']
# print(students)
#
#
# set1 = {"apple", "banana", "cherry"}
# set2 = {"pear", "coconut", "strawberry"}
# set3 = set1 | set2

# print(set3)

# def asterikses(n):
#     for n in range (1,5):
#         print(n*'*')

list = [1,2,3,4,5]
for i in list:
    if (i == 3 and i % 2 !=0) or (i != 3 and i % 2 !=0 ):
        continue
    print(i)