# @Author  : xy.zhang
# @Email   : zhangxuyi@wanshare.com
# @Time    : 18-11-21


class Demo:
    name = "Demo"
    
    @classmethod
    def hello(cls):
        print(cls.name)


if __name__ == '__main__':
    Demo.hello()