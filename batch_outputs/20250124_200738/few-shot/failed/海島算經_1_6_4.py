"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a clear deep pool, and at the bottom of the pool, there is a white stone.
A carpenter's square is placed on the bank, with the vertical leg (ju) set to a height of 3 chi.
Looking diagonally across the water to the opposite bank, the lower horizontal leg (gu) extends 4 chi 5 cun.
Looking diagonally at the white stone, the lower horizontal leg (gu) extends 2 chi 4 cun.
Another carpenter's square is placed above the first, with a vertical distance of 4 chi between them.
From the upper square, looking diagonally across the water to the opposite bank, the upper horizontal leg (gu) extends 4 chi.
Looking diagonally at the white stone, the upper horizontal leg (gu) extends 2 chi 2 cun.
Question: how deep is the water?

The procedure says: Subtract the upper and lower horizontal legs when looking at the opposite bank. Multiply the remainder by the upper horizontal leg when looking at the white stone to get the upper ratio.
Subtract the upper and lower horizontal legs when looking at the white stone. Multiply the remainder by the upper horizontal leg when looking at the opposite bank to get the lower ratio.
Subtract the two ratios. Multiply the remainder by the vertical distance between the two carpenter's squares to get the dividend.
Multiply the two differences to get the divisor.
Divide the dividend by the divisor to get the depth of the water.

Answer: *a* zhang.
"""

# Convert chi and cun to a single unit (chi)
def convert_to_chi(chi, cun):
    return chi + Fraction(cun, 10)

# Given data
句高 = 3  # Vertical leg (ju) height in chi
矩間 = 4  # Vertical distance between the two carpenter's squares in chi

# Lower square measurements
望水下股 = convert_to_chi(4, 5)  # Lower horizontal leg (gu) when looking at the opposite bank
望石下股 = convert_to_chi(2, 4)  # Lower horizontal leg (gu) when looking at the white stone

# Upper square measurements
望水上股 = convert_to_chi(4, 0)  # Upper horizontal leg (gu) when looking at the opposite bank
望石上股 = convert_to_chi(2, 2)  # Upper horizontal leg (gu) when looking at the white stone

# Procedure calculations
# Subtract the upper and lower horizontal legs when looking at the opposite bank
望水股差 = 望水上股 - 望水下股

# Multiply the remainder by the upper horizontal leg when looking at the white stone to get the upper ratio
上率 = 望水股差 * 望石上股

# Subtract the upper and lower horizontal legs when looking at the white stone
望石股差 = 望石上股 - 望石下股

# Multiply the remainder by the upper horizontal leg when looking at the opposite bank to get the lower ratio
下率 = 望石股差 * 望水上股

# Subtract the two ratios
率差 = 上率 - 下率

# Multiply the remainder by the vertical distance between the two carpenter's squares to get the dividend
實 = 率差 * 矩間

# Multiply the two differences to get the divisor
法 = 望水股差 * 望石股差

# Divide the dividend by the divisor to get the depth of the water
a = Fraction(實, 法)  # Depth of the water in chi

# Convert the result to zhang (1 zhang = 10 chi)
a = a / 10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -6/5"""
