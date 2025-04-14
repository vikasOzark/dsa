class MyMeta(type):
    def __new__(cls, name, bases, clsdict):
        clsdict['show'] = lambda self: "hello from metaclass"
        return super().__new__(cls, name, bases, clsdict)


class MyCls(metaclass=MyMeta):
    def show(self):
        print("===============")


m = MyCls()
print(m.show())
