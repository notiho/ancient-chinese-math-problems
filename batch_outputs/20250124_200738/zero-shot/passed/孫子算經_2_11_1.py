"""
今有圓窖，周五丈四尺，深一丈八尺。問：受粟幾何？
術曰：先置周五丈四尺相乘，得二千九百一十六尺，以深一丈八尺乘之，得五萬二千四百八十八尺；以一十二除之，得四千三百七十四尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
周 = Fraction(5 * 10 + 4)  # 周 is 5丈4尺, converted to 尺
深 = Fraction(1 * 10 + 8)  # 深 is 1丈8尺, converted to 尺
斛法 = Fraction(1, 1) + Fraction(6, 10) + Fraction(2, 100)  # 1尺6寸2分

# Step 1: Calculate 周 squared
周_squared = 周 * 周

# Step 2: Multiply 周_squared by 深
體積 = 周_squared * 深

# Step 3: Divide by 12
體積除以十二 = 體積 / 12

# Step 4: Divide by 斛法 to get the answer in 斛
a = 體積除以十二 / 斛法

# The answer is stored in variable 'a'
a
#----- content ends here -----


"""


This code calculates the volume of the circular granary and determines how many "斛" of grain it can hold. The result is stored in the variable `a`.
"""


"""
"""
