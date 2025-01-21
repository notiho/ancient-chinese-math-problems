"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a(=117/50)里 。
"""

"""
Suppose someone climbs a mountain to look at a ford (a shallow crossing in a river), which is south of the mountain. 
A carpenter's square is laid flat on the mountain, with the vertical leg (the "upright") being 1 zhang and 2 chi tall. 
From the tip of the upright, looking diagonally at the southern bank of the ford, the line of sight enters the lower horizontal leg (the "base") by 2 zhang, 3 chi, and 1 cun. 
Looking at the northern bank of the ford, the line of sight enters the forward base by 1 zhang and 8 cun. 

Then, climbing a higher cliff to the north, one retreats 22 bu and climbs 51 bu to reach the top of the mountain again. 
From the tip of the upright, looking diagonally at the southern bank of the ford, the line of sight enters the upper base by 2 zhang and 2 chi. 
Question: how wide is the ford?

The procedure says: Multiply the height of the upright by the lower base, and divide by the upper base. Subtract the height of the upright from the result, and the remainder is the divisor. 
Place the northern retreat, multiply it by the height of the upright, and divide by the upper base. Subtract the northern climb from the result, and multiply the remainder by the entry into the base to get the dividend. 
Divide the dividend by the divisor to get the width of the ford.

Answer: *a*(=117/50) li.
"""

# Given values
句高 = 1 * 10 + 2  # 1丈2尺 = 12尺
下股 = 2 * 10 + 3 + Fraction(1, 10)  # 2丈3尺1寸 = 23.1尺
上股 = 2 * 10 + 2  # 2丈2尺 = 22尺
北行 = 22  # 22步
上登 = 51  # 51步
入股裏 = 1 * 10 + 8  # 1丈8寸 = 10.8尺

# Step 1: Multiply 句高 by 下股, divide by 上股
step1 = (句高 * 下股) / 上股

# Subtract 句高 from the result to get the divisor (法)
法 = step1 - 句高

# Step 2: Multiply 北行 by 句高, divide by 上股
step2 = (北行 * 句高) / 上股

# Subtract 上登 from the result
step3 = step2 - 上登

# Multiply the remainder by 入股裏 to get the dividend (實)
實 = step3 * 入股裏

# Step 3: Divide the dividend by the divisor to get the width of the ford
津廣 = 實 / 法

# Convert to li (1 li = 300 chi)
a = 津廣 / 300  # 117/50 li
"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -3.9"""
