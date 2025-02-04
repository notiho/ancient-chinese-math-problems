"""
今有望清淵淵下有白石偃矩岸上令句高三尺斜望水岸入下股四尺五寸望白石入下股二尺四寸又設重矩于上其間相去四尺更從句端斜望水岸入上股四尺以望白石入上股二尺二寸問水深幾何
術曰置望水上下股相減餘以乘望石上股為上率又以望石上下股相減餘以乘望水上股為下率兩率相減餘以乘矩間為實以二差相乘為法實如法而一得水深
答曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a clear deep pool, and at the bottom of the pool lies a white stone. 
A right-angled instrument is placed on the bank, with the vertical leg (height) being 3 chi. 
Looking diagonally from the top of the instrument, the diagonal line intersects the water's surface at 4 chi 5 cun along the horizontal leg.
Looking further diagonally, the diagonal line intersects the white stone at 2 chi 4 cun along the horizontal leg.

Another identical instrument is placed above the first, with a vertical distance of 4 chi between them. 
From the top of the second instrument, the diagonal line intersects the water's surface at 4 chi along the horizontal leg, 
and the diagonal line intersects the white stone at 2 chi 2 cun along the horizontal leg.

Question: How deep is the water?

The procedure says:
1. Place the upper and lower horizontal distances to the water's surface and subtract them. Multiply the remainder by the upper horizontal distance to the white stone to obtain the numerator for the upper rate.
2. Subtract the upper and lower horizontal distances to the white stone. Multiply the remainder by the upper horizontal distance to the water's surface to obtain the numerator for the lower rate.
3. Subtract the two rates. Multiply the remainder by the vertical distance between the two instruments to obtain the dividend.
4. Multiply the two differences (from steps 1 and 2) to obtain the divisor.
5. Divide the dividend by the divisor to obtain the water depth.

Answer: The water depth is *a* zhang.
"""

# Define measurements in chi and cun
望水下股 = 4 + Fraction(5, 10)  # 4 chi 5 cun
望石下股 = 2 + Fraction(4, 10)  # 2 chi 4 cun
望水上股 = 4  # 4 chi
望石上股 = 2 + Fraction(2, 10)  # 2 chi 2 cun
矩間 = 4  # Vertical distance between instruments (4 chi)

# Step 1: Calculate the numerator for the upper rate
望水上下股差 = 望水下股 - 望水上股
上率 = 望水上下股差 * 望石上股

# Step 2: Calculate the numerator for the lower rate
望石上下股差 = 望石下股 - 望石上股
下率 = 望石上下股差 * 望水上股

# Step 3: Subtract the two rates and multiply by the vertical distance
兩率差 = 上率 - 下率
實 = 兩率差 * 矩間

# Step 4: Multiply the two differences to obtain the divisor
法 = 望水上下股差 * 望石上下股差

# Step 5: Divide the dividend by the divisor to obtain the water depth
a = Fraction(實, 法)  # Water depth in chi

# Convert chi to zhang (1 zhang = 10 chi)
a = a / 10  # Water depth in zhang#----- content ends here -----

"""
"""
