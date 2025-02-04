"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical log buried in a wall, and its size is unknown.
Using a measuring tool (鐻), it is pressed into the wall to a depth of 1 cun, and the length of the chord (鐻道) is 1 chi.
Question: what is the diameter of the log?

The procedure says: Take half of the chord's length and square it. 
If the depth is 1 cun, divide by 1, and then add the depth to the result. 
This gives the radius of the log. Multiply the radius by 2 to get the diameter.

Answer: the diameter of the log is *a* chi.
"""

from fractions import Fraction

# Given values
鐻道 = 1  # chord length in chi
深 = Fraction(1, 10)  # depth in chi (1 cun = 1/10 chi)

# 半鐻道自乘
半鐻道 = Fraction(鐻道, 2)
半鐻道平方 = 半鐻道 ** 2

# 如深寸而一，以深寸增之
材半徑 = 半鐻道平方 / 深 + 深

# 材徑
材徑 = 2 * 材半徑

a = 材徑  # Diameter of the log in chi
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 26/5"""
