import subprocess

dosCommand = r'xcopy \\10.132.16.2\E$\temp\Test1.bat D:\Temp /f /j /v /y /z'
process = subprocess.Popen(dosCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)

