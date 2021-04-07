from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def f_cloth(self):
        pass


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    def f_cloth(self):
        cloth = 2 * self.h + 0.3
        return cloth


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def f_cloth(self):
        cloth = self.v / 6.5 + 0.5
        return cloth


a = Costume(2)
b = Coat(3)
print(f'{round(a.f_cloth() + b.f_cloth, 2)} м ткани необходимо для костюма "а" и пальто "b"')
