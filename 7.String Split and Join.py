'''
def split_and_join(line):
    # write your code here
    lists = line.split(' ')
    '-'.join(lists)
    return lists
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    '''
l = 'I love Thailand'
print(l)
lists = l.split(' ')
print(lists)
o = '-'.join(lists)
print(o)