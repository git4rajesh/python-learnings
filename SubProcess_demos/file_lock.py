import fcntl
x = open('foo', 'w+')
fcntl.flock(x, fcntl.LOCK_EX | fcntl.LOCK_NB)