"""
今有羨除，下廣六尺，上廣一丈，深三尺，末廣八尺，無深，袤七尺。問︰積幾何？
術曰：并三廣，以深乘之，又以袤乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the volume of a frustum-like shape with specified dimensions. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
lower_width = Fraction(6)  # 下廣 (6 尺)
upper_width = Fraction(10)  # 上廣 (1 丈 = 10 尺)
depth = Fraction(3)  # 深 (3 尺)
end_width = Fraction(8)  # 末廣 (8 尺)
length = Fraction(7)  # 袤 (7 尺)

# Step 1: Add the three widths together
total_width = lower_width + upper_width + end_width

# Step 2: Multiply by the depth
volume_1 = total_width * depth

# Step 3: Multiply by the length
volume_2 = volume_1 * length

# Step 4: Divide by 6
a = volume_2 / Fraction(6)

# The answer is stored in variable 'a'
a  # This represents the volume in cubic 尺
#----- content ends here -----


"""


The solution is stored in the variable `a`, which represents the volume in cubic 尺.
"""


"""
"""
