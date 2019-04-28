import sys
import os

try:
    error_msg = 'Please troubleshoot the issue manually. Logging off !!'
    print(error_msg)
    # os._exit(1)
    sys.exit(1)
except :
    print('Inside except block')
    os._exit(1)
finally:
    print('Inside finally block')
