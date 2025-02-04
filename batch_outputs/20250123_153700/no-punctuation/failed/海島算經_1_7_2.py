"""
今有登山望津津在山南偃矩山上令句高一丈二尺從句端斜望津南岸入下股二丈三尺一寸又望津北岸入前望股裏一丈八寸更登高巖北卻行二十二步上登五十一步偃矩山上更從句端斜望津南岸入上股二丈二尺問津廣幾何
術曰以句高乘下股如上股而一所得以句高減之餘為法置北行以句高乘之如上股而一所得以減上登餘以乘入股裏為實實如法而一即得津廣
答曰 a里 
"""

"""
Suppose there is a person climbing a mountain to observe a river crossing. The river lies south of the mountain.
On the mountain, a right triangle is formed with the height (the vertical leg) being 1 zhang 2 chi.
From the top of the vertical leg, the observer looks diagonally to the south bank of the river, where the diagonal leg enters the lower horizontal leg by 2 zhang 3 chi 1 cun.
The observer then looks diagonally to the north bank of the river, where the diagonal leg enters the forward horizontal leg by 1 zhang 8 cun.
The observer then climbs a higher peak to the north, walking backward 22 bu and climbing upward 51 bu.
From the top of the new vertical leg, the observer looks diagonally to the south bank of the river again, where the diagonal leg enters the upper horizontal leg by 2 zhang 2 chi.
Question: how wide is the river?

The procedure says:
1. Multiply the height of the first triangle by the lower horizontal leg (as if it were the upper horizontal leg), and divide by 1. Subtract the height of the first triangle from the result. The remainder is the divisor.
2. Place the backward walking distance (22 bu). Multiply it by the height of the first triangle (as if it were the upper horizontal leg), and divide by 1. Subtract the upward climbing distance (51 bu) from the result. Multiply the remainder by the forward horizontal leg (1 zhang 8 cun) to get the dividend.
3. Divide the dividend by the divisor to get the width of the river.

Answer: *a* li.
"""

# Convert all measurements to chi for consistency
# 1 zhang = 10 chi, 1 chi = 10 cun, 1 bu = 6 chi

# Initial data
句高 = 1 * 10 + 2  # 1丈2尺 = 12尺
下股 = 2 * 10 + 3 + Fraction(1, 10)  # 2丈3尺1寸 = 23.1尺
入股裏 = 1 * 10 + Fraction(8, 10)  # 1丈8寸 = 10.8尺
北行 = 22 * 6  # 22步 = 132尺
上登 = 51 * 6  # 51步 = 306尺
上股 = 2 * 10 + 2  # 2丈2尺 = 22尺

# Step 1: Calculate the divisor
# 以句高乘下股，如上股而一，所得以句高減之，餘為法
法 = Fraction(句高 * 下股, 上股) - 句高

# Step 2: Calculate the dividend
# 置北行，以句高乘之，如上股而一，所得以減上登，餘以乘入股裏，為實
實 = (Fraction(句高 * 北行, 上股) - 上登) * 入股裏

# Step 3: Calculate the width of the river
# 實如法而一，即得津廣
津廣 = Fraction(實, 法)

# Convert the result from chi to li (1 li = 1800 chi)
a = Fraction(津廣, 1800)  # Convert chi to li
"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -117/50"""
