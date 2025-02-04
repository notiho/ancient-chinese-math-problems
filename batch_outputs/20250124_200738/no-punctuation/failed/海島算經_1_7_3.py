"""
今有登山望津津在山南偃矩山上令句高一丈二尺從句端斜望津南岸入下股二丈三尺一寸又望津北岸入前望股裏一丈八寸更登高巖北卻行二十二步上登五十一步偃矩山上更從句端斜望津南岸入上股二丈二尺問津廣幾何
術曰以句高乘下股如上股而一所得以句高減之餘為法置北行以句高乘之如上股而一所得以減上登餘以乘入股裏為實實如法而一即得津廣
答曰 a里 
"""

#----- content starts here -----
"""
Suppose someone climbs a mountain to look at a river crossing. The river crossing is south of the mountain. 
A right triangle is formed with the mountain. The height of the mountain (the vertical leg) is 1 zhang 2 chi. 
From the top of the mountain, looking diagonally to the south bank of the river, the diagonal leg enters the lower horizontal leg by 2 zhang 3 chi 1 cun. 
Looking diagonally to the north bank of the river, the diagonal leg enters the forward horizontal leg by 1 zhang 8 cun. 
The person then climbs a higher peak to the north, walking backward 22 bu and climbing upward 51 bu. 
From the top of the higher peak, looking diagonally to the south bank of the river, the diagonal leg enters the upper horizontal leg by 2 zhang 2 chi. 
Question: how wide is the river?

The procedure says: Multiply the height of the mountain by the lower horizontal leg. Divide by the upper horizontal leg. Subtract the result from the height of the mountain. The remainder is the divisor.
Place the backward walking distance. Multiply it by the height of the mountain. Divide by the upper horizontal leg. Subtract the result from the climbing distance. Multiply the remainder by the forward horizontal leg. This is the dividend.
Divide the dividend by the divisor to obtain the width of the river.

Answer: *a* li.
"""

# Convert all measurements to chi for consistency
# 1 zhang = 10 chi, 1 chi = 10 cun

# 句高 (height of the mountain): 1丈2尺 = 12尺
句高 = 12

# 下股 (lower horizontal leg): 2丈3尺1寸 = 23尺1寸 = 231/10 尺
下股 = Fraction(231, 10)

# 上股 (upper horizontal leg): 2丈2尺 = 22尺
上股 = 22

# 股裏 (forward horizontal leg): 1丈8寸 = 10尺8寸 = 108/10 尺
股裏 = Fraction(108, 10)

# 北卻行 (backward walking distance): 22步
北行 = 22

# 上登 (climbing distance): 51步
上登 = 51

# Step 1: Multiply 句高 by 下股, divide by 上股
step1_result = (句高 * 下股) / 上股

# Subtract the result from 句高 to get the divisor (法)
法 = 句高 - step1_result

# Step 2: Multiply 北行 by 句高, divide by 上股
step2_result = (北行 * 句高) / 上股

# Subtract the result from 上登
remainder = 上登 - step2_result

# Multiply the remainder by 股裏 to get the dividend (實)
實 = remainder * 股裏

# Divide the dividend by the divisor to get the river width in chi
津廣 = 實 / 法

# Convert the river width from chi to li (1 li = 300 chi)
a = 津廣 / 300#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -2.3400000000000003"""
