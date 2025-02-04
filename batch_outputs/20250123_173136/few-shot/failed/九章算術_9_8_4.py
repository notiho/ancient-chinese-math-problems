"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a尺 。
"""

"""
Suppose there is a cylindrical object buried in a wall, and its size is unknown.
When measured with a caliper, the depth is 1 cun, and the caliper's span is 1 chi.
Question: what is the diameter of the cylinder?

The procedure says: Take half the caliper's span and square it. 
If the depth is 1 cun, divide by 1. 
Add the depth to the result, and this is the diameter of the cylinder.

Answer: the diameter of the cylinder is *a* chi.
"""

# 鐻道長一尺
鐻道 = 1  # in chi

# 深一寸
深 = Fraction(1, 10)  # 1 cun = 1/10 chi

# 半鐻道自乘
半鐻道 = 鐻道 / 2
半鐻道平方 = 半鐻道 * 半鐻道

# 如深寸而一，以深寸增之，即材徑
材徑 = 半鐻道平方 / 深 + 深

a = 材徑  # 材徑 in chi
"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 2.6"""
