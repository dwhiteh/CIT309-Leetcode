class Solution:
    def romanToInt(self, s: str = input("Enter a Roman Numeral: ")) -> int:
        roman_num_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        answer = 0
        current = 0
        for numeral in s[::-1]:
            previous = current
            current = roman_num_dict.get(numeral)
            if current < previous:
                answer -= current
            else:
                answer += current
        return answer

solution = Solution()
print("The Roman Numeral you entered converted to an integer is: ",solution.romanToInt(),".")
