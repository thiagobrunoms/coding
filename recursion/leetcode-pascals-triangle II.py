class PascalTriangle:
    def calculate_value(self, i: int, j: int) -> int:
        if i == j or j == 1:
            return 1

        return self.calculate_value(i-1, j-1) + self.calculate_value(i-1, j)

    def get_row(self, rowIndex: int) -> list:
        row_values = []

        for j in range(1, rowIndex + 1):
            print('looking for ', rowIndex, j)
            result = self.calculate_value(rowIndex, j)
            row_values.append(result)

        return row_values


pascal = PascalTriangle()
result = pascal.get_row(7)
print(result)
