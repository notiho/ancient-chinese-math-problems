"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a clear deep pool, and at the bottom of the pool, there is a white stone.
A carpenter's square is placed on the bank, with the vertical leg (ju) set to 3 chi high.
Looking diagonally across the water to the opposite bank, the lower horizontal leg (gu) extends 4 chi 5 cun.
Looking at the white stone, the lower horizontal leg extends 2 chi 4 cun.
Another carpenter's square is placed above the first, with a vertical distance of 4 chi between them.
From the top square, looking diagonally across the water to the opposite bank, the upper horizontal leg extends 4 chi.
Looking at the white stone, the upper horizontal leg extends 2 chi 2 cun.
Question: how deep is the water?

The procedure says: Subtract the upper and lower horizontal legs when looking at the water, and multiply the remainder by the upper horizontal leg when looking at the stone to get the numerator of the upper ratio.
Then subtract the upper and lower horizontal legs when looking at the stone, and multiply the remainder by the upper horizontal leg when looking at the water to get the numerator of the lower ratio.
Subtract the two ratios, and multiply the remainder by the vertical distance between the two carpenter's squares to get the dividend.
Multiply the two differences to get the divisor.
Divide the dividend by the divisor to get the depth of the water.

Answer: *a* zhang.
"""

# Convert all measurements to chi (1 chi = 10 cun)

# Lower carpenter's square
句高 = 3  # Vertical leg (ju)
望水下股 = 4 + Fraction(5, 10)  # Lower horizontal leg when looking at the water
望石下股 = 2 + Fraction(4, 10)  # Lower horizontal leg when looking at the stone

# Upper carpenter's square
矩間 = 4  # Vertical distance between the two carpenter's squares
望水上股 = 4  # Upper horizontal leg when looking at the water
望石上股 = 2 + Fraction(2, 10)  # Upper horizontal leg when looking at the stone

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
水深 = Fraction(實, 法)

# Convert chi to zhang (1 zhang = 10 chi)
a = 水深 / 10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -6/5"""
