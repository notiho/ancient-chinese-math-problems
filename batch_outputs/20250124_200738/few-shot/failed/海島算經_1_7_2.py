"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a里 。
"""

#----- content starts here -----
"""
Suppose one climbs a mountain to look at a ford, which is south of the mountain. 
A right triangle is formed on the mountain, where the vertical leg (height) is 1 zhang and 2 chi. 
From the top of the vertical leg, looking diagonally to the south bank of the ford, the diagonal leg extends 2 zhang, 3 chi, and 1 cun into the lower horizontal leg. 
Looking diagonally to the north bank of the ford, the diagonal leg extends 1 zhang and 8 cun into the forward horizontal leg.

Then, climbing a higher cliff to the north, one retreats 22 bu, ascends 51 bu, and forms another right triangle on the mountain. 
From the top of the new vertical leg, looking diagonally to the south bank of the ford, the diagonal leg extends 2 zhang and 2 chi into the upper horizontal leg. 
Question: how wide is the ford?

The procedure says: Multiply the height of the vertical leg by the lower horizontal leg, and divide by the upper horizontal leg. Subtract the result from the height of the vertical leg, and the remainder becomes the divisor. 
Place the northward retreat, multiply it by the height of the vertical leg, and divide by the upper horizontal leg. Subtract the result from the northward ascent, and multiply the remainder by the forward horizontal leg to obtain the dividend. 
Divide the dividend by the divisor to obtain the width of the ford.

Answer: *a* li.
"""

from fractions import Fraction

# Input values
句高 = 1 * 10 + 2  # 1丈2尺 converted to chi
下股 = 2 * 10 + 3 + Fraction(1, 10)  # 2丈3尺1寸 converted to chi
上股 = 2 * 10 + 2  # 2丈2尺 converted to chi
北行 = 22 * 6  # 22步 converted to chi (1步 = 6 chi)
上登 = 51 * 6  # 51步 converted to chi (1步 = 6 chi)
入股裏 = 1 * 10 + Fraction(8, 10)  # 1丈8寸 converted to chi

# Step 1: Multiply 句高 by 下股, divide by 上股
step1 = Fraction(句高 * 下股, 上股)

# Step 2: Subtract step1 from 句高 to get 法
法 = 句高 - step1

# Step 3: Multiply 北行 by 句高, divide by 上股
step3 = Fraction(北行 * 句高, 上股)

# Step 4: Subtract step3 from 上登
step4 = 上登 - step3

# Step 5: Multiply step4 by 入股裏 to get 實
實 = step4 * 入股裏

# Step 6: Divide 實 by 法 to get 津廣
津廣 = Fraction(實, 法)

# Convert 津廣 from chi to li (1 li = 1800 chi)
a = Fraction(津廣, 1800)  # 津廣 in li

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -117/50"""
