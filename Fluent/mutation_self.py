class Poem(object):
    def __init__(self, content):
        self.content = content

    def indent(self, spaces=4):
        self.content = " " * spaces + self.content
        return self

    def suffix(self, content):
        self.content += " - {}".format(content)
        return self

    # def __str__(self):
    #     return self.content

# print(Poem('Road Not Taken').indent(4).suffix('Rober Frost').content)
p = Poem('Road Not Taken')
q = p.indent(4)
r = p.indent(2)
print(str(q) == str(r))
print(id(q), id(r))

