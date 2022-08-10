class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for i in range(1, n + 1):
            char = ""
            if i % 3 == 0:
                char = char + "Fizz"
            if i % 5 == 0:
                char = char + "Buzz"
            if char == "":
                char = str(i)
            result.append(char)
        
        return result
        