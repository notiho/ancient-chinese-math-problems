"""
今有方錐下方二丈七尺，高二丈九尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square pyramid with a base side length of 2 zhang 7 chi and a height of 2 zhang 9 chi.
Question: what is the volume of the pyramid?

Answer: the volume is *a* cubic chi.
"""

# 下方二丈七尺 (convert to chi)
base_side = 2 * 10 + 7  # 1 zhang = 10 chi

# 高二丈九尺 (convert to chi)
height = 2 * 10 + 9  # 1 zhang = 10 chi

# Formula for the volume of a square pyramid: V = (1/3) * base_area * height
# Base area = side^2
base_area = base_side * base_side

# Volume
a = Fraction(1, 3) * base_area * height

# Result
a#----- content ends here -----

"""
"""
