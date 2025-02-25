string = 'llasdnknqlwejkalsdxkkdnk'
sub_string = 'dnk'

print(string.find(sub_string))

'''
print(string.count('cdc'))
'''

counter = 0
for i in range (len(string)):
    if sub_string == string[i:len(sub_string)+i]:
        counter += 1
print(counter)

