"""
今有東南望波口立兩表南北相去九丈以索薄地連之當北表之西卻行去表六丈薄地遙望波口南岸入索北端四丈二寸以望北岸入前所望表里一丈二尺又卻後行去表一十三丈五尺薄地遙望波口南岸與南表參合問波口廣幾何
術曰以後去表乘入索如表相去而一所得以前去表減之餘以為法復以前去表減後去表餘以乘入所望表里為實實如法而一得波口廣
答曰 a里 
"""

#----- content starts here -----
"""
Suppose there is a scenario where one observes a river mouth from the southeast. Two poles are erected, aligned north-south, and are 9 zhang apart. A rope is stretched across the ground connecting the poles. Starting at the west of the northern pole, one walks 6 zhang away from the pole. The rope is stretched to the southern bank of the river mouth, and the northern end of the rope is 4 zhang 2 cun into the river. Observing the northern bank, the distance from the previous observation point to the pole is 1 zhang 2 chi. Then, moving further back, one walks 13 zhang 5 chi away from the pole. The rope is stretched again to the southern bank of the river mouth, aligning with the southern pole.

Question: What is the width of the river mouth?

The procedure says: Multiply the distance walked back from the pole (after the second observation) by the rope's length into the river. Divide this by the distance between the poles. Subtract the result from the distance walked back during the first observation. The remainder becomes the divisor. Subtract the first distance walked back from the second distance walked back. Multiply the result by the distance observed from the pole to the northern bank. This becomes the dividend. Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: The width of the river mouth is *a* li.
"""

# 南北相去 9 丈
表相去 = 9

# 當北表之西卻行去表 6 丈
前去表 = 6

# 入索北端 4 丈 2 寸
入索 = 4 + Fraction(2, 10)

# 望北岸入前所望表里 1 丈 2 尺
所望表里 = 1 + Fraction(2, 10)

# 卻後行去表 13 丈 5 尺
後去表 = 13 + Fraction(5, 10)

# Step 1: 以後去表乘入索
後乘入索 = 後去表 * 入索

# Step 2: 如表相去而一
後乘入索除表相去 = Fraction(後乘入索, 表相去)

# Step 3: 所得以前去表減之，餘以為法
法 = 前去表 - 後乘入索除表相去

# Step 4: 復以前去表減後去表，餘以乘入所望表里
實 = (後去表 - 前去表) * 所望表里

# Step 5: 實如法而一
波口廣 = Fraction(實, 法)

# Convert to li (1 丈 = 1/300 里)
a = 波口廣 / 300#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/3, Actual: -1/10"""
