"""
今有委粟平地，下周一十二丈，高二丈。問︰積及為粟幾何？
荅曰：積 a尺 。為粟 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground. The base circumference is 12 zhang, and the height is 2 zhang.
Question: what is the volume of the pile, and how much millet does it contain?

Answer: the volume is *a* cubic chi, and it contains *b* hu of millet.
"""

# 下周一十二丈 (base circumference is 12 zhang)
周 = 12 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高二丈 (height is 2 zhang)
高 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# Calculate the radius of the base (周 = 2 * pi * r, approximate pi as 3)
半徑 = 周 / (2 * 3)

# Volume of a cone: V = (1/3) * pi * r^2 * h, approximate pi as 3
積 = Fraction(1, 3) * 3 * 半徑**2 * 高

# Convert volume to hu (1 cubic zhang = 100 hu, and 1 zhang^3 = 1000 chi^3)
為粟 = 積 / 1000 * 100

# Final results
a = 積  # Volume in cubic chi
b = 為粟  # Amount of millet in hu#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 80000/27, Actual: 800.0"""
