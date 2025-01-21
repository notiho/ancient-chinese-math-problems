"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

"""
Suppose one is observing the mouth of a river from the southeast. Two poles are erected, one to the south and one to the north, separated by 9 zhang. A rope is stretched across the ground connecting them.
Standing 6 zhang west of the northern pole, one observes the southern bank of the river mouth, and the rope's northern end is 4 zhang 2 cun inward. Observing the northern bank, the inward distance from the previous observation point is 1 zhang 2 chi.
Then, moving further back to a position 13 zhang 5 chi west of the northern pole, one observes the southern bank of the river mouth aligning with the southern pole.
Question: how wide is the river mouth?

The procedure says: Multiply the distance from the second observation point to the pole by the inward distance of the rope. Divide this by the distance between the poles to get a preliminary result.
Subtract the distance from the first observation point to the pole from this result, and the remainder becomes the divisor.
Then subtract the distance from the first observation point to the pole from the second observation point to the pole, and multiply the remainder by the inward distance of the first observation point's observation of the northern bank. This becomes the dividend.
Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: *a* li.
"""

# 南北表相去九丈
表距 = 9

# 當北表之西卻行去表六丈
前去表 = 6

# 入索北端四丈二寸
入索 = 4 + Fraction(2, 10)

# 入前所望表里一丈二尺
入表里 = 1 + Fraction(2, 10)

# 卻後行去表一十三丈五尺
後去表 = 13 + Fraction(5, 10)

# 以後去表乘入索
後乘入索 = 後去表 * 入索

# 如表相去而一
初步結果 = Fraction(後乘入索, 表距)

# 所得，以前去表減之，餘以為法
法 = 初步結果 - 前去表

# 復以前去表減後去表
距差 = 後去表 - 前去表

# 餘以乘入所望表里為實
實 = 距差 * 入表里

# 實如法而一，得波口廣
波口廣 = Fraction(實, 法)

# Convert to li (1 zhang = 1/300 li)
a = 波口廣 / 300
"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1/10"""
