class Solution:
    def romanToInt(self, s: str = input("Enter a Roman Numeral: ")) -> int:
        #Define Value of Roman Numeral
        roman_num_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        #This will keep track of the integer value of the Roman Numeral
        answer = 0
        #This is the value of the current roman numeral being converted to integer
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
