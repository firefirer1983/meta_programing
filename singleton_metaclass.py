# @Author  : xy.zhang
# @Email   : zhangxuyi@wanshare.com
# @Time    : 18-11-20


class SingletonMetaClass(type):
    
    _instance = dict()
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(cls, *args, **kwargs)
        return cls._instance[cls]


class Me(metaclass=SingletonMetaClass):
    
    def __init__(self):
        print("i am fyman")

    def __call__(self, *args, **kwargs):
        print("call me baby")
        

me = Me()


you = Me()
you()
