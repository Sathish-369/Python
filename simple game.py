class Parrot:
    def fly(self):
        print("parrot can fly")

    def swim(self):
        print("parrot can't swim")


class Penguin:

    def fly(self):
        print("penguin can't fly")

    def swim(self):
        print("penguin can swim")


def flingTest(obj):  # edu tha common inter face edha vachu enna panna poro
    obj.fly()


def swimTest(obj):
    obj.swim()


parr = Parrot()

pen = Penguin()

flingTest(parr)
flingTest(pen)

swimTest(parr)
swimTest(pen)