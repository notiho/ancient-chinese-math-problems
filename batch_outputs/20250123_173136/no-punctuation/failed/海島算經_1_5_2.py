"""
今有東南望波口立兩表南北相去九丈以索薄地連之當北表之西卻行去表六丈薄地遙望波口南岸入索北端四丈二寸以望北岸入前所望表里一丈二尺又卻後行去表一十三丈五尺薄地遙望波口南岸與南表參合問波口廣幾何
術曰以後去表乘入索如表相去而一所得以前去表減之餘以為法復以前去表減後去表餘以乘入所望表里為實實如法而一得波口廣
答曰 a里 
"""

"""
Suppose there is a scenario where one observes a river mouth from the southeast. Two poles are placed north-south, 9 zhang apart. A rope is stretched across the ground connecting them. 
Starting at the west of the northern pole, one walks 6 zhang away from the pole. Stretching the rope, the southern end of the rope reaches 4 zhang and 2 cun into the southern bank of the river mouth. Observing the northern bank, the rope extends 1 zhang and 2 chi into the area inside the northern pole. 
Then, one walks further back, 13 zhang and 5 chi away from the northern pole. Stretching the rope again, it aligns with the southern pole and the southern bank of the river mouth.

Question: What is the width of the river mouth?

The procedure says:
1. Multiply the distance walked back (after the northern pole) by the rope's southern bank extension. If the distance between the poles is treated as 1, subtract the earlier distance walked back from this product. The remainder becomes the divisor.
2. Subtract the earlier distance walked back from the later distance walked back. Multiply this difference by the northern bank extension of the rope. This product becomes the dividend.
3. Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: The width of the river mouth is *a* li.
"""

# 南北相去 9 丈
表相去 = 9

# 當北表之西卻行去表 6 丈
前去表 = 6

# 入索北端 4 丈 2 寸
入索南岸 = 4 + Fraction(2, 10)

# 以望北岸入前所望表里 1 丈 2 尺
入所望表里 = 1 + Fraction(2, 10)

# 卻後行去表 13 丈 5 尺
後去表 = 13 + Fraction(5, 10)

# Step 1: Calculate the divisor
# 以後去表乘入索
後去表乘入索 = 後去表 * 入索南岸

# 如表相去而一，所得以前去表減之，餘以為法
法 = 後去表乘入索 - 表相去 * 前去表

# Step 2: Calculate the dividend
# 復以前去表減後去表，餘以乘入所望表里
實 = (後去表 - 前去表) * 入所望表里

# Step 3: Divide the dividend by the divisor to get the width of the river mouth
波口廣 = Fraction(實, 法)

# Convert the result to li (1 丈 = 1/300 里)
a = 波口廣 / 300
"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1/90"""
