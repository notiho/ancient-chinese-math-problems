"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

"""
Suppose there is an observation of a river mouth from the southeast. Two poles are erected, one to the south and one to the north, with a distance of 9 zhang between them. A rope is stretched across the ground connecting the two poles.
From the north pole, walk westward 6 zhang, and from there, observe the south bank of the river mouth. The rope enters the northern end by 4 zhang and 2 cun. Then, observe the north bank, and the rope enters the previous observation point by 1 zhang and 2 chi.
Next, walk further westward, 13 zhang and 5 chi from the north pole. From there, observe the south bank of the river mouth, aligning with the south pole.
Question: What is the width of the river mouth?

The procedure says: Multiply the distance from the second observation point to the north pole by the rope's entry at the northern end. Divide the result by the distance between the two poles to get a preliminary value. Subtract the distance from the first observation point to the north pole from this value, and the remainder becomes the divisor. Subtract the distance from the first observation point to the north pole from the second observation point, and multiply the result by the rope's entry at the first observation point. This becomes the dividend. Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: The width of the river mouth is *a* li.
"""

# Constants and conversions
丈_to_尺 = 10  # 1 丈 = 10 尺
尺_to_寸 = 10  # 1 尺 = 10 寸
尺_to_里 = Fraction(1, 300)  # 1 里 = 300 尺

# Data
表相去 = 9 * 丈_to_尺  # 南北表相距 9 丈
第一次去表 = 6 * 丈_to_尺  # 第一次去北表 6 丈
第一次入索 = 4 * 丈_to_尺 + 2  # 第一次入索 4 丈 2 寸
第一次入表里 = 1 * 丈_to_尺 + 2  # 第一次入表里 1 丈 2 尺
第二次去表 = 13 * 丈_to_尺 + 5  # 第二次去北表 13 丈 5 尺

# Procedure
# Step 1: Multiply the second distance to the pole by the rope's entry at the northern end
step1 = 第二次去表 * 第一次入索

# Step 2: Divide by the distance between the poles
step2 = Fraction(step1, 表相去)

# Step 3: Subtract the first distance to the pole
法 = step2 - 第一次去表

# Step 4: Subtract the first distance to the pole from the second distance to the pole
step4 = 第二次去表 - 第一次去表

# Step 5: Multiply the result by the rope's entry at the first observation point
實 = step4 * 第一次入表里

# Step 6: Divide the dividend by the divisor to get the width of the river mouth
波口廣 = Fraction(實, 法)

# Convert the result to li
a = 波口廣 * 尺_to_里
"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1"""
