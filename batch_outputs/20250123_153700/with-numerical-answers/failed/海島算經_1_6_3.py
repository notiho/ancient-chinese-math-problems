"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a(=6/5)丈 。
"""

"""
Suppose one looks into a clear deep pool, where there is a white stone at the bottom. 
A carpenter's square is placed on the bank, with the vertical leg (the "upright") set to 3 chi in height. 
Looking diagonally across the water to the opposite bank, the lower leg (the "base") extends 4 chi 5 cun inward. 
Looking at the white stone, the lower leg extends 2 chi 4 cun inward. 

Another carpenter's square is placed above the first, with a vertical separation of 4 chi between them. 
From the top square, looking diagonally across the water to the opposite bank, the upper leg extends 4 chi inward. 
Looking at the white stone, the upper leg extends 2 chi 2 cun inward. 

Question: how deep is the water?

The procedure says: Subtract the upper and lower legs when looking at the water, and multiply the remainder by the upper leg when looking at the stone to obtain the upper ratio. 
Then subtract the upper and lower legs when looking at the stone, and multiply the remainder by the upper leg when looking at the water to obtain the lower ratio. 
Subtract the two ratios, and multiply the remainder by the vertical separation of the squares to obtain the dividend. 
Multiply the two differences to obtain the divisor. 
Divide the dividend by the divisor to obtain the depth of the water.

Answer: *a*(=6/5) zhang.
"""

from fractions import Fraction

# Measurements in chi and cun (1 chi = 10 cun)
句高 = 3  # Vertical leg height (chi)
矩間 = 4  # Vertical separation between the two squares (chi)

# Lower square measurements
望水下股 = 4 + Fraction(5, 10)  # 4 chi 5 cun
望石下股 = 2 + Fraction(4, 10)  # 2 chi 4 cun

# Upper square measurements
望水上股 = 4  # 4 chi
望石上股 = 2 + Fraction(2, 10)  # 2 chi 2 cun

# 置望水上下股相減，餘以乘望石上股為上率
上率 = (望水下股 - 望水上股) * 望石上股

# 又以望石上下股相減，餘以乘望水上股為下率
下率 = (望石下股 - 望石上股) * 望水上股

# 兩率相減，餘以乘矩間為實
實 = (上率 - 下率) * 矩間

# 以二差相乘為法
法 = (望水下股 - 望水上股) * (望石下股 - 望石上股)

# 實如法而一，得水深
水深 = Fraction(實, 法)

a = 水深  # 6/5 zhang
"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 12"""
