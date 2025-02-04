"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a(=117/50)里 。
"""

"""
Suppose someone climbs a mountain to look at a ford, which is south of the mountain. 
A right triangle is laid flat on the mountain, with the vertical leg (height) being 1 zhang 2 chi. 
From the top of the vertical leg, looking diagonally to the southern bank of the ford, the diagonal enters the lower horizontal leg by 2 zhang 3 chi 1 cun. 
Looking diagonally to the northern bank of the ford, the diagonal enters the forward horizontal leg by 1 zhang 8 cun. 

Later, the person climbs a higher peak to the north, walking backward 22 bu and climbing upward 51 bu to reach the top of the mountain. 
From the top of the vertical leg, looking diagonally to the southern bank of the ford again, the diagonal enters the upper horizontal leg by 2 zhang 2 chi. 
Question: What is the width of the ford?

The procedure says: Multiply the height of the vertical leg by the lower horizontal leg, then divide by the upper horizontal leg. Subtract the height of the vertical leg from the result, and the remainder becomes the divisor. 
Place the backward walking distance, multiply it by the height of the vertical leg, then divide by the upper horizontal leg. Subtract the climbing distance from the result, and multiply the remainder by the distance entered into the horizontal leg to get the dividend. 
Divide the dividend by the divisor to obtain the width of the ford.

Answer: *a*(=117/50) li.
"""

# Define units
丈 = 10  # 1 丈 = 10 尺
尺 = 1   # 1 尺 = 1 尺
寸 = Fraction(1, 10)  # 1 寸 = 1/10 尺
步 = 6  # 1 步 = 6 尺
里 = 300  # 1 里 = 300 步

# Given values
句高 = 1 * 丈 + 2 * 尺  # 1 丈 2 尺
下股 = 2 * 丈 + 3 * 尺 + 1 * 寸  # 2 丈 3 尺 1 寸
上股 = 2 * 丈 + 2 * 尺  # 2 丈 2 尺
望股裏 = 1 * 丈 + 8 * 寸  # 1 丈 8 寸
北行 = 22 * 步  # 22 步
上登 = 51 * 步  # 51 步

# Step 1: Multiply 句高 by 下股, divide by 上股
step1 = (句高 * 下股) / 上股

# Step 2: Subtract 句高 from the result to get 法
法 = step1 - 句高

# Step 3: Multiply 北行 by 句高, divide by 上股
step3 = (北行 * 句高) / 上股

# Step 4: Subtract 上登 from the result
step4 = step3 - 上登

# Step 5: Multiply the remainder by 望股裏 to get 實
實 = step4 * 望股裏

# Step 6: Divide 實 by 法 to get 津廣
津廣 = 實 / 法

# Convert 津廣 to 里
a = 津廣 / 里  # 117/50 里
"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -14.040000000000003"""
