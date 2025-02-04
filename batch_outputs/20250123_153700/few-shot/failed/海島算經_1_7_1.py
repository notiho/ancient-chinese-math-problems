"""
今有登山望津，津在山南。偃矩山上，令句高一丈二尺。從句端斜望津南岸，入下股二丈三尺一寸。又望津北岸，入前望股裏一丈八寸。更登高巖北，卻行二十二步，上登五十一步，偃矩山上。更從句端斜望津南岸，入上股二丈二尺。問津廣幾何？
術曰：以句高乘下股，如上股而一。所得以句高減之，餘為法；置北行，以句高乘之，如上股而一。所得以減上登，餘以乘入股裏為實。實如法而一，即得津廣。
答曰： a里 。
"""

"""
Suppose one climbs a mountain to look at a ford (river crossing), with the ford located south of the mountain.
A carpenter's square is laid flat on the mountain, with the vertical leg (height) being 1 zhang and 2 chi.
From the top of the vertical leg, looking diagonally at the southern bank of the ford, the diagonal leg (lower hypotenuse) extends 2 zhang, 3 chi, and 1 cun into the lower base.
Looking diagonally at the northern bank of the ford, the diagonal leg extends 1 zhang and 8 cun into the forward base.
Then, climbing a higher cliff to the north, one retreats 22 bu northward and ascends 51 bu upward, laying the carpenter's square flat again.
From the top of the vertical leg, looking diagonally at the southern bank of the ford, the diagonal leg (upper hypotenuse) extends 2 zhang and 2 chi into the upper base.
Question: what is the width of the ford?

The procedure says: Multiply the height of the vertical leg by the lower base, and divide by the upper base.
Subtract the result from the height of the vertical leg, and the remainder becomes the divisor.
Place the northward retreat, multiply it by the height of the vertical leg, and divide by the upper base.
Subtract the result from the upward climb, and multiply the remainder by the forward base to obtain the dividend.
Divide the dividend by the divisor to obtain the width of the ford.

Answer: *a* li.
"""

# Define units in terms of chi
丈 = 10  # 1 zhang = 10 chi
尺 = 1   # 1 chi = 1 chi
寸 = Fraction(1, 10)  # 1 cun = 1/10 chi
步 = 6   # 1 bu = 6 chi
里 = 300  # 1 li = 300 chi

# Input values
句高 = 1 * 丈 + 2 * 尺  # Vertical leg height: 1 zhang 2 chi
下股 = 2 * 丈 + 3 * 尺 + 1 * 寸  # Lower base: 2 zhang 3 chi 1 cun
入股裏 = 1 * 丈 + 8 * 寸  # Forward base: 1 zhang 8 cun
北行 = 22 * 步  # Northward retreat: 22 bu
上登 = 51 * 步  # Upward climb: 51 bu
上股 = 2 * 丈 + 2 * 尺  # Upper base: 2 zhang 2 chi

# Step 1: Multiply 句高 by 下股, divide by 上股
step1 = (句高 * 下股) / 上股

# Step 2: Subtract result from 句高 to get 法 (divisor)
法 = 句高 - step1

# Step 3: Multiply 北行 by 句高, divide by 上股
step3 = (北行 * 句高) / 上股

# Step 4: Subtract result from 上登
step4 = 上登 - step3

# Step 5: Multiply remainder by 入股裏 to get 實 (dividend)
實 = step4 * 入股裏

# Step 6: Divide 實 by 法 to get 津廣
津廣 = 實 / 法

# Convert 津廣 from chi to li
a = 津廣 / 里
"""
Variable 'a' has wrong value. Expected: 117/50, Actual: -14.040000000000003"""
