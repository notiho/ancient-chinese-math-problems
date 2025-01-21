"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a里 。
"""

"""
Suppose someone climbs a mountain to observe a river crossing (jin), which lies south of the mountain. 
A carpenter's square is laid flat on the mountain, with the vertical leg (ju) set to a height of 1 zhang 2 chi. 
From the end of the vertical leg, looking diagonally toward the south bank of the river, the diagonal leg (xie) extends downward into the lower horizontal leg (gu) by 2 zhang 3 chi 1 cun. 
Looking toward the north bank of the river, the diagonal leg extends into the forward horizontal leg by 1 zhang 8 cun. 
The observer then climbs a higher cliff to the north, walking backward 22 bu and climbing upward 51 bu to reach the top of the cliff. 
From there, the carpenter's square is laid flat again, and from the end of the vertical leg, looking diagonally toward the south bank of the river, the diagonal leg extends into the upper horizontal leg by 2 zhang 2 chi. 
Question: What is the width of the river crossing (jin)?

The procedure says: Multiply the vertical leg (ju) by the lower horizontal leg (gu), and divide by the upper horizontal leg (gu). Subtract the result from the vertical leg (ju), and the remainder becomes the divisor. 
Take the northward walking distance, multiply it by the vertical leg (ju), and divide by the upper horizontal leg (gu). Subtract the result from the upward climbing distance, and multiply the remainder by the forward horizontal leg (gu) to obtain the dividend. 
Divide the dividend by the divisor to obtain the width of the river crossing.

Answer: *a* li.
"""

# Given values
句高 = 1 * 10 + 2  # 1丈2尺 = 12尺
下股 = 2 * 10 + 3 + Fraction(1, 10)  # 2丈3尺1寸 = 23.1尺
上股 = 2 * 10 + 2  # 2丈2尺 = 22尺
入股裏 = 1 * 10 + 8  # 1丈8寸 = 10尺 + 8寸 = 10.8尺
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

# Step 5: Multiply step4 by 入股裏 to get 實
實 = step4 * 入股裏

# Step 6: Divide 實 by 法 to get 津廣
津廣 = 實 / 法

# Convert 津廣 from 尺 to 里 (1里 = 300步 = 1500尺)
a = 津廣 / 1500
"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -0.78"""
