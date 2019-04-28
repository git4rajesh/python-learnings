 pip3 install overloading

 from overloading import overload


 Refer:
 https://overloading.readthedocs.io/en/latest/

 Use the overload decorator to register multiple implementations of a function.
 All variants must differ by parameter type or count.


 Why use overloading instead of *args / **kwargs?

Reduces the need for mechanical argument validation.
Promotes explicit call signatures, making for cleaner, more self-documenting code.
Enables the use of full type declarations and type checking tools.


Decorators

Overloading directives may be combined with other decorators.

The rule is to always apply the other decorator before the resulting function is passed to the overloading apparatus.
This means placing the custom decorator after the overloading directive:

@overload
@decorates_int_operation
def f(x: int):
    ...

@overload
@decorates_float_operation
def f(x: float):