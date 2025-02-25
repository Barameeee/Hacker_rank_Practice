string = 'abracadabra'
index,alphabet = input().split(' ')
index = int(index)
string = string[0:index]+alphabet+string[index+1:]
print(string)