"""
今有東南望波口立兩表南北相去九丈以索薄地連之當北表之西卻行去表六丈薄地遙望波口南岸入索北端四丈二寸以望北岸入前所望表里一丈二尺又卻後行去表一十三丈五尺薄地遙望波口南岸與南表參合問波口廣幾何
術曰以後去表乘入索如表相去而一所得以前去表減之餘以為法復以前去表減後去表餘以乘入所望表里為實實如法而一得波口廣
答曰 a里 
"""

#----- content starts here -----
"""
Suppose there is a situation where one observes a river mouth from the southeast. Two poles are erected, aligned north-south, and separated by 9 zhang. A rope is stretched across the ground connecting the poles. 

From the north pole, one moves westward 6 zhang and stretches the rope to observe the river mouth's southern bank. The rope's northern end enters the southern bank by 4 zhang and 2 cun. Observing the northern bank, the rope enters the previous observation point by 1 zhang and 2 chi.

Then, moving further westward from the north pole by 13 zhang and 5 chi, the rope is stretched again to observe the river mouth's southern bank, aligning with the southern pole.

Question: What is the width of the river mouth?

The procedure says:
1. Multiply the distance moved westward after the second observation by the rope's entry into the southern bank.
2. Divide the result by the distance between the poles.
3. Subtract the distance moved westward during the first observation from the result. The remainder becomes the divisor.
4. Subtract the first westward distance from the second westward distance. Multiply the remainder by the rope's entry into the northern bank during the first observation. This becomes the dividend.
5. Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: The width of the river mouth is *a* li.
"""

# 南北相去九丈
表相去 = 9  # 丈

# 當北表之西卻行去表六丈
前去表 = 6  # 丈

# 入索北端四丈二寸
入索 = 4 + Fraction(2, 10)  # 丈

# 以望北岸入前所望表里一丈二尺
入所望表里 = 1 + Fraction(2, 10)  # 丈

# 又卻後行去表一十三丈五尺
後去表 = 13 + Fraction(5, 10)  # 丈

# 薄地遙望波口南岸與南表參合
# 求波口廣

# Step 1: 以後去表乘入索
step1 = 後去表 * 入索

# Step 2: 如表相去而一
step2 = Fraction(step1, 表相去)

# Step 3: 所得以前去表減之，餘以為法
法 = step2 - 前去表

# Step 4: 復以前去表減後去表，餘以乘入所望表里為實
實 = (後去表 - 前去表) * 入所望表里

# Step 5: 實如法而一，得波口廣
波口廣 = Fraction(實, 法)

# Convert to li (1 丈 = 1/300 里)
a = 波口廣 / 300  # Convert 丈 to 里#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1/10"""
