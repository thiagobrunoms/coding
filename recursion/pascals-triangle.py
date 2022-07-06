class PascalTriangle:
    def calculate_value(self, i: int, j: int) -> int:
        if i == j or j == 1:
            return 1

        return self.calculate_value(i-1, j-1) + self.calculate_value(i-1, j)


pascal = PascalTriangle()
result = pascal.calculate_value(5, 3)
print(result)
