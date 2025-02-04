"""
今有平地聚粟，下周三丈六尺，高四尺五寸。問：粟幾何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground. The base circumference is 3 zhang 6 chi, and the height is 4 chi 5 cun.
Question: how much millet is there?

Answer: *a* hu.
"""

# 下周三丈六尺 (base circumference)
周 = 3 * 10 + 6  # Convert zhang to chi (1 zhang = 10 chi)

# 高四尺五寸 (height)
高 = 4 + Fraction(5, 10)  # Convert cun to chi (1 chi = 10 cun)

# Calculate the radius of the base (周 = 2 * pi * r, so r = 周 / (2 * pi))
半徑 = Fraction(周, 2 * 3)  # Use pi ≈ 3 as per ancient Chinese approximation

# Volume of the cone (V = 1/3 * base area * height, base area = pi * r^2)
體積 = Fraction(1, 3) * 3 * 半徑**2 * 高  # Use pi ≈ 3

# Convert volume from cubic chi to hu (1 hu = 10 cubic chi)
a = Fraction(體積, 10)  # Convert to hu

a  # Result in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 100, Actual: 81/5"""
