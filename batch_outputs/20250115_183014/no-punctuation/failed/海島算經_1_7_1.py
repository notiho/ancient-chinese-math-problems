"""
今有登山望津津在山南偃矩山上令句高一丈二尺從句端斜望津南岸入下股二丈三尺一寸又望津北岸入前望股裏一丈八寸更登高巖北卻行二十二步上登五十一步偃矩山上更從句端斜望津南岸入上股二丈二尺問津廣幾何
術曰以句高乘下股如上股而一所得以句高減之餘為法置北行以句高乘之如上股而一所得以減上登餘以乘入股裏為實實如法而一即得津廣
答曰 a里 
"""

"""
Suppose someone climbs a mountain to observe a river crossing. The river crossing is south of the mountain.
A right-angled triangle is formed on the mountain. Let the vertical leg (height) of the triangle be 1 zhang 2 chi.
From the top of the vertical leg, looking diagonally to the southern bank of the river, the diagonal enters the lower horizontal leg by 2 zhang 3 chi 1 cun.
Looking diagonally to the northern bank of the river, the diagonal enters the forward horizontal leg by 1 zhang 8 cun.
The observer then climbs a higher peak to the north, walking back 22 bu and climbing up 51 bu.
From the top of the new vertical leg, looking diagonally to the southern bank of the river, the diagonal enters the upper horizontal leg by 2 zhang 2 chi.
Question: How wide is the river crossing?

The procedure says:
1. Multiply the height of the vertical leg by the lower horizontal leg. Divide by the upper horizontal leg. Subtract the height of the vertical leg. The remainder is the divisor.
2. Place the northward walk. Multiply it by the height of the vertical leg. Divide by the upper horizontal leg. Subtract the upward climb. Multiply the remainder by the forward horizontal leg. This is the dividend.
3. Divide the dividend by the divisor to obtain the width of the river crossing.

Answer: *a* li.
"""

# Initial measurements
句高 = 1 * 10 + 2  # 1丈2尺 = 12尺
下股 = 2 * 10 + 3 + Fraction(1, 10)  # 2丈3尺1寸 = 23.1尺
上股 = 2 * 10 + 2  # 2丈2尺 = 22尺
股裏 = 1 * 10 + Fraction(8, 10)  # 1丈8寸 = 10.8尺
北行 = 22  # 22步
上登 = 51  # 51步

# Step 1: Calculate the divisor
# 以句高乘下股，如上股而一
step1_result = (句高 * 下股) / 上股
# 所得以句高減之，餘為法
法 = step1_result - 句高

# Step 2: Calculate the dividend
# 置北行，以句高乘之，如上股而一
step2_result = (北行 * 句高) / 上股
# 所得以減上登
step2_remainder = step2_result - 上登
# 餘以乘入股裏，為實
實 = step2_remainder * 股裏

# Step 3: Calculate the river width
# 實如法而一，即得津廣
津廣 = 實 / 法

# Convert the result to li (1 li = 300 chi)
a = 津廣 / 300  # Convert from chi to li
"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -2.3400000000000003"""
