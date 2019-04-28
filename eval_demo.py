class A:
    d = 1
    def __init__(self):
        a = 5
        b = 'Raj'
        print('Inside init a = %s and b = %s' %(a,b))

    def print_a(self):
        print('Inside class A')


if __name__ == '__main__':
  class_name = 'A'
  clsA = eval(class_name)
  print(clsA.d)

  obj = clsA()
  obj.print_a()


