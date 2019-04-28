import os
statinfo = os.stat('somefile.txt')
print(statinfo.st_size)

