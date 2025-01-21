"""
今有平地聚粟下周三丈髙四尺問受粟幾何
術曰置周尺數自相乗以髙乗之三十六而一得積尺以斛法除之即粟數
答曰 a斛
"""

"""
Suppose there is a flat ground where millet is piled. The base circumference is 3 zhang, and the height is 4 chi.
Question: how much millet does it hold?

The procedure says: Take the circumference in chi, square it, and multiply it by the height.
Divide by 36 to obtain the volume in cubic chi.
Divide it by the hu-divisor to get the number of hu.

Answer: it holds *a* hu.
"""

# 下周三丈 (convert to chi: 1丈 = 10尺)
周 = 3 * 10  # in chi

# 高四尺
高 = 4  # in chi

# 置周尺數自相乘
周平方 = 周 * 周

# 以高乘之
積尺 = 周平方 * 高

# 三十六而一
積尺 = Fraction(積尺, 36)

# 斛法 (1斛 = 10立方尺)
斛法 = 10

# 以斛法除之，即粟數
a = Fraction(積尺, 斛法)
"""
Variable 'a' has wrong value. Expected: 5000/81, Actual: 10"""
