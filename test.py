class X:
    def __init__(self, id, name, age, height):
        self.id = id
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self):
        return f"id: {self.id} name: {self.name} age: {self.age}  height: {self.height}"


class Y:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"id: {self.id} name: {self.name} age: {self.age}"


if __name__ == '__main__':
    x = X(1, "ola", 3, 10)
    y = Y(2, "xau", 5)

    for k, v in x.__dict__.items():
        if hasattr(y, k):
            setattr(y, k, v)

    print(y.__dict__)

