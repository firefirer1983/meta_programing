# @Author  : xy.zhang
# @Email   : zhangxuyi@wanshare.com
# @Time    : 18-11-20


class ListMetaClass(type):
    
    def __new__(cls, name, bases, attrs):
        attrs["add"] = lambda self, value: self.append(value)
        clz = super().__new__(cls, name, bases, attrs)
        return clz

    def __call__(self, *args, **kwargs):
        print("this is the instantiate function")


class MyList(list, metaclass=ListMetaClass):
    pass


mlist = MyList()
mlist.add("hello world")
print(mlist)


class MyClass:
    
    def __call__(self, *args, **kwargs):
        print("args: ", args)
        print("kwargs: ", kwargs)


me = MyClass()
me()