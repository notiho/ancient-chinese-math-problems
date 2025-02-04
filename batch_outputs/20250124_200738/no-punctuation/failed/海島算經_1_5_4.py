"""
今有東南望波口立兩表南北相去九丈以索薄地連之當北表之西卻行去表六丈薄地遙望波口南岸入索北端四丈二寸以望北岸入前所望表里一丈二尺又卻後行去表一十三丈五尺薄地遙望波口南岸與南表參合問波口廣幾何
術曰以後去表乘入索如表相去而一所得以前去表減之餘以為法復以前去表減後去表餘以乘入所望表里為實實如法而一得波口廣
答曰 a里 
"""

#----- content starts here -----
"""
Suppose there is a scenario where one observes a river mouth from the southeast. Two poles are erected, aligned north-south, and are 9 zhang apart. A rope is stretched across the ground connecting them. 

One walks westward from the northern pole for 6 zhang and stretches the rope to observe the river mouth's southern bank. The rope's northern end is 4 zhang and 2 cun away from the pole, and the observation point is 1 zhang and 2 chi inside the pole. 

Then, one walks further westward from the northern pole for 13 zhang and 5 chi and stretches the rope again to observe the river mouth's southern bank. This time, the observation aligns with the southern pole.

Question: What is the width of the river mouth?

The procedure says:
1. Multiply the distance walked after the northern pole (後去表) by the rope length (入索). If the result equals the distance between the poles (表相去), subtract the earlier distance walked (以前去表). The remainder is the divisor (法).
2. Subtract the earlier distance walked (以前去表) from the later distance walked (後去表). Multiply the remainder by the distance observed inside the pole (入所望表里). This is the dividend (實).
3. Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: The river mouth is *a* li wide.
"""

# Constants
表相去 = 9  # 表相去 (distance between the poles) in 丈

# First observation
以前去表 = 6  # 以前去表 (earlier distance walked) in 丈
入索 = Fraction(42, 10)  # 入索 (rope length) in 丈 (4丈2寸 = 4.2丈)
入所望表里 = Fraction(12, 10)  # 入所望表里 (distance observed inside the pole) in 丈 (1丈2尺 = 1.2丈)

# Second observation
後去表 = Fraction(135, 10)  # 後去表 (later distance walked) in 丈 (13丈5尺 = 13.5丈)

# Step 1: Calculate the divisor (法)
法 = (後去表 * 入索 - 表相去)

# Step 2: Calculate the dividend (實)
實 = (後去表 - 以前去表) * 入所望表里

# Step 3: Calculate the width of the river mouth
波口廣 = Fraction(實, 法)

# Convert to li (1 丈 = 1/300 里)
a = 波口廣 / 300  # 波口廣 in 里

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1/1590"""
