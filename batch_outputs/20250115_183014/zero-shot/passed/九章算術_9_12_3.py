"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a尺 。
"""

"""
To solve the problem, let's translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
bamboo_height = Fraction(10, 1)  # 1丈 = 10尺
distance_from_base = Fraction(3, 1)  # 3尺

# Calculation
a = (bamboo_height - (distance_from_base * distance_from_base / bamboo_height)) / 2

# The height of the broken part
a  # in 尺


"""


The variable `a` will contain the height of the broken part in 尺.
"""


"""
"""
