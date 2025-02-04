"""
今有登山望津津在山南偃矩山上令句高一丈二尺從句端斜望津南岸入下股二丈三尺一寸又望津北岸入前望股裏一丈八寸更登高巖北卻行二十二步上登五十一步偃矩山上更從句端斜望津南岸入上股二丈二尺問津廣幾何
術曰以句高乘下股如上股而一所得以句高減之餘為法置北行以句高乘之如上股而一所得以減上登餘以乘入股裏為實實如法而一即得津廣
答曰 a里 
"""

"""
Suppose one climbs a mountain to observe a river crossing. The river lies to the south of the mountain.
On the mountain, a right triangle is formed with the height (vertical leg) being 1 zhang 2 chi, and the hypotenuse is used to observe the south bank of the river.
The hypotenuse enters the lower horizontal leg by 2 zhang 3 chi 1 cun.
Then, observing the north bank of the river, the hypotenuse enters the front horizontal leg by 1 zhang 8 cun.
Next, one climbs a higher peak to the north, retreating 22 bu and ascending 51 bu.
From this higher peak, observing the south bank of the river again, the hypotenuse enters the upper horizontal leg by 2 zhang 2 chi.
Question: What is the width of the river?

The procedure says:
1. Multiply the height of the vertical leg by the lower horizontal leg, treating it as the upper horizontal leg, and divide by 1. Subtract the height of the vertical leg from the result to obtain the divisor.
2. Place the northward retreat (22 bu). Multiply it by the height of the vertical leg, treating it as the upper horizontal leg, and divide by 1. Subtract the upward climb (51 bu) from the result. Multiply the remainder by the entry into the front horizontal leg to obtain the dividend.
3. Divide the dividend by the divisor to obtain the width of the river.

Answer: The width of the river is *a* li.
"""

# Convert units to chi for consistency
# 1 zhang = 10 chi, 1 cun = 1/10 chi, 1 bu = 6 chi

# Given values
句高 = 1 * 10 + 2  # 1丈2尺 = 12尺
下股 = 2 * 10 + 3 + Fraction(1, 10)  # 2丈3尺1寸 = 23.1尺
入股裏 = 1 * 10 + Fraction(8, 10)  # 1丈8寸 = 10.8尺
北行 = 22 * 6  # 22步 = 132尺
上登 = 51 * 6  # 51步 = 306尺
上股 = 2 * 10 + 2  # 2丈2尺 = 22尺

# Step 1: Calculate the divisor
# 以句高乘下股，如上股而一，所得
step1_result = (句高 * 下股) / 上股

# 以句高減之，餘為法
法 = step1_result - 句高

# Step 2: Calculate the dividend
# 置北行，以句高乘之，如上股而一，所得
step2_result = (北行 * 句高) / 上股

# 以減上登，餘
餘 = step2_result - 上登

# 以乘入股裏，為實
實 = 餘 * 入股裏

# Step 3: Calculate the width of the river
# 實如法而一，即得津廣
津廣 = 實 / 法

# Convert the result from chi to li (1 li = 1800 chi)
a = Fraction(津廣, 1800)  # Convert to li
"""
Code error: both arguments should be Rational instances"""
