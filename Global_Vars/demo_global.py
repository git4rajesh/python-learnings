class Demo_Global:
    """
     PP-Work: Re parenting WBS in PP and SOR is PP
     """

    x = 6


    def example(self):
        print(Demo_Global.x)

if __name__ == '__main__':
    demo_obj = Demo_Global()
    print(Demo_Global.__doc__)
    demo_obj.example()

