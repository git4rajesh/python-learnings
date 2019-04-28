http://stackabuse.com/pythons-classmethod-and-staticmethod-explained/

1. @classmethod methods also have a mandatory first argument, but this argument isn't a class instance, it's actually the
uninstantiated class itself.

2. @classmethod can be used for creating the static factory pattern very well, encapsulating the parsing logic inside
of the method itself.

3. ex2.py,  Imagine if a Student object could be serialized in to many different formats.
You could use this same strategy to parse them all

4. The decorator becomes even more useful when you realize its usefulness in sub-classes. Since the class object is given to
you within the method, you can still use the same @classmethod for sub-classes as well.