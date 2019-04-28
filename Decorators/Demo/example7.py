def tags(tag_name, doc_str):
    def tags_decorator(func):
        print(doc_str)
        def func_wrapper(name):
            return '<{0}>{1}</{0}>'.format(tag_name, func(name))
        return func_wrapper

    return tags_decorator


@tags('h1', 'Example for Decorators with params')
def get_text(name):
    return "Hello " + name


print(get_text("John"))
