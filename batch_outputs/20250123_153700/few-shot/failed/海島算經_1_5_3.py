"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

"""
Suppose there is a point looking southeast toward the mouth of a river. Two poles are erected, one to the south and one to the north, separated by 9 zhang. A rope is stretched across the ground connecting them.
From the northern pole, one walks westward 6 zhang and looks across the ground toward the southern bank of the river mouth. The rope is observed to enter the northern end by 4 zhang and 2 cun.
Looking toward the northern bank, the rope enters the pole by 1 zhang and 2 chi.
Then, walking further westward, 13 zhang and 5 chi from the northern pole, one observes the rope meeting the southern pole and the southern bank of the river mouth aligned.
Question: how wide is the river mouth?

The procedure says: Multiply the distance from the second observation point to the northern pole by the rope's entry at the northern end. Treat the distance between the poles as 1. Subtract the distance from the first observation point to the northern pole from the result, and the remainder becomes the divisor.
Then subtract the distance from the first observation point to the northern pole from the distance to the second observation point. Multiply the remainder by the rope's entry at the northern pole during the first observation to get the dividend.
Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: the width of the river mouth is *a* li.
"""

# Constants
表相去 = 9  # 南北表相去 9 丈
後去表 = 13 + Fraction(5, 10)  # 後去表 13 丈 5 尺
前去表 = 6  # 前去表 6 丈
入索 = 4 + Fraction(2, 10)  # 入索北端 4 丈 2 寸
入表里 = 1 + Fraction(2, 10)  # 入表里 1 丈 2 尺

# Step 1: Calculate the divisor (法)
# 以後去表乘入索，如表相去而一
後乘入索 = 後去表 * 入索

# 所得，以前去表減之，餘以為法
法 = 後乘入索 - 前去表

# Step 2: Calculate the dividend (實)
# 復以前去表減後去表，餘以乘入所望表里為實
實 = (後去表 - 前去表) * 入表里

# Step 3: Calculate the width of the river mouth (波口廣)
a = Fraction(實, 法)  # 波口廣 in 丈

# Convert to 里 (1 里 = 300 丈)
a = a / 300  # 波口廣 in 里
"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1/1690"""
