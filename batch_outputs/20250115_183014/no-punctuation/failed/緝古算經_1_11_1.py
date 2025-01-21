"""
假令有粟三千七十二石欲作方倉一圓窖一令徑與方等方於窖深二尺少於倉高三尺盛各滿中而粟適盡問方徑高深各多少
術曰三十五乘粟二十五而一為率多自乘以並多少乘之以乘一十四如二十五而一所得以減率余為實並多少以乘多倍之乘一十四如二十五而一多自乘加之為方法又並多少以乘一十四如二十五而一加多加之為廉法從開立方除之即窖深各加差即方徑高
答曰方徑各 a丈 高 b丈 深 c丈 
"""

"""
This is a complex problem involving the calculation of the dimensions of a square granary and a circular granary, given specific conditions. Let's translate the procedure into Python step by step.

### Problem Description:
There are 3072 shi of grain. A square granary and a circular granary are to be constructed such that:
1. The diameter of the circular granary equals the side length of the square granary.
2. The depth of the circular granary is 2 chi less than the height of the square granary.
3. The height of the square granary is 3 chi greater than the depth of the circular granary.
4. Both granaries are filled to capacity, and the total volume exactly matches the given amount of grain.

The procedure provides a method to calculate the side length (or diameter), height, and depth.

---

### Procedure Translation:

"""


from fractions import Fraction
from math import pow

# 粟三千七十二石
粟 = 3072

# 三十五乘粟，二十五而一，為率
率 = Fraction(35 * 粟, 25)

# 多自乘，以並多少乘之，以乘一十四如二十五而一
多 = 1  # Initial guess for 多 (side length or diameter)
while True:
    多自乘 = 多 * 多
    並多少 = 多 + 多
    實 = 並多少 * 多自乘 * Fraction(14, 25)
    減率 = 實 - 率

    # If the difference is small enough, break the loop
    if abs(減率) < Fraction(1, 1000000):
        break

    # Adjust 多 based on the difference
    多 += Fraction(1, 1000)

# 多自乘，加之，為方法
方法 = 多自乘 + 減率

# 又並多少，以乘一十四如二十五而一，加多，加之，為廉法
廉法 = 並多少 * Fraction(14, 25) + 多 + 減率

# 從開立方，除之，即窖深
窖深 = pow(float(方法 / 廉法), 1/3)

# 各加差，即方徑高
方徑 = 多
高 = 窖深 + Fraction(3, 10)  # Add 3 chi
深 = 窖深 - Fraction(2, 10)  # Subtract 2 chi

# 答案
a = 方徑
b = 高
c = 深

print(f"方徑各 {a} 丈, 高 {b} 丈, 深 {c} 丈")


"""


---

### Explanation of the Code:
1. **Initial Setup**: The total grain volume is given as 3072 shi. The procedure starts by calculating a "rate" (`率`) based on the grain volume.
2. **Iterative Calculation**: The side length (or diameter) `多` is iteratively adjusted until the calculated difference (`減率`) is sufficiently small.
3. **Formulas**: The procedure uses specific formulas to calculate the method (`方法`) and the edge method (`廉法`), which are then used to determine the depth (`窖深`).
4. **Final Dimensions**: Once the depth is determined, the side length (or diameter), height, and depth are calculated based on the relationships provided in the problem.

---

### Note:
This problem involves iterative calculations and cube roots, which are not explicitly detailed in the original procedure but are implied by the context. The Python code uses fractions for precision and approximates the cube root using `pow`.
"""


"""
Timed out"""
