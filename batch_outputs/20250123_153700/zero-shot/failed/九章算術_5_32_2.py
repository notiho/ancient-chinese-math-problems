"""
今有穿地，袤一丈六尺，深一丈，上廣六尺，為垣積五百七十六尺。問︰穿地下廣幾何？
術曰：置垣積尺，四之為實。以深、袤相乘，又三之，為法。所得倍之，減上廣，餘即下廣。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the width of the bottom of a trench (下廣, denoted as `a`) given the dimensions of the trench and the volume of the wall (垣積).

Here is the Python code:


"""


from fractions import Fraction

# Given values
垣積 = 576  # Wall volume in cubic feet
袤 = Fraction(1, 1) + Fraction(6, 10)  # Length of the trench in zhang (1丈6尺 = 1.6丈)
深 = Fraction(1, 1)  # Depth of the trench in zhang
上廣 = Fraction(6, 10)  # Top width of the trench in zhang (6尺 = 0.6丈)

# Calculation
實 = 垣積 * 4  # Multiply the wall volume by 4
法 = 深 * 袤 * 3  # Multiply depth and length, then multiply by 3
下廣 = (實 / 法) * 2 - 上廣  # Divide 實 by 法, double the result, then subtract the top width

# Assign the result to variable `a`
a = 下廣

# Output the result
a


"""


### Explanation of the Code:
1. **垣積 (Wall Volume):** This is given as 576 cubic feet.
2. **袤 (Length):** The length of the trench is 1丈6尺, which is converted to 1.6丈 using fractions.
3. **深 (Depth):** The depth of the trench is 1丈.
4. **上廣 (Top Width):** The top width of the trench is 6尺, which is converted to 0.6丈 using fractions.
5. **實 (Intermediate Value):** Multiply the wall volume by 4.
6. **法 (Denominator):** Multiply the depth and length, then multiply by 3.
7. **下廣 (Bottom Width):** Divide 實 by 法, double the result, and subtract the top width.

### Result:
The variable `a` will contain the bottom width of the trench in zhang.
"""


"""
Variable 'a' has wrong value. Expected: 18/5, Actual: 4797/5"""
