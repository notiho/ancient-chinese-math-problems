"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a(=6/5)丈 。
"""

"""
Suppose one looks into a clear deep pool, where there is a white stone at the bottom. 
A carpenter's square is placed on the bank, with the vertical leg (the "upright") being 3 chi tall. 
Looking diagonally from the top of the upright to the water's edge, the lower horizontal leg (the "base") extends inward by 4 chi 5 cun. 
Looking diagonally to the white stone, the lower horizontal leg extends inward by 2 chi 4 cun. 

Another carpenter's square is placed above the first, with a vertical separation of 4 chi between the two squares. 
From the top of the upper square's upright, looking diagonally to the water's edge, the upper horizontal leg extends inward by 4 chi. 
Looking diagonally to the white stone, the upper horizontal leg extends inward by 2 chi 2 cun. 

Question: how deep is the water?

The procedure says: Subtract the upper and lower horizontal legs when looking at the water's edge, and multiply the remainder by the upper horizontal leg when looking at the white stone. This gives the numerator of the upper ratio. 
Then subtract the upper and lower horizontal legs when looking at the white stone, and multiply the remainder by the upper horizontal leg when looking at the water's edge. This gives the numerator of the lower ratio. 
Subtract the two ratios, and multiply the remainder by the vertical separation between the two squares to get the dividend. 
Multiply the two differences (from the subtractions) to get the divisor. 
Divide the dividend by the divisor to obtain the water depth.

Answer: *a*(=6/5) zhang.
"""

# Convert all measurements to chi (1 chi = 10 cun)
句高 = 3  # Vertical leg (upright) height in chi
矩間 = 4  # Vertical separation between the two squares in chi

# Lower square measurements
望水下股 = 4 + Fraction(5, 10)  # 4 chi 5 cun
望石下股 = 2 + Fraction(4, 10)  # 2 chi 4 cun

# Upper square measurements
望水上股 = 4  # 4 chi
望石上股 = 2 + Fraction(2, 10)  # 2 chi 2 cun

# Step 1: 置望水上下股相減，餘以乘望石上股為上率
望水差 = 望水下股 - 望水上股
上率 = 望水差 * 望石上股

# Step 2: 又以望石上下股相減，餘以乘望水上股為下率
望石差 = 望石下股 - 望石上股
下率 = 望石差 * 望水上股

# Step 3: 兩率相減，餘以乘矩間為實
實 = (上率 - 下率) * 矩間

# Step 4: 以二差相乘為法
法 = 望水差 * 望石差

# Step 5: 實如法而一，得水深
a = Fraction(實, 法)  # 6/5 zhang
"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 12"""
