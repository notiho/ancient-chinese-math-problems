"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a(=6/5)丈 。
"""

"""
Suppose one looks into a clear deep pool, where there is a white stone at the bottom. 
A carpenter's square is placed on the bank, with the vertical leg (the "upright") being 3 chi tall. 
Looking diagonally from the top of the upright to the water's edge, the lower horizontal leg (the "base") extends 4 chi 5 cun inward. 
Looking diagonally to the white stone, the lower base extends 2 chi 4 cun inward. 

Another carpenter's square is placed above the first, with a vertical distance of 4 chi between them. 
From the top of the upper upright, looking diagonally to the water's edge, the upper base extends 4 chi inward. 
Looking diagonally to the white stone, the upper base extends 2 chi 2 cun inward. 

Question: how deep is the water?

The procedure says: Subtract the upper and lower bases for the water's edge, and multiply the remainder by the upper base for the white stone, obtaining the upper rate. 
Then subtract the upper and lower bases for the white stone, and multiply the remainder by the upper base for the water's edge, obtaining the lower rate. 
Subtract the two rates, and multiply the remainder by the vertical distance between the two carpenter's squares, obtaining the dividend. 
Multiply the two differences (from the subtractions) together, obtaining the divisor. 
Divide the dividend by the divisor to obtain the water's depth.

Answer: *a*(=6/5) zhang.
"""

# Constants for unit conversion
CUN_TO_CHI = Fraction(1, 10)  # 1 cun = 1/10 chi

# Given measurements
句高 = 3  # chi
矩間 = 4  # chi

望水下股 = 4 + 5 * CUN_TO_CHI  # 4 chi 5 cun
望石下股 = 2 + 4 * CUN_TO_CHI  # 2 chi 4 cun
望水上股 = 4  # 4 chi
望石上股 = 2 + 2 * CUN_TO_CHI  # 2 chi 2 cun

# Step 1: Subtract the upper and lower bases for the water's edge
望水股差 = 望水下股 - 望水上股

# Step 2: Multiply the remainder by the upper base for the white stone to get the upper rate
上率 = 望水股差 * 望石上股

# Step 3: Subtract the upper and lower bases for the white stone
望石股差 = 望石下股 - 望石上股

# Step 4: Multiply the remainder by the upper base for the water's edge to get the lower rate
下率 = 望石股差 * 望水上股

# Step 5: Subtract the two rates
率差 = 上率 - 下率

# Step 6: Multiply the remainder by the vertical distance between the two carpenter's squares to get the dividend
實 = 率差 * 矩間

# Step 7: Multiply the two differences together to get the divisor
法 = 望水股差 * 望石股差

# Step 8: Divide the dividend by the divisor to get the water's depth
a = Fraction(實, 法)  # 6/5 zhang
"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 12"""
