"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a(=6/5)丈 。
"""

"""
Suppose one looks into a clear deep pool, where there is a white stone at the bottom.
A carpenter's square is placed on the bank, with the vertical leg (the "ju") set to a height of 3 chi.
Looking diagonally toward the water's edge, the lower horizontal leg (the "gu") extends inward by 4 chi 5 cun.
Looking at the white stone, the lower horizontal leg extends inward by 2 chi 4 cun.
Another carpenter's square is placed above the first, with a vertical separation of 4 chi between them.
From the upper square's vertical leg, looking diagonally toward the water's edge, the upper horizontal leg extends inward by 4 chi.
Looking at the white stone, the upper horizontal leg extends inward by 2 chi 2 cun.
Question: how deep is the water?

The procedure says: Take the difference between the upper and lower horizontal legs when looking at the water's edge.
Multiply the remainder by the upper horizontal leg when looking at the white stone to obtain the upper ratio.
Then take the difference between the upper and lower horizontal legs when looking at the white stone.
Multiply the remainder by the upper horizontal leg when looking at the water's edge to obtain the lower ratio.
Subtract the two ratios, and multiply the remainder by the vertical separation between the two carpenter's squares to obtain the dividend.
Multiply the two differences to obtain the divisor.
Divide the dividend by the divisor to obtain the water depth.

Answer: *a*(=6/5) zhang.
"""

# Constants for unit conversion
chi_to_cun = 10  # 1 chi = 10 cun
zhang_to_chi = 10  # 1 zhang = 10 chi

# Given values
句高 = 3  # chi
望水下股 = 4 + Fraction(5, chi_to_cun)  # 4 chi 5 cun
望石下股 = 2 + Fraction(4, chi_to_cun)  # 2 chi 4 cun
矩間 = 4  # chi
望水上股 = 4  # chi
望石上股 = 2 + Fraction(2, chi_to_cun)  # 2 chi 2 cun

# Procedure
# 置望水上下股相減
望水股差 = 望水上股 - 望水下股

# 餘以乘望石上股為上率
上率 = 望水股差 * 望石上股

# 又以望石上下股相減
望石股差 = 望石上股 - 望石下股

# 餘以乘望水上股為下率
下率 = 望石股差 * 望水上股

# 兩率相減
率差 = 上率 - 下率

# 餘以乘矩間為實
實 = 率差 * 矩間

# 以二差相乘為法
法 = 望水股差 * 望石股差

# 實如法而一，得水深
水深 = Fraction(實, 法)  # in chi

# Convert to zhang
a = 水深 / zhang_to_chi  # 6/5 zhang
"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -6/5"""
