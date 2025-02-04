"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a尺 。
"""

#----- content starts here -----
"""
Suppose there is a circular log buried in a wall, and its size is unknown.
Using a measuring tool, it is pressed into the log to a depth of 1 cun, and the length of the chord (the measuring tool's path) is 1 chi.
Question: what is the diameter of the log?

The procedure says: Take half of the chord's length and square it. Divide by the depth (1 cun), then add the depth to the result. This gives the diameter of the log.

Answer: the diameter of the log is *a* chi.
"""

from fractions import Fraction

# Given values
鐻道長 = 1  # chi (length of the chord)
深 = Fraction(1, 10)  # cun (depth, converted to chi since 1 chi = 10 cun)

# 半鐻道
半鐻道 = Fraction(鐻道長, 2)

# 半鐻道自乘
半鐻道平方 = 半鐻道 ** 2

# 如深寸而一 (divide by depth)
深分之一 = 半鐻道平方 / 深

# 以深寸增之 (add the depth)
材徑 = 深分之一 + 深

# Output the result
a = 材徑
a#----- content ends here -----

"""
"""
