class MyCls:
    a = 22
    b = 33
    def __init__(self, data: str, a, b):
        self.data = data
        self.a = a
        self.b = b

    @staticmethod
    def some(a, b):
        return a + b

    @classmethod
    def some_cls(cls):
        return cls.a + cls.b

if __name__ == '__main__':
    a = MyCls('some name', 2, 5)
    # print(a.a + a.b)
    # print(a.some_cls())
    # print(MyCls.some_cls())
    print(a.__module__)