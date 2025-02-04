"""
今有平地聚粟下周三丈髙四尺問受粟幾何
術曰置周尺數自相乗以髙乗之三十六而一得積尺以斛法除之即粟數
答曰 a斛
"""

"""
Suppose there is a flat ground where millet is piled. The base circumference is 3 zhang, and the height is 4 chi.
Question: how much millet does it hold?

The procedure says: Take the number of chi in the circumference, square it, and multiply it by the height.
Divide it by 36 to get the volume in cubic chi.
Then divide it by the hu divisor to get the number of hu.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周三丈 (convert to chi: 1 zhang = 10 chi)
周 = 3 * 10

# 高四尺
高 = 4

# 置周尺數自相乘 (square the circumference in chi)
周平方 = 周 * 周

# 以高乘之 (multiply by the height)
積尺 = 周平方 * 高

# 三十六而一 (divide by 36 to get cubic chi)
積尺 = Fraction(積尺, 36)

# 斛法 (1 hu = 10 cubic chi)
斛法 = 10

# 以斛法除之，即粟數
a = Fraction(積尺, 斛法)
"""
Variable 'a' has wrong value. Expected: 5000/81, Actual: 10"""
