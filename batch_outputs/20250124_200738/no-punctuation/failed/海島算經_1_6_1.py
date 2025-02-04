"""
今有望清淵淵下有白石偃矩岸上令句高三尺斜望水岸入下股四尺五寸望白石入下股二尺四寸又設重矩于上其間相去四尺更從句端斜望水岸入上股四尺以望白石入上股二尺二寸問水深幾何
術曰置望水上下股相減餘以乘望石上股為上率又以望石上下股相減餘以乘望水上股為下率兩率相減餘以乘矩間為實以二差相乘為法實如法而一得水深
答曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a clear deep pool, with white stones at the bottom. A right-angled instrument is placed on the bank.
Let the vertical leg (height) be 3 chi. The slanted sightline to the water's edge intersects the lower horizontal leg at 4 chi 5 cun.
The sightline to the white stone intersects the lower horizontal leg at 2 chi 4 cun.
Another right-angled instrument is placed above, with a vertical distance of 4 chi between the two instruments.
From the top instrument, the slanted sightline to the water's edge intersects the upper horizontal leg at 4 chi.
The sightline to the white stone intersects the upper horizontal leg at 2 chi 2 cun.
Question: How deep is the water?

The procedure says:
1. Subtract the upper and lower horizontal legs for the water's edge. Multiply the result by the upper horizontal leg for the white stone. This gives the upper ratio.
2. Subtract the upper and lower horizontal legs for the white stone. Multiply the result by the upper horizontal leg for the water's edge. This gives the lower ratio.
3. Subtract the two ratios. Multiply the result by the vertical distance between the two instruments. This gives the dividend.
4. Multiply the two differences (from steps 1 and 2). This gives the divisor.
5. Divide the dividend by the divisor to obtain the water's depth.

Answer: The water's depth is *a* zhang.
"""

# Define measurements in chi and cun
# Convert cun to chi (1 chi = 10 cun)
def to_chi(chi, cun=0):
    return chi + Fraction(cun, 10)

# Given data
句高 = to_chi(3)  # Vertical leg (height)
矩間 = to_chi(4)  # Vertical distance between instruments

# Lower instrument measurements
望水下股 = to_chi(4, 5)  # Horizontal leg for water's edge (lower)
望石下股 = to_chi(2, 4)  # Horizontal leg for white stone (lower)

# Upper instrument measurements
望水上股 = to_chi(4)  # Horizontal leg for water's edge (upper)
望石上股 = to_chi(2, 2)  # Horizontal leg for white stone (upper)

# Step 1: Calculate the upper ratio
望水上下股差 = 望水上股 - 望水下股
上率 = 望水上下股差 * 望石上股

# Step 2: Calculate the lower ratio
望石上下股差 = 望石上股 - 望石下股
下率 = 望石上下股差 * 望水上股

# Step 3: Subtract the two ratios and multiply by 矩間
兩率差 = 上率 - 下率
實 = 兩率差 * 矩間

# Step 4: Multiply the two differences
法 = 望水上下股差 * 望石上下股差

# Step 5: Divide 实 by 法 to get the water depth
水深 = Fraction(實, 法)

# Convert to zhang (1 zhang = 10 chi)
a = 水深 / 10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -6/5"""
