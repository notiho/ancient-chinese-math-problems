"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
術曰：三十五乘粟，二十五而一，為率。多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實。並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法。又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從。開立方除之，即窖深。各加差，即方、徑、高。
答曰：方徑各 a丈 ，高 b丈 ，深 c丈 。
"""

"""
To solve this problem, we will carefully follow the ancient procedure ("術") step by step and translate it into Python code. Here's the solution:


"""


from fractions import Fraction
from math import pow

# 粟三千七十二石
粟 = 3072

# 三十五乘粟，二十五而一，為率
率 = Fraction(35 * 粟, 25)

# 方於窖深二尺，少於倉高三尺
方差 = 2
高差 = 3

# 多自乘，以並多少乘之
多 = 方差 + 高差
多自乘 = 多 * 多
並多少 = 方差 * 高差

# 以乘一十四，如二十五而一，所得以減率，余為實
實 = 率 - Fraction(14 * 並多少, 25)

# 並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法
方法 = 多自乘 + Fraction(14 * 並多少 * 多 * 2, 25)

# 又並多少，以乘一十四，如二十五而一，加多加之，為廉法
廉法 = 並多少 + Fraction(14 * 並多少, 25) + 多

# 從。開立方除之，即窖深
窖深 = pow(Fraction(實, 方法), Fraction(1, 3))

# 各加差，即方、徑、高
方 = 窖深 + 方差
徑 = 窖深 + 方差
高 = 窖深 + 高差

# 答案
a = 方  # 方徑各 a 丈
b = 高  # 高 b 丈
c = 窖深  # 深 c 丈


"""


### Explanation of the Code:
1. **Input and Constants**: The total amount of 粟 (grain) is given as 3072 石. The relationships between the dimensions (方差 and 高差) are also provided.
2. **Rate Calculation**: The rate (率) is calculated as per the procedure.
3. **Intermediate Calculations**: Using the relationships between 方差, 高差, and the given formulas, we calculate `實`, `方法`, and `廉法`.
4. **窖深 Calculation**: The depth of the circular pit (窖深) is calculated by taking the cube root of `實 / 方法`.
5. **Final Dimensions**: Using 窖深, we calculate 方 (square side), 徑 (circular diameter), and 高 (height).

### Final Output:
- 方徑 each equals `a` 丈.
- 高 equals `b` 丈.
- 深 equals `c` 丈.
"""


"""
Variable 'a' has wrong value. Expected: 8/5, Actual: 6.1857254170332965
Variable 'b' has wrong value. Expected: 19/10, Actual: 7.1857254170332965
Variable 'c' has wrong value. Expected: 7/5, Actual: 4.1857254170332965"""
