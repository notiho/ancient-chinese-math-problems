"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
術曰：三十五乘粟，二十五而一，為率。多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實。並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法。又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從。開立方除之，即窖深。各加差，即方、徑、高。
答曰：方徑各 a丈 ，高 b丈 ，深 c丈 。
"""

"""
This problem involves a complex ancient Chinese mathematical procedure for determining the dimensions of a square granary and a circular silo. Below is the Python implementation of the procedure:


"""


from fractions import Fraction
from math import pow

# 粟三千七十二石
粟 = 3072

# 三十五乘粟，二十五而一，為率
率 = Fraction(35 * 粟, 25)

# 多自乘
多 = 3  # The difference between the square granary and the circular silo depths (given in the problem)
多自乘 = 多 * 多

# 以並多少乘之
並多少 = 2  # The difference between the granary height and the silo depth (given in the problem)
並多少乘之 = 並多少 * 多

# 以乘一十四，如二十五而一
乘一十四 = Fraction(14, 25)
所得 = 並多少乘之 * 乘一十四

# 所得以減率，余為實
實 = 率 - 所得

# 並多少，以乘多，倍之
倍之 = 2 * 並多少 * 多

# 乘一十四，如二十五而一
乘一十四_2 = 倍之 * 乘一十四

# 多自乘加之，為方法
方法 = 多自乘 + 乘一十四_2

# 又並多少，以乘一十四，如二十五而一
廉法 = 並多少 * 乘一十四

# 加多加之，為廉法，從
廉法 += 多

# 開立方除之，即窖深
窖深 = pow(float(實 / 方法), 1/3)

# 各加差，即方、徑、高
深 = Fraction(窖深)
方 = 深 + 多
徑 = 方
高 = 深 + 並多少

a = 方
b = 高
c = 深

# Output results
print(f"方徑各 {a} 丈 ，高 {b} 丈 ，深 {c} 丈 。")


"""


### Explanation of the Code:
1. **Input Values**: The total amount of grain (`粟`), the differences between the square granary and circular silo depths (`多`), and the difference between the granary height and silo depth (`並多少`) are given.
2. **Procedure**: The procedure follows the ancient Chinese algorithm step by step, as described in the problem.
3. **Fraction Usage**: The `Fraction` class is used to ensure precise calculations, as the problem involves ratios and divisions.
4. **Cube Root**: The depth of the silo (`窖深`) is calculated by taking the cube root of the result (`實 / 方法`).
5. **Final Dimensions**: The dimensions of the square granary (`方`), the circular silo's diameter (`徑`), the granary height (`高`), and the silo depth (`深`) are calculated.

### Final Answer:
The values of `a`, `b`, and `c` represent the dimensions of the square granary and circular silo:
- `a`: The side length of the square granary and the diameter of the circular silo.
- `b`: The height of the square granary.
- `c`: The depth of the circular silo.
"""


"""
Variable 'a' has wrong value. Expected: 8/5, Actual: 2671230043636601/281474976710656
Variable 'b' has wrong value. Expected: 19/10, Actual: 2389755066925945/281474976710656
Variable 'c' has wrong value. Expected: 7/5, Actual: 1826805113504633/281474976710656"""
