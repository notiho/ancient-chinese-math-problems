"""
今有井徑五尺，不知其深。立五尺木於井上，從木末望水岸，入徑四寸。問︰井深幾何
術曰：置井徑五尺，以入徑四寸減之，餘，以乘立木五尺為實。以入徑四寸為法。實如法得一寸。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
井徑 = Fraction(5)  # 井徑 (井的直徑) in 尺
立木 = Fraction(5)  # 立木 (木的長度) in 尺
入徑 = Fraction(4, 10)  # 入徑 (木末入井徑的部分) in 尺 (4寸 = 4/10尺)

# Calculation
實 = (井徑 - 入徑) * 立木  # 實 = (井徑 - 入徑) * 立木
井深 = 實 / 入徑  # 井深 = 實 / 入徑

# Convert 井深 to 丈
a = 井深 / 10  # 1丈 = 10尺

# Result
a


"""


The variable `a` will contain the depth of the well in 丈.
"""


"""
"""
