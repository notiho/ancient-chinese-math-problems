"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a tree 2 zhang tall, with a circumference of 3 chi. A vine grows at the base of the tree and wraps around it 7 times, reaching the top of the tree.  
Question: how long is the vine?

Answer: the vine is *a* zhang long.
"""

# 木長二丈
木高 = 2  # in zhang

# 圍之三尺
木圍 = 3  # in chi

# Convert 木圍 to zhang (1 zhang = 10 chi)
木圍 = 木圍 / 10  # in zhang

# 葛纏木七周
纏繞次數 = 7

# 葛長 follows the Pythagorean theorem for each wrap:
# 葛長 = sqrt((木高 / 纏繞次數)^2 + 木圍^2) * 纏繞次數
from fractions import Fraction
from math import sqrt

# Calculate 葛長
單圈高度 = 木高 / 纏繞次數
單圈長度 = sqrt(單圈高度**2 + 木圍**2)
葛長 = 單圈長度 * 纏繞次數

# Convert 葛長 to zhang
a = Fraction(葛長).limit_denominator(1000)  # Simplify to a fraction

a#----- content ends here -----

"""
"""
