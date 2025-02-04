"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical object (round timber) buried in a wall, and its size is unknown.
Using a measuring tool, the depth is found to be 1 cun, and the chord length of the arc is 1 chi.
Question: what is the diameter of the cylinder?

The procedure says: Take half of the chord length, square it, and divide it by the depth (1 cun).
Add the depth to the result, and this gives the diameter of the cylinder.

Answer: the diameter of the cylinder is *a* chi.
"""

from fractions import Fraction

# Given values
鐻道長 = 1  # Chord length in chi
深寸 = Fraction(1, 10)  # Depth in chi (1 cun = 1/10 chi)

# 半鐻道
半鐻道 = Fraction(鐻道長, 2)

# 半鐻道自乘
半鐻道平方 = 半鐻道 ** 2

# 如深寸而一
深寸分之一 = 半鐻道平方 / 深寸

# 以深寸增之，即材徑
材徑 = 深寸分之一 + 深寸

# Answer
a = 材徑
a#----- content ends here -----

"""
"""
