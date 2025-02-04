"""
假令有粟三千七十二石欲作方倉一圓窖一令徑與方等方於窖深二尺少於倉高三尺盛各滿中而粟適盡問方徑高深各多少
術曰三十五乘粟二十五而一為率多自乘以並多少乘之以乘一十四如二十五而一所得以減率余為實並多少以乘多倍之乘一十四如二十五而一多自乘加之為方法又並多少以乘一十四如二十五而一加多加之為廉法從開立方除之即窖深各加差即方徑高
答曰方徑各 a丈 高 b丈 深 c丈 
"""

"""
This is a complex problem involving the calculation of the dimensions of a square warehouse and a circular pit, given a specific volume of grain. Below is the translation of the procedure into Python code:


"""


"""
Suppose there are 3072 shi of grain. It is desired to construct a square warehouse and a circular pit.
The diameter of the pit is equal to the side length of the square warehouse.
The depth of the pit is 2 chi less than the height of the warehouse, and the height of the warehouse is 3 chi greater than the depth of the pit.
Both the warehouse and the pit are filled to capacity, and the grain is exactly used up.
Question: What are the side length (or diameter), height, and depth?

The procedure says:
1. Multiply 35 by the grain and divide by 25 to get the initial rate.
2. Multiply the larger dimension by itself, then multiply by the smaller dimension.
3. Multiply by 14 and divide by 25 to get the result.
4. Subtract the rate from the result to get the remainder.
5. Multiply the larger dimension by itself and add the remainder to get the square method.
6. Add the remainder to the larger dimension to get the edge method.
7. Extract the cube root and divide to get the depth of the pit.
8. Add the difference to get the side length, height, and depth.

Answer: The side length (or diameter) is *a* zhang, the height is *b* zhang, and the depth is *c* zhang.
"""

from fractions import Fraction

# 粟三千七十二石
粟 = 3072

# Step 1: 三十五乘粟，二十五而一為率
率 = Fraction(35 * 粟, 25)

# Step 2: 多自乘，以並多少乘之
多 = 1  # Initial guess for the side length (or diameter)
並多少 = 1  # Initial guess for the height difference
while True:
    # Step 3: 以乘一十四如二十五而一，所得以減率余為實
    實 = Fraction(14 * 多 * 多 * 並多少, 25) - 率

    # Step 4: 並多少以乘多倍之，乘一十四如二十五而一
    方法 = 多 * 多 + 實
    廉法 = 並多少 * Fraction(14, 25) + 多 + 實

    # Step 5: 從開立方除之，即窖深
    窖深 = round(方法 ** (1 / 3))

    # Step 6: 各加差，即方徑高
    方徑 = 多
    高 = 窖深 + 3
    深 = 窖深

    # Check if the calculations satisfy the constraints
    if abs(高 - 深 - 3) < 1e-6 and abs(深 - 高 + 2) < 1e-6:
        break

    # Update guesses
    多 += 1
    並多少 += 1

a = 方徑
b = 高
c = 深


"""


### Explanation of the Code:
1. **Input and Initialization**: The total grain volume is given as 3072 shi. Initial guesses for the side length (or diameter) and height difference are set.
2. **Rate Calculation**: The rate is calculated using the formula provided in the procedure.
3. **Iterative Calculation**: The dimensions are iteratively adjusted until they satisfy the constraints of the problem.
4. **Output**: The side length (or diameter), height, and depth are calculated and stored in `a`, `b`, and `c`, respectively.

This code follows the ancient procedure step by step, using Python's `Fraction` class to handle fractional calculations accurately.
"""


"""
Code error: type complex doesn't define __round__ method"""
