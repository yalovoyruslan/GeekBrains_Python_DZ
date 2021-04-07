class Cage:
    def __init__(self, amount_cells):
        self.amount_cells = amount_cells

    def __add__(self, other):
        result = self.amount_cells + other.amount_cells
        return Cage(result)

    def __sub__(self, other):
        if self.amount_cells > other.amount_cells:
            result = self.amount_cells - other.amount_cells
        else:
            return 'Вычитание выполнить невоможно'
        return Cage(result)


    def __mul__(self, other):
        result = self.amount_cells * other.amount_cells
        return Cage(result)

    def __floordiv__(self, other):
        self.amount_cells = self.amount_cells // other.amount_cells
        return Cage(self.amount_cells)

    def make_order(self, in_row):
        int_row = self.amount_cells // in_row
        short_row = self.amount_cells % in_row
        visual_cage = ('*' * in_row + '\n') * int_row + '*' * short_row
        return str(visual_cage)


a = Cage(4)
b = Cage(18)
z = b + a
x = b-a
c = x * a
v = b // a

print(f'клетка а \n{a.make_order(10)}')
print(f'клетка z \n{z.make_order(10)}')
print(f'клетка x \n{x.make_order(10)}')
print(f'клетка c \n{c.make_order(10)}')
print(f'клетка v \n{v.make_order(10)}')

