def bubble(ls):
    n = len(ls)
    for i in range(n-1):
        for j in range(n-i-1):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]

def selection_sort(ls):
    n = len(ls)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if ls[j]<ls[min_index]:
                min_index = i
        ls[i],ls[min_index]=ls[min_index],ls[i]