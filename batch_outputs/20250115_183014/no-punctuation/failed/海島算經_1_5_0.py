"""
今有東南望波口立兩表南北相去九丈以索薄地連之當北表之西卻行去表六丈薄地遙望波口南岸入索北端四丈二寸以望北岸入前所望表里一丈二尺又卻後行去表一十三丈五尺薄地遙望波口南岸與南表參合問波口廣幾何
術曰以後去表乘入索如表相去而一所得以前去表減之餘以為法復以前去表減後去表餘以乘入所望表里為實實如法而一得波口廣
答曰 a里 
"""

"""
Suppose there is a river mouth visible from the southeast. Two poles are erected north and south, 9 zhang apart. A rope is stretched across the ground connecting them.
At the northern pole, move westward 6 zhang and stretch the rope to the southern bank of the river mouth. The northern end of the rope enters the southern bank by 4 zhang and 2 cun.
Looking northward, the rope enters the northern bank by 1 zhang and 2 chi from the previously observed pole.
Then, move further westward 13 zhang and 5 chi from the northern pole. Stretch the rope to the southern bank of the river mouth, aligning with the southern pole.
Question: What is the width of the river mouth?

The procedure says:
1. Multiply the distance moved westward after the northern pole (later distance) by the rope's southern bank entry (later entry).
2. Divide by the distance between the poles (north-south distance).
3. Subtract the earlier distance moved westward from the northern pole (earlier distance) from the result. The remainder is the divisor.
4. Subtract the later distance from the earlier distance. Multiply the remainder by the rope's northern bank entry (earlier entry). This is the dividend.
5. Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: The width of the river mouth is *a* li.
"""

# 南北相去 9 丈
表相去 = 9

# 當北表之西卻行去表 6 丈
前去表 = 6

# 入索北端 4 丈 2 寸
入索南岸 = 4 + Fraction(2, 10)

# 望北岸入前所望表里 1 丈 2 尺
入所望表里 = 1 + Fraction(2, 10)

# 卻後行去表 13 丈 5 尺
後去表 = 13 + Fraction(5, 10)

# 薄地遙望波口南岸與南表參合
入索後南岸 = 入索南岸  # Same as earlier for calculation consistency.

# Step 1: Multiply the later distance by the later southern bank entry
step1 = 後去表 * 入索後南岸

# Step 2: Divide by the distance between the poles
step2 = Fraction(step1, 表相去)

# Step 3: Subtract the earlier distance from the result to get the divisor
法 = step2 - 前去表

# Step 4: Subtract the later distance from the earlier distance
step4 = 前去表 - 後去表

# Multiply the result by the earlier northern bank entry to get the dividend
實 = step4 * 入所望表里

# Step 5: Divide the dividend by the divisor to get the width of the river mouth
波口廣 = Fraction(實, 法)

# Convert to li (1 丈 = 1/15 里)
a = 波口廣 / 15
"""
Variable 'a' has wrong value. Expected: 5/3, Actual: -2"""
