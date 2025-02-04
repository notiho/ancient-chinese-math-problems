"""
今有圓材埋在壁中不知大小以鐻鐻之深一寸鐻道長一尺問徑幾何
術曰半鐻道自乘如深寸而一以深寸增之即材徑
荅曰材徑 a尺 
"""

"""
Suppose there is a circular log embedded in a wall, and its size is unknown.
Using a measuring tool, the depth of the indentation is 1 cun, and the length of the measuring tool's arc is 1 chi.
Question: what is the diameter of the log?

The procedure says: Take half of the arc length, and square it. 
If the depth is 1 cun, add it to the square of the half arc length.
The result is the diameter of the log.

Answer: the diameter of the log is *a* chi.
"""

# 鐻道長一尺
鐻道長 = 1  # in chi

# 鐻鐻之深一寸
深 = Fraction(1, 10)  # 1 cun = 1/10 chi

# 半鐻道
半鐻道 = Fraction(鐻道長, 2)

# 半鐻道自乘
半鐻道平方 = 半鐻道 * 半鐻道

# 如深寸而一，以深寸增之
材徑 = 半鐻道平方 + 深

a = 材徑
"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 7/20"""
