"""
今有望清淵淵下有白石偃矩岸上令句高三尺斜望水岸入下股四尺五寸望白石入下股二尺四寸又設重矩于上其間相去四尺更從句端斜望水岸入上股四尺以望白石入上股二尺二寸問水深幾何
術曰置望水上下股相減餘以乘望石上股為上率又以望石上下股相減餘以乘望水上股為下率兩率相減餘以乘矩間為實以二差相乘為法實如法而一得水深
答曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a clear deep pool, and at the bottom of the pool lies a white stone. 
A right triangle is set up on the bank, with the vertical leg (height) being 3 chi. 
Looking diagonally from the top of the triangle, the horizontal leg (base) extends into the water by 4 chi 5 cun. 
Looking diagonally at the white stone, the horizontal leg extends into the water by 2 chi 4 cun. 

Another right triangle is set up above the first, with the distance between the two triangles being 4 chi. 
From the top of the second triangle, looking diagonally at the water's edge, the horizontal leg extends into the water by 4 chi. 
Looking diagonally at the white stone, the horizontal leg extends into the water by 2 chi 2 cun. 

Question: How deep is the water?

The procedure says: Subtract the upper and lower horizontal legs when looking at the water, and multiply the remainder by the upper horizontal leg when looking at the stone. This gives the upper rate. 
Then subtract the upper and lower horizontal legs when looking at the stone, and multiply the remainder by the upper horizontal leg when looking at the water. This gives the lower rate. 
Subtract the two rates, and multiply the remainder by the distance between the two triangles. This gives the dividend. 
Multiply the two differences (from the subtractions) together. This gives the divisor. 
Divide the dividend by the divisor to obtain the water depth.

Answer: The water depth is *a* zhang.
"""

# Convert all measurements to chi (1 chi = 10 cun)
句高 = 3  # Vertical leg (height) in chi
望水下股 = 4 + Fraction(5, 10)  # Lower horizontal leg when looking at the water
望石下股 = 2 + Fraction(4, 10)  # Lower horizontal leg when looking at the stone
矩間 = 4  # Distance between the two triangles
望水上股 = 4  # Upper horizontal leg when looking at the water
望石上股 = 2 + Fraction(2, 10)  # Upper horizontal leg when looking at the stone

# 置望水上下股相減
望水股差 = 望水上股 - 望水下股

# 餘以乘望石上股，為上率
上率 = 望水股差 * 望石上股

# 又以望石上下股相減
望石股差 = 望石上股 - 望石下股

# 餘以乘望水上股，為下率
下率 = 望石股差 * 望水上股

# 兩率相減餘
率差 = 上率 - 下率

# 餘以乘矩間，為實
實 = 率差 * 矩間

# 以二差相乘，為法
法 = 望水股差 * 望石股差

# 實如法而一，得水深
水深 = Fraction(實, 法)

# Convert the result to zhang (1 zhang = 10 chi)
a = 水深 / 10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -6/5"""
