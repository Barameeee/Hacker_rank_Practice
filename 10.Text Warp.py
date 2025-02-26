texts = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
width = 4
'''
nom = len(texts)
print(nom)
print(int(nom/width))

istart = 0
istop = 1
for i in range(int(nom/width)): 
    print(i)
    istop = (i+1)*width
    print(texts[istart:istop]) 
'''
'''
bstart = -len(texts) 
bstop = width
for i in range(int(nom/width)+1):
    print(texts[bstart:bstop])
    bstart += width
    bstop += width
'''
def wrap(string, max_width):
    bstart = -len(string) 
    bstop = max_width
    result_str = ''
    for i in range(int(len(string)/max_width)+1):
        result_str += string[bstart:bstop]
        if i < (int(len(string)/max_width)):
            result_str += '\n'
        #print(string[bstart:bstop])
        bstart += max_width
        bstop += max_width
    return (result_str)

result = wrap(texts, width)
print(result)