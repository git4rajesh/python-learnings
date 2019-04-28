Using decorators can be very helpful but note that it can be very hard to debug the code
with them.
One of the issue that you can face is based on the decorators nature.
Since decorator is simply a function that wraps original one so it will
replace function.__name__ property to it’s own name and that can cause some misunderstanding
during debugging your code and(or) using introspection(inspect/traceback module and etc.
 in some certain conditions).