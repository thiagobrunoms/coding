class BinaryGenerator:
    def generate_numbers(self, n: int) -> list:
        left = ""
        right = ""
        result = ["1"]
        for i in range(0, n // 2):
            left = result[i] + "0"
            right = result[i] + "1"
            result.append(left)
            result.append(right)

        print(type(result))
        return result
    
binary = BinaryGenerator().generate_numbers(5)
print(binary)
