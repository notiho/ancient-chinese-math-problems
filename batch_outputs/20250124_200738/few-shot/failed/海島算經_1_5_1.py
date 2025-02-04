"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a point at the southeast looking toward the mouth of a river. Two poles are erected, one to the south and one to the north, with a distance of 9 zhang between them. A rope is stretched along the ground connecting the two poles.
From the northern pole, walk westward 6 zhang away from the pole. From this position, look toward the southern bank of the river mouth, and the rope enters the northern end by 4 zhang and 2 cun. Then, look toward the northern bank, and the rope enters the previous pole by 1 zhang and 2 chi.
Next, walk further westward, 13 zhang and 5 chi away from the northern pole. From this position, look toward the southern bank of the river mouth, and the line aligns with the southern pole.
Question: How wide is the river mouth?

The procedure says: Multiply the later distance from the pole by the rope's entry. Divide this by the distance between the poles to get a value. Subtract the earlier distance from the pole from this value, and the remainder becomes the divisor.
Then, subtract the earlier distance from the later distance, and multiply the remainder by the rope's earlier entry to get the dividend. Divide the dividend by the divisor to get the width of the river mouth.

Answer: The width of the river mouth is *a* li.
"""

# Constants
表相去 = 9  # 南北兩表相距 9 丈
後去表 = 13 + Fraction(5, 10)  # 後去表 13 丈 5 尺
前去表 = 6  # 前去表 6 丈
入索 = 4 + Fraction(2, 10)  # 入索北端 4 丈 2 寸
入所望表里 = 1 + Fraction(2, 10)  # 入前所望表里 1 丈 2 尺

# Step 1: 以後去表乘入索，如表相去而一
值 = (後去表 * 入索) / 表相去

# Step 2: 所得，以前去表減之，餘以為法
法 = 值 - 前去表

# Step 3: 復以前去表減後去表，餘以乘入所望表里為實
實 = (後去表 - 前去表) * 入所望表里

# Step 4: 實如法而一，得波口廣
波口廣 = 實 / 法

# Convert to li (1 丈 = 1/300 里)
a = 波口廣 / 300#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1/10"""
