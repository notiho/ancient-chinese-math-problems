"""
今有羨除，下廣六尺，上廣一丈，深三尺，末廣八尺，無深，袤七尺。問︰積幾何？
術曰：并三廣，以深乘之，又以袤乘之，六而一。
荅曰： a尺 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a truncated prism. Here's the Python code:


"""


from fractions import Fraction

# Given dimensions
lower_width = Fraction(6)  # 下廣 (6尺)
upper_width = Fraction(10)  # 上廣 (1丈 = 10尺)
depth = Fraction(3)  # 深 (3尺)
end_width = Fraction(8)  # 末廣 (8尺)
length = Fraction(7)  # 袤 (7尺)

# Formula: (lower_width + upper_width + end_width) * depth * length / 6
a = (lower_width + upper_width + end_width) * depth * length / 6

# The result is stored in variable 'a'


"""


The value of `a` will be the volume of the truncated prism in cubic 尺.
"""


"""
"""
