"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a(=117/50)里 。
"""

#----- content starts here -----
"""
Suppose someone climbs a mountain to look at a ford, which is south of the mountain. 
A right triangle is formed on the mountain, with the vertical leg (height) being 1 zhang 2 chi. 
From the top of the vertical leg, looking diagonally to the south bank of the ford, the diagonal enters the lower horizontal leg by 2 zhang 3 chi 1 cun. 
Looking diagonally to the north bank, the diagonal enters the forward horizontal leg by 1 zhang 8 cun. 

The person then climbs a higher cliff to the north, walking backward 22 bu and climbing upward 51 bu to reach the top. 
From there, looking diagonally to the south bank of the ford again, the diagonal enters the upper horizontal leg by 2 zhang 2 chi. 
Question: What is the width of the ford?

The procedure says: Multiply the height of the vertical leg by the lower horizontal leg, dividing by the upper horizontal leg. 
Subtract the result from the height of the vertical leg, and the remainder becomes the divisor. 
Place the backward walking distance, multiply it by the height of the vertical leg, and divide by the upper horizontal leg. 
Subtract the result from the upward climbing distance, and multiply the remainder by the horizontal leg entry to get the dividend. 
Divide the dividend by the divisor to obtain the width of the ford.

Answer: *a*(=117/50) li.
"""

# Define units in chi
丈 = 10  # 1 zhang = 10 chi
尺 = 1   # 1 chi = 1 chi
寸 = Fraction(1, 10)  # 1 cun = 1/10 chi
步 = 6  # 1 bu = 6 chi
里 = 300  # 1 li = 300 chi

# Given values
句高 = 1 * 丈 + 2 * 尺  # Height of the vertical leg
下股 = 2 * 丈 + 3 * 尺 + 1 * 寸  # Lower horizontal leg entry
上股 = 2 * 丈 + 2 * 尺  # Upper horizontal leg entry
北行 = 22 * 步  # Backward walking distance
上登 = 51 * 步  # Upward climbing distance

# Procedure calculations
# Step 1: Multiply the height by the lower horizontal leg, divide by the upper horizontal leg
step1_result = (句高 * 下股) / 上股

# Step 2: Subtract the result from the height to get the divisor
法 = 句高 - step1_result

# Step 3: Multiply the backward walking distance by the height, divide by the upper horizontal leg
step3_result = (北行 * 句高) / 上股

# Step 4: Subtract the result from the upward climbing distance
step4_result = 上登 - step3_result

# Step 5: Multiply the remainder by the horizontal leg entry to get the dividend
實 = step4_result * 下股

# Step 6: Divide the dividend by the divisor to get the width of the ford
津廣 = 實 / 法

# Convert the result to li
a = 津廣 / 里  # 117/50 li#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -30.030000000000005"""
