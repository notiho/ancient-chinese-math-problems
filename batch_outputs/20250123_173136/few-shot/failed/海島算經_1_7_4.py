"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a里 。
"""

"""
Suppose someone climbs a mountain to observe a ford, which lies south of the mountain. 
A carpenter's square is placed on the mountain, with the vertical leg (the "upright") being 1 zhang and 2 chi tall.
From the tip of the vertical leg, they look diagonally to the south bank of the ford, which enters the lower horizontal leg (the "base") by 2 zhang, 3 chi, and 1 cun.
They also look to the north bank of the ford, which enters the forward horizontal leg by 1 zhang and 8 cun.
Then, they climb a higher cliff to the north, retreating 22 bu and ascending 51 bu, placing another carpenter's square on the mountain.
From the tip of the vertical leg, they again look diagonally to the south bank of the ford, which enters the upper horizontal leg by 2 zhang and 2 chi.
Question: how wide is the ford?

The procedure says: Multiply the height of the vertical leg by the lower horizontal leg, dividing by the upper horizontal leg. 
Subtract the result from the height of the vertical leg, and the remainder becomes the divisor.
Place the northward retreat, multiply it by the height of the vertical leg, dividing by the upper horizontal leg.
Subtract the result from the upward climb, and multiply the remainder by the forward horizontal leg to get the dividend.
Divide the dividend by the divisor to get the width of the ford.

The answer says: *a* li.
"""

# Define units
zhang_to_chi = 10  # 1 zhang = 10 chi
chi_to_cun = 10    # 1 chi = 10 cun
bu_to_chi = 6      # 1 bu = 6 chi
chi_to_li = 300    # 1 li = 300 chi

# Given values
句高 = 1 * zhang_to_chi + 2  # 1丈2尺 = 12尺
下股 = 2 * zhang_to_chi + 3 + Fraction(1, chi_to_cun)  # 2丈3尺1寸 = 23.1尺
入股裏 = 1 * zhang_to_chi + Fraction(8, chi_to_cun)  # 1丈8寸 = 10.8尺
北行 = 22 * bu_to_chi  # 22步 = 132尺
上登 = 51 * bu_to_chi  # 51步 = 306尺
上股 = 2 * zhang_to_chi + 2  # 2丈2尺 = 22尺

# Procedure
# Step 1: Multiply the height of the vertical leg by the lower horizontal leg, dividing by the upper horizontal leg
step1 = Fraction(句高 * 下股, 上股)

# Step 2: Subtract the result from the height of the vertical leg, and the remainder becomes the divisor
法 = 句高 - step1

# Step 3: Multiply the northward retreat by the height of the vertical leg, dividing by the upper horizontal leg
step3 = Fraction(北行 * 句高, 上股)

# Step 4: Subtract the result from the upward climb
step4 = 上登 - step3

# Step 5: Multiply the remainder by the forward horizontal leg to get the dividend
實 = step4 * 入股裏

# Step 6: Divide the dividend by the divisor to get the width of the ford
津廣 = Fraction(實, 法)

# Convert the result to li
a = Fraction(津廣, chi_to_li)  # Convert chi to li
"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -351/25"""
