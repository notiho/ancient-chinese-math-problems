"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical log embedded in a wall, and its size is unknown.
Using a measuring tool (鐻), it is pressed into the log to a depth of 1 cun, and the length of the chord (鐻道) is measured to be 1 chi.
Question: what is the diameter of the log?

The procedure says: Take half of the chord length, square it, and divide by the depth (1 cun). 
Add the depth to the result, and this gives the diameter of the log.

Answer: the diameter of the log is *a* chi.
"""

from fractions import Fraction

# Given values
鐻道 = 1  # chord length in chi
深 = Fraction(1, 10)  # depth in chi (1 cun = 1/10 chi)

# Half of the chord length
半鐻道 = Fraction(鐻道, 2)

# Square the half chord length
半鐻道平方 = 半鐻道 ** 2

# Divide by the depth
徑部分 = 半鐻道平方 / 深

# Add the depth to get the diameter
材徑 = 徑部分 + 深

# Final answer
a = 材徑
a#----- content ends here -----

"""
"""
