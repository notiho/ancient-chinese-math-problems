"""
今有方窖長一丈三尺廣六尺深一丈問受粟幾何
術曰置長尺數以廣尺數乗之又以深乗之得積尺以斛法除之即粟數
答曰 a斛
"""

"""
Suppose there is a square pit with a length of 1 zhang and 3 chi, a width of 6 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

The procedure says: Place the number of chi in the length, multiply it by the number of chi in the width, and then multiply it by the depth.
This gives the accumulated chi.
Divide it by the hu-divisor to obtain the number of hu of millet.

Answer: *a* hu.
"""

# 長一丈三尺
長 = 1 * 10 + 3  # Convert zhang to chi (1 zhang = 10 chi)

# 廣六尺
廣 = 6

# 深一丈
深 = 1 * 10  # Convert zhang to chi

# 置長尺數以廣尺數乗之
積尺 = 長 * 廣

# 又以深乗之
積尺 = 積尺 * 深

# 斛法 (1斛 = 1000立方尺)
斛法 = 1000

# 以斛法除之，即粟數
a = Fraction(積尺,斛法)
"""
Variable 'a' has wrong value. Expected: 13000/27, Actual: 39/50"""
