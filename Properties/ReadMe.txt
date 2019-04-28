https://metallapan.se/post/What-s-the-point-of-properties-in-Python/

Encapsulation!'. What will we do if we need to control access to x,
make it read-only or do something else to it?

1. We can have validations on setting an instance member in the setter property as shown in ex1.
2. We can create read only instance members as shown in ex2.

3. No underscore: it's a public variable.
   One underscore: it's a protected variable.
   Two underscores: it's a private variable.

4. We can read-write-delete attributes using Properties.

    3 Decorators are used with Property as shown in ex3:

    @property = Getter
    @x.setter = Setter
    @x.deleter = Deleter

    The methods setter and deleter will be based on @property method name.

    b. Refer ex3 for Delete operation which removes the instance member itself.

5. Refer ex4 which demonstrates using @property and @setter decorators to create
   different instance members based on units.

5. Summary:
-----------

Coming to the advantages what comes to my mind are as follows,
1. Class internals can change without worrying too much about the interfaces.
2. One can create read or read-write or read-write-delete attributes.
3. Perform cleanup for properties when deleted
4. One can expose complex calculated fields as properties
5. One can do some validation (e.g. validating email address expression)