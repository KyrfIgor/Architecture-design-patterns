def func():
    print('test')

func()


class NewClass:
    def __call__(self, *args, **kwargs):
        pass

obj = NewClass()
obj()
