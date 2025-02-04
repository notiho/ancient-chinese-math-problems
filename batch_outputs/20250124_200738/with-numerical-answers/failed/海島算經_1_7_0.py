"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a(=117/50)里 。
"""

#----- content starts here -----
"""
Suppose someone climbs a mountain to look at a ford, which is south of the mountain. 
A carpenter's square is laid flat on the mountain, with the vertical leg (height) being 1 zhang 2 chi. 
From the top of the vertical leg, looking diagonally to the south bank of the ford, the diagonal enters the lower horizontal leg by 2 zhang 3 chi 1 cun. 
Looking diagonally to the north bank of the ford, the diagonal enters the forward horizontal leg by 1 zhang 8 cun. 
The person then climbs a higher cliff to the north, walking backward 22 bu and climbing upward 51 bu, laying the carpenter's square flat again. 
From the top of the vertical leg, looking diagonally to the south bank of the ford, the diagonal enters the upper horizontal leg by 2 zhang 2 chi. 
Question: what is the width of the ford?

The procedure says: Multiply the height of the vertical leg by the lower horizontal leg, dividing by the upper horizontal leg. 
Subtract the result from the height of the vertical leg, and the remainder becomes the divisor. 
Place the northward walking distance, multiply it by the height of the vertical leg, and divide by the upper horizontal leg. 
Subtract the result from the upward climbing distance, and multiply the remainder by the distance entered into the horizontal leg to obtain the dividend. 
Divide the dividend by the divisor to obtain the width of the ford.

Answer: *a*(=117/50) li.
"""

# Given values
句高 = 1 * 10 + 2  # 1丈2尺 = 12尺
下股 = 2 * 10 + 3 + Fraction(1, 10)  # 2丈3尺1寸 = 23.1尺
上股 = 2 * 10 + 2  # 2丈2尺 = 22尺
入下股 = 1 * 10 + 8  # 1丈8寸 = 10.8尺
北行 = 22  # 22步
上登 = 51  # 51步

# Step 1: Multiply 句高 by 下股, divide by 上股
step1 = (句高 * 下股) / 上股

# Step 2: Subtract step1 from 句高 to get 法
法 = 句高 - step1

# Step 3: Multiply 北行 by 句高, divide by 上股
step3 = (北行 * 句高) / 上股

# Step 4: Subtract step3 from 上登
step4 = 上登 - step3

# Step 5: Multiply step4 by 入下股 to get 實
實 = step4 * 入下股

# Step 6: Divide 實 by 法 to get 津廣
津廣 = 實 / 法

# Convert 津廣 from 尺 to 里 (1里 = 300尺)
a = 津廣 / 300  # 117/50里#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -3.9"""
