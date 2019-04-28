import sys
import subprocess

# ARGS = sys.argv
# CMD = ARGS[:]
# CMD.pop(0)

command = sys.argv[1]
input_file = sys.argv[2]
operator = sys.argv[3]
output_file = sys.argv[4]

CMD = [command, input_file, operator, output_file]

print('The command executed is :' , CMD)

return_status = subprocess.check_call(CMD, shell=True)

if return_status == 0:
    print('The return status is: %s' %(return_status))
else:
    print('Failure in creating output file and return status is %s' %(return_status) )





