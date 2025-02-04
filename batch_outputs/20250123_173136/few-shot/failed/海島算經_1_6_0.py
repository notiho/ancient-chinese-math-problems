"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a丈 。
"""

"""
Suppose one looks into a clear deep pool, and there is a white stone at the bottom of the pool.
A carpenter's square is placed on the bank, with the vertical leg (ju) set to a height of 3 chi.
Looking diagonally from the top of the vertical leg to the water's edge, the lower horizontal leg (gu) extends 4 chi 5 cun.
Looking diagonally to the white stone, the lower horizontal leg extends 2 chi 4 cun.
Another carpenter's square is placed above the first, with a vertical distance of 4 chi between them.
From the top of the upper vertical leg, looking diagonally to the water's edge, the upper horizontal leg extends 4 chi.
Looking diagonally to the white stone, the upper horizontal leg extends 2 chi 2 cun.

Question: how deep is the water?

The procedure says:
Take the difference between the upper and lower horizontal legs when looking at the water's edge, and multiply the result by the upper horizontal leg when looking at the white stone. This gives the upper ratio.
Then, take the difference between the upper and lower horizontal legs when looking at the white stone, and multiply the result by the upper horizontal leg when looking at the water's edge. This gives the lower ratio.
Subtract the two ratios, and multiply the result by the distance between the two carpenter's squares. This gives the dividend.
Multiply the two differences (from the horizontal legs) to get the divisor.
Divide the dividend by the divisor to get the water depth.

Answer: the water depth is *a* zhang.
"""

# Define units
chi_to_zhang = 10  # 1 zhang = 10 chi
cun_to_chi = 10    # 1 chi = 10 cun

# Known values
句高 = 3  # Vertical leg height in chi
矩間 = 4  # Distance between the two carpenter's squares in chi

# Lower horizontal legs
望水下股 = 4 + Fraction(5, cun_to_chi)  # 4 chi 5 cun
望石下股 = 2 + Fraction(4, cun_to_chi)  # 2 chi 4 cun

# Upper horizontal legs
望水上股 = 4  # 4 chi
望石上股 = 2 + Fraction(2, cun_to_chi)  # 2 chi 2 cun

# Step 1: Calculate the upper ratio
上下股望水差 = 望水上股 - 望水下股
上率 = 上下股望水差 * 望石上股

# Step 2: Calculate the lower ratio
上下股望石差 = 望石上股 - 望石下股
下率 = 上下股望石差 * 望水上股

# Step 3: Calculate the dividend
兩率差 = 上率 - 下率
實 = 兩率差 * 矩間

# Step 4: Calculate the divisor
法 = 上下股望水差 * 上下股望石差

# Step 5: Calculate the water depth
水深 = Fraction(實, 法)

# Convert to zhang
a = 水深 / chi_to_zhang
"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -6/5"""
