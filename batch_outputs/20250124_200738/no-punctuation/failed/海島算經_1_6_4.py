"""
今有望清淵淵下有白石偃矩岸上令句高三尺斜望水岸入下股四尺五寸望白石入下股二尺四寸又設重矩于上其間相去四尺更從句端斜望水岸入上股四尺以望白石入上股二尺二寸問水深幾何
術曰置望水上下股相減餘以乘望石上股為上率又以望石上下股相減餘以乘望水上股為下率兩率相減餘以乘矩間為實以二差相乘為法實如法而一得水深
答曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a clear deep pool, and at the bottom of the pool lies a white stone. 
A right-angled instrument is placed on the bank, with the vertical leg (height) being 3 chi. 
Looking diagonally from the top of the vertical leg to the water's edge, the lower horizontal leg (lower 股) is 4 chi 5 cun. 
Looking diagonally to the white stone, the lower horizontal leg (lower 股) is 2 chi 4 cun. 
Another right-angled instrument is placed above the first, with a vertical separation of 4 chi. 
From the top of the upper vertical leg, looking diagonally to the water's edge, the upper horizontal leg (upper 股) is 4 chi. 
Looking diagonally to the white stone, the upper horizontal leg (upper 股) is 2 chi 2 cun. 
Question: how deep is the water?

The procedure says: Place the difference between the horizontal legs for the water's edge (upper 股 - lower 股), and multiply the remainder by the horizontal leg for the white stone (upper 股) to get the upper rate. 
Then, take the difference between the horizontal legs for the white stone (upper 股 - lower 股), and multiply the remainder by the horizontal leg for the water's edge (upper 股) to get the lower rate. 
Subtract the two rates, and multiply the remainder by the vertical separation between the instruments to get the dividend. 
Multiply the two differences (for the water's edge and the white stone) to get the divisor. 
Divide the dividend by the divisor to get the water depth.

Answer: *a* zhang.
"""

# Define measurements in chi and cun (1 chi = 10 cun)
句高 = 3  # Vertical leg (height) in chi
矩間 = 4  # Vertical separation between instruments in chi

# Lower instrument measurements
望水下股 = 4 + Fraction(5, 10)  # Lower horizontal leg to water's edge (4 chi 5 cun)
望石下股 = 2 + Fraction(4, 10)  # Lower horizontal leg to white stone (2 chi 4 cun)

# Upper instrument measurements
望水上股 = 4  # Upper horizontal leg to water's edge (4 chi)
望石上股 = 2 + Fraction(2, 10)  # Upper horizontal leg to white stone (2 chi 2 cun)

# Step 1: Calculate the upper rate
望水股差 = 望水上股 - 望水下股  # Difference for water's edge
上率 = 望水股差 * 望石上股  # Multiply by upper horizontal leg for white stone

# Step 2: Calculate the lower rate
望石股差 = 望石上股 - 望石下股  # Difference for white stone
下率 = 望石股差 * 望水上股  # Multiply by upper horizontal leg for water's edge

# Step 3: Calculate the dividend
率差 = 上率 - 下率  # Difference between the two rates
實 = 率差 * 矩間  # Multiply by vertical separation

# Step 4: Calculate the divisor
法 = 望水股差 * 望石股差  # Multiply the two differences

# Step 5: Calculate the water depth
水深 = Fraction(實, 法)

# Convert to zhang (1 zhang = 10 chi)
a = 水深 / 10  # Water depth in zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -6/5"""
