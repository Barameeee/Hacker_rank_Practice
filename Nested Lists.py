
studentlist = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    studentlist.append([name,score])
print(studentlist)

'''
Test Case
studentlist = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
'''
o = list(set([y for x,y in studentlist]))
o.sort()
name = []
for x,y in studentlist :
    if y == o[1]:
        name.append(x)
name.sort()

for i in range(len(name)):
   print(name[i])