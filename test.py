class X:
    def __init__(self, first, last):
        self.first = first
        self.last = last


def print_x(*args, **kwargs):
    for x in args:
        print(x)

    for k, v in kwargs.items():
        print(k, v)

if __name__ == '__main__':

    print_x('a', 'b', 'c', )

    # x = {'first': 'a', 'last': 'b'}
    #
    # print_x(**x)
    # print_x(first='a', last='b')
