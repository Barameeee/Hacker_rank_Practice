

'''
    n = int(input())
    arr = map(int, input().split())
'''

n = 5
arr = map(int, ('6 6 4 3 1').split())

a = list(arr)
listp = []
for i in a:
    if i not in listp:
        listp.append(i)
listp.sort(reverse = True)
print(listp)