"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a(=117/50)里 。
"""

#----- content starts here -----
"""
Suppose someone climbs a mountain to look at a ford, which is south of the mountain.
A carpenter's square is placed on the mountain, with the vertical leg (height) being 1 zhang 2 chi.
From the end of the vertical leg, looking obliquely to the south bank of the ford, the lower horizontal leg extends 2 zhang 3 chi 1 cun.
Looking obliquely to the north bank of the ford, the forward horizontal leg extends 1 zhang 8 cun.
The person then climbs a higher cliff to the north, walking back 22 bu and climbing up 51 bu to reach the top of the mountain.
From the end of the vertical leg, looking obliquely to the south bank of the ford again, the upper horizontal leg extends 2 zhang 2 chi.
Question: how wide is the ford?

The procedure says: Multiply the height of the vertical leg by the lower horizontal leg, and divide by the upper horizontal leg.
Subtract the height of the vertical leg from the result, and the remainder is the divisor.
Place the northward walking distance, multiply it by the height of the vertical leg, and divide by the upper horizontal leg.
Subtract the climbing distance from the result, and multiply the remainder by the horizontal leg extending into the ford to get the dividend.
Divide the dividend by the divisor to get the width of the ford.

Answer: *a*(=117/50) li.
"""

# 句高一丈二尺
句高 = 1 * 10 + 2  # Convert to chi (1 zhang = 10 chi)

# 下股二丈三尺一寸
下股 = 2 * 10 + 3 + Fraction(1, 10)  # Convert to chi (1 zhang = 10 chi, 1 chi = 10 cun)

# 上股二丈二尺
上股 = 2 * 10 + 2  # Convert to chi

# 北行二十二步
北行 = 22

# 上登五十一步
上登 = 51

# 入股裏一丈八寸
入股裏 = 1 * 10 + Fraction(8, 10)  # Convert to chi

# Step 1: Multiply 句高 by 下股 and divide by 上股
step1 = Fraction(句高 * 下股, 上股)

# Step 2: Subtract 句高 from the result to get the divisor
法 = step1 - 句高

# Step 3: Multiply 北行 by 句高 and divide by 上股
step3 = Fraction(北行 * 句高, 上股)

# Step 4: Subtract 上登 from the result
step4 = step3 - 上登

# Step 5: Multiply the remainder by 入股裏 to get the dividend
實 = step4 * 入股裏

# Step 6: Divide the dividend by the divisor to get the width of the ford
a = Fraction(實, 法)  # 117/50 li#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -702"""
