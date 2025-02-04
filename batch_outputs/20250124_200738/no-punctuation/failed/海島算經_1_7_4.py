"""
今有登山望津津在山南偃矩山上令句高一丈二尺從句端斜望津南岸入下股二丈三尺一寸又望津北岸入前望股裏一丈八寸更登高巖北卻行二十二步上登五十一步偃矩山上更從句端斜望津南岸入上股二丈二尺問津廣幾何
術曰以句高乘下股如上股而一所得以句高減之餘為法置北行以句高乘之如上股而一所得以減上登餘以乘入股裏為實實如法而一即得津廣
答曰 a里 
"""

#----- content starts here -----
"""
Suppose someone climbs a mountain to observe a river crossing. The river crossing is south of the mountain.
On the mountain, a right triangle is formed with the height (vertical leg) being 1 zhang 2 chi (12 chi).
From the top of the vertical leg, the diagonal (hypotenuse) is extended to the south bank of the river, entering the lower horizontal leg by 2 zhang 3 chi 1 cun (231 cun).
The diagonal is also extended to the north bank of the river, entering the forward horizontal leg by 1 zhang 8 cun (108 cun).
The observer then climbs a higher cliff to the north, walking backward 22 bu and climbing upward 51 bu.
From this new height, the diagonal is extended again to the south bank of the river, entering the upper horizontal leg by 2 zhang 2 chi (220 cun).
Question: What is the width of the river crossing?

The procedure says:
1. Multiply the height of the vertical leg by the lower horizontal leg. Divide by the upper horizontal leg. Subtract the height of the vertical leg from the result. The remainder is the divisor.
2. Place the backward walk (northward movement). Multiply it by the height of the vertical leg. Divide by the upper horizontal leg. Subtract the upward climb. The remainder is multiplied by the forward horizontal leg to form the dividend.
3. Divide the dividend by the divisor to obtain the width of the river crossing.

Answer: *a* li.
"""

# Step 1: Define known values
句高 = 12  # 高度 (12 尺)
下股 = 231  # 下股 (231 寸)
上股 = 220  # 上股 (220 寸)
股裏 = 108  # 股裏 (108 寸)
北行 = 22  # 北行 (22 步)
上登 = 51  # 上登 (51 步)

# Step 2: Calculate the divisor
# 以句高乘下股
下股乘積 = 句高 * 下股

# 如上股而一
下股商 = Fraction(下股乘積, 上股)

# 所得以句高減之，餘為法
法 = 下股商 - 句高

# Step 3: Calculate the dividend
# 置北行，以句高乘之
北行乘積 = 北行 * 句高

# 如上股而一
北行商 = Fraction(北行乘積, 上股)

# 所得以減上登
北行減上登 = 北行商 - 上登

# 餘以乘入股裏，為實
實 = 北行減上登 * 股裏

# Step 4: Calculate the river width
# 實如法而一，即得津廣
津廣 = Fraction(實, 法)

# Convert to li (1 li = 1800 cun)
a = Fraction(津廣, 1800)  # Convert from cun to li#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -249/50"""
