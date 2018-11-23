# @Author  : xy.zhang
# @Email   : zhangxuyi@wanshare.com
# @Time    : 18-11-22

print("-----------------SingletonMetaclass-----------------")


class SingletonMetaclass(type):
    _instances = dict()
    
    def __call__(cls, *args, **kwargs):
        print("metaclass __call__ enter")
        print("cls: ", type(cls).__name__)
        print("args: ", args)
        print("kwargs: ", kwargs)
        # ret = cls._instances.setdefault(cls, super().__call__(*args, **kwargs))
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        print("metaclass __call__ exit")
        return cls._instances[cls]
    
    def __new__(mcs, *args, **kwargs):
        print("metaclass __new__ enter")
        print("mcs: ", type(mcs).__name__)
        print("args: ", args)
        print("kwargs: ", kwargs)
        ret = super().__new__(mcs, *args, **kwargs)
        print("metaclass new return :", type(ret).__name__)
        print("metaclass __new__ exit")
        return ret
    
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        print("metaclass __init__ enter")
        print("name: ", name)
        print("bases: ", bases)
        print("attrs: ", attrs)
        print("metaclass __init__ exit")


print("-----------------Demo-----------------")


class Demo(metaclass=SingletonMetaclass):
    
    def __init__(self):
        print("Demo __init__ enter")
        super().__init__()
        print("Demo __init__ exit")
        
    def __new__(cls, *args, **kwargs):
        print("Demo __new__ enter")
        print("cls: ", type(cls).__name__)
        print("args: ", args)
        print("kwargs: ", kwargs)
        ret = super().__new__(cls, *args, **kwargs)
        print("Demo new return:", type(ret).__name__)
        print("Demo __new__ exit")
        return ret
    
    def __call__(self, *args, **kwargs):
        print("Demo __call__ enter")
        print("args: ", args)
        print("kwargs: ", kwargs)
        print("Demo __call__")
        print("Demo __call__ exit")


if __name__ == '__main__':
    print("-----------------main-----------------")
    d = Demo()
    print("==================")
    d2 = Demo()
