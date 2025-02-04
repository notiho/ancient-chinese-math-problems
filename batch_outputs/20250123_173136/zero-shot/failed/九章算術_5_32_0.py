"""
今有穿地，袤一丈六尺，深一丈，上廣六尺，為垣積五百七十六尺。問︰穿地下廣幾何？
術曰：置垣積尺，四之為實。以深、袤相乘，又三之，為法。所得倍之，減上廣，餘即下廣。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
垣積 = 576  # 垣積 in square 尺
袤 = Fraction(1, 1) * 16  # 袤 in 尺 (1丈6尺 = 16尺)
深 = Fraction(1, 1) * 10  # 深 in 尺 (1丈 = 10尺)
上廣 = Fraction(1, 1) * 6  # 上廣 in 尺

# Calculation
實 = 垣積 * 4
法 = 深 * 袤 * 3
下廣 = (實 * 2 - 上廣) / 法

# Answer
a = 下廣
a


"""


This code calculates the value of `下廣` (represented as `a` in the answer). The result will be in 尺.
"""


"""
Variable 'a' has wrong value. Expected: 18/5, Actual: 767/80"""
