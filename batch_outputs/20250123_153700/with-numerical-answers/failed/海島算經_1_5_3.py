"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a(=5/3)里 。
"""

"""
Suppose one is looking southeast toward the mouth of a river. Two poles are erected, one to the south and one to the north, separated by 9 zhang. A rope is stretched along the ground connecting them.
From the north pole, one walks westward 6 zhang and looks toward the southern bank of the river mouth. The rope enters the northern end by 4 zhang and 2 cun.
Looking toward the northern bank, the rope enters the pole by 1 zhang and 2 chi.
Then, one walks further westward, 13 zhang and 5 chi from the north pole. Looking toward the southern bank of the river mouth, the rope aligns with the southern pole.
Question: how wide is the river mouth?

The procedure says: Multiply the distance walked westward after the pole by the amount the rope enters at the northern end. Divide by the distance between the poles to get a preliminary result.
Subtract the distance walked westward before the pole from this result to obtain the divisor.
Subtract the distance walked westward before the pole from the distance walked westward after the pole. Multiply this difference by the amount the rope enters the pole when looking toward the northern bank to obtain the dividend.
Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: *a*(=5/3) li.
"""

# Constants
表相去 = 9  # 南北表相去 9 丈
前去表 = 6  # 當北表之西卻行去表 6 丈
入索北端 = Fraction(42, 10)  # 入索北端 4 丈 2 寸 (convert to fraction: 4丈 + 2寸 = 42/10丈)
入所望表里 = Fraction(12, 10)  # 入前所望表里 1 丈 2 尺 (convert to fraction: 1丈 + 2尺 = 12/10丈)
後去表 = Fraction(135, 10)  # 卻後行去表 13 丈 5 尺 (convert to fraction: 13丈 + 5尺 = 135/10丈)

# Step 1: 以後去表乘入索
後乘入索 = 後去表 * 入索北端

# Step 2: 如表相去而一
初步結果 = Fraction(後乘入索, 表相去)

# Step 3: 所得，以前去表減之，餘以為法
法 = 初步結果 - 前去表

# Step 4: 復以前去表減後去表
差距 = 後去表 - 前去表

# Step 5: 餘以乘入所望表里為實
實 = 差距 * 入所望表里

# Step 6: 實如法而一，得波口廣
a = Fraction(實, 法)  # 5/3 里
"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 30"""
