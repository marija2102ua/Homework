class Human(object):
    def __init__(self):
        self.human = "human"


class Women(Human):
    def __init__(self, name):
        self.sex = "women"
        self.name = name


class Man(Human):
    def __init__(self, name):
        self.sex = "man"
        self.name = name


def God():
    man = Man("Adam")
    women = Women("Eva")
    return [man, women]


if __name__ == '__main__':
    print(God)
