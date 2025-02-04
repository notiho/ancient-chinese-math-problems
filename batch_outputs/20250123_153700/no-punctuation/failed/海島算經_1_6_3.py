"""
今有望清淵淵下有白石偃矩岸上令句高三尺斜望水岸入下股四尺五寸望白石入下股二尺四寸又設重矩于上其間相去四尺更從句端斜望水岸入上股四尺以望白石入上股二尺二寸問水深幾何
術曰置望水上下股相減餘以乘望石上股為上率又以望石上下股相減餘以乘望水上股為下率兩率相減餘以乘矩間為實以二差相乘為法實如法而一得水深
答曰 a丈 
"""

"""
Suppose there is a clear deep pool, and at the bottom of the pool lies a white stone. 
A right-angled instrument is placed on the bank, with the vertical leg (height) being 3 chi. 
Looking diagonally from the top of the vertical leg, the diagonal line enters the lower horizontal leg by 4 chi 5 cun when aimed at the water's edge, and by 2 chi 4 cun when aimed at the white stone.
Another right-angled instrument is set up above the first one, with a vertical distance of 4 chi between the two instruments. 
From the top of the second vertical leg, the diagonal line enters the upper horizontal leg by 4 chi when aimed at the water's edge, and by 2 chi 2 cun when aimed at the white stone.
Question: what is the depth of the water?

The procedure says:
1. Place the differences between the upper and lower horizontal legs when aiming at the water's edge, and multiply the remainder by the upper horizontal leg when aiming at the white stone. This gives the numerator for the upper rate.
2. Place the differences between the upper and lower horizontal legs when aiming at the white stone, and multiply the remainder by the upper horizontal leg when aiming at the water's edge. This gives the numerator for the lower rate.
3. Subtract the two rates, and multiply the remainder by the vertical distance between the two instruments. This gives the dividend.
4. Multiply the two differences (from step 1 and step 2) together. This gives the divisor.
5. Divide the dividend by the divisor to obtain the depth of the water.

Answer: the depth of the water is *a* zhang.
"""

# Convert all measurements to chi (1 chi = 10 cun)
句高 = 3  # Vertical leg (height) in chi
矩間 = 4  # Vertical distance between the two instruments in chi

# Lower instrument measurements
望水下股 = 4 + Fraction(5, 10)  # Horizontal leg when aiming at the water's edge
望石下股 = 2 + Fraction(4, 10)  # Horizontal leg when aiming at the white stone

# Upper instrument measurements
望水上股 = 4  # Horizontal leg when aiming at the water's edge
望石上股 = 2 + Fraction(2, 10)  # Horizontal leg when aiming at the white stone

# Step 1: Calculate the numerator for the upper rate
上下股差_望水 = 望水上股 - 望水下股  # Difference for water's edge
上率 = 上下股差_望水 * 望石上股  # Multiply by upper horizontal leg for white stone

# Step 2: Calculate the numerator for the lower rate
上下股差_望石 = 望石上股 - 望石下股  # Difference for white stone
下率 = 上下股差_望石 * 望水上股  # Multiply by upper horizontal leg for water's edge

# Step 3: Calculate the dividend
兩率差 = 上率 - 下率  # Subtract the two rates
實 = 兩率差 * 矩間  # Multiply by the vertical distance between instruments

# Step 4: Calculate the divisor
法 = 上下股差_望水 * 上下股差_望石  # Multiply the two differences

# Step 5: Calculate the depth of the water
a = Fraction(實, 法)  # Depth of the water in chi

# Convert to zhang (1 zhang = 10 chi)
a = a / 10  # Depth in zhang
"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -6/5"""
