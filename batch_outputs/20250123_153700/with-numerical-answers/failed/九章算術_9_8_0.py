"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a(=13/5)尺 。
"""

"""
Suppose there is a circular log buried in a wall, and its size is unknown.
Using a measuring tool, it is pressed into the wall to a depth of 1 cun, and the length of the arc (the measuring tool's path) is 1 chi.
Question: what is the diameter of the log?

The procedure says: Take half of the arc length and square it. 
If the depth is 1 cun, treat it as 1. Add the depth to the squared value, and this is the diameter of the log.

Answer: the diameter of the log is *a*(=13/5) chi.
"""

# 鐻道長一尺
鐻道 = 1

# 深一寸
深 = Fraction(1, 10)  # 1 cun = 1/10 chi

# 半鐻道自乘
半鐻道 = 鐻道 / 2
半鐻道平方 = 半鐻道 * 半鐻道

# 如深寸而一，以深寸增之，即材徑
材徑 = 半鐻道平方 + 深

a = 材徑  # 13/5 chi
"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 0.35"""
