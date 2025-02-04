"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

#----- content starts here -----
"""
Suppose one is observing the mouth of a river from the southeast. Two poles are erected, one to the south and one to the north, separated by 9 zhang. A rope is stretched across the ground connecting them.
From the northern pole, walk westward 6 zhang away from the pole. From this position, observe the southern bank of the river mouth, and the rope enters the northern end by 4 zhang and 2 cun. Then, observe the northern bank of the river mouth, and the rope enters the pole by 1 zhang and 2 chi.
Next, walk further westward, 13 zhang and 5 chi away from the pole. From this position, observe the southern bank of the river mouth, and the view aligns with the southern pole.
Question: what is the width of the river mouth?

The procedure says: Multiply the later distance from the pole by the rope entry. Treat the distance between the poles as 1. Subtract the earlier distance from the pole from the result, and the remainder becomes the divisor.
Then subtract the earlier distance from the later distance, and multiply the remainder by the earlier rope entry to obtain the dividend. Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: *a* li.
"""

# Constants and conversions
丈_to_尺 = 10  # 1 丈 = 10 尺
尺_to_寸 = 10  # 1 尺 = 10 寸
尺_to_里 = 3000  # 1 里 = 3000 尺

# Input values
表相去 = 9  # 南北相去 9 丈
表相去_尺 = 表相去 * 丈_to_尺

前去表 = 6  # 前去表 6 丈
前去表_尺 = 前去表 * 丈_to_尺

入索 = 4 + Fraction(2, 尺_to_寸)  # 入索北端 4 丈 2 寸
入索_尺 = 入索 * 丈_to_尺

入所望表里 = 1 * 丈_to_尺 + 2  # 入前所望表里 1 丈 2 尺

後去表 = 13 + Fraction(5, 丈_to_尺)  # 後去表 13 丈 5 尺
後去表_尺 = 後去表 * 丈_to_尺

# Procedure
# 以後去表乘入索
後乘入索 = 後去表_尺 * 入索_尺

# 如表相去而一
表相去_一 = 表相去_尺

# 所得，以前去表減之，餘以為法
法 = 後乘入索 - 前去表_尺

# 復以前去表減後去表
距離差 = 後去表_尺 - 前去表_尺

# 餘以乘入所望表里為實
實 = 距離差 * 入所望表里

# 實如法而一，得波口廣
波口廣_尺 = Fraction(實, 法)

# Convert to li
a = 波口廣_尺 / 尺_to_里#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1/18700"""
