https://www.programiz.com/python-programming/closure

1. In ex1, the last line of the function print_msg() function does a call to printer().

2. In the ex2 the last line of the function print_msg() returned the printer() function instead of calling it.

3. When do we have a closure?

   - We must have a nested function (function inside a function).
   - The nested function must refer to a value defined in the enclosing function.
   - The enclosing function must return the nested function.

4. When to use closures?
    Closures can avoid the use of global values and provides some form of data hiding.
    It can also provide an object oriented solution to the problem.
    When there are few methods (one method in most cases) to be implemented in a class,
    closures can provide an alternate and more elegant solutions.
    But when the number of attributes and methods get larger, better implement a class.

    Decorators in Python make an extensive use of closures as well.

More on Closures:
==================
http://www.bogotobogo.com/python/python_closure.php

1. A closure is a combination of code and scope

2. Sometimes we want a function to retain a value when it was created even though the scope cease to exist.
   This technique of using the values of outer parameters within a dynamic function is another way of defining the closure.

3. In summary, a closure is a function (object) that remembers its creation environment (enclosing scope).

4. Closure and Lambda Functions.Refer ex4


Closure vs Classes?
==================
https://stackoverflow.com/questions/3182603/objects-or-closures-when-to-use

1. As a rule of thumb:
If the thing is really only a single function, and it is only capturing static state,
then consider a closure.
If the thing is intended to have mutable state, and/or has more than one function, use a class.
