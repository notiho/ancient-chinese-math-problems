"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a尺 。
"""

#----- content starts here -----
"""
Suppose there is a circular log buried in a wall, and its size is unknown.
Using a measuring tool (a "ju"), it is measured such that the depth is 1 cun, and the length of the measuring tool's arc is 1 chi.
Question: what is the diameter of the log?

The procedure says: Take half the arc length of the measuring tool and square it.
If the depth is 1 cun, divide by 1.
Add the depth to the result, and this gives the diameter of the log.

Answer: the diameter of the log is *a* chi.
"""

# 深一寸
深寸 = Fraction(1, 10)  # 1 寸 = 1/10 尺

# 鐻道長一尺
鐻道 = 1  # 尺

# 半鐻道自乘
半鐻道 = 鐻道 / 2
半鐻道平方 = 半鐻道 * 半鐻道

# 如深寸而一，以深寸增之，即材徑
材徑 = 半鐻道平方 / 深寸 + 深寸

a = 材徑#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 2.6"""
