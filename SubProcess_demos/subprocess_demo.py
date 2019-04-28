import subprocess, re


remote_cmd = 'ipconfig'
proc = subprocess.Popen(remote_cmd, stdout=subprocess.PIPE, shell=False)

proc = proc.decode(encoding='windows-1252')
for line in iter(proc.stdout.readline, b''):
    str(line, encoding)
    if re.search('IPv4 Address', line):
        print('my_out', line)

proc.communicate(input=None)


