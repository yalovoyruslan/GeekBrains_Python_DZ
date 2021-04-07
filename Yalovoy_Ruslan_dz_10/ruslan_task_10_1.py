class Matrix:

    def __init__(self, var_matrix):
        self.var_matrix = var_matrix

    def __add__(self, other):
        return Matrix([[item[i] + item_y[i] for i in range(len(item))]
                       for item, item_y in
                       zip(self.var_matrix, other.var_matrix)])

    def __str__(self):
        a = ''
        for item in range(len(self.var_matrix)):
            a += ' '.join(map(str, self.var_matrix[item])) + '\n'
        return a


x = Matrix([[2, 3, 7, 8], [8, 3, 3, 9]])
y = Matrix([[2, 9, 4, 3], [8, 3, 3, 9]])
v = x + y
print(x + y)
