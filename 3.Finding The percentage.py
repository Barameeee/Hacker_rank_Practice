'''
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
'''
query_name = 'Malika'
student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}

#valuess = (sum(student_marks[query_name])/3)
#print(round(valuess,2))  Doesn't Work !!! I don't know why 

print("{:.2f}".format(sum(x for x in student_marks[query_name])/3))