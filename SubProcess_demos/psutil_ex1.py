# import psutil
from subprocess import PIPE, Popen

cmd1 = 'python.exe sample1.py'

# cmd2 = 'dir'

status = False

for i in range(1,3):
    proc = Popen(cmd1, shell=False)
    proc.communicate(input=None)
    if proc.returncode == 0:
        status = True

    print('-------', status)