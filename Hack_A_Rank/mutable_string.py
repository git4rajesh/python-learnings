string = "abcd"
l = list(string)
l[3] = 'k'
string = ''.join(l)
print(string)
