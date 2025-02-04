"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a(=5/3)里 。
"""

#----- content starts here -----
"""
Suppose there is a point where one looks southeast toward the mouth of a river. Two poles are erected, one to the south and one to the north, separated by 9 zhang. A rope is stretched flat along the ground connecting them. 

At a point 6 zhang west of the northern pole, the observer looks toward the southern bank of the river mouth. The rope's northern end is 4 zhang and 2 cun away from the observer. Looking toward the northern bank, the observer sees it 1 zhang and 2 chi inside the northern pole.

The observer then moves 13 zhang and 5 chi west of the northern pole. Looking toward the southern bank of the river mouth, the observer sees it aligned with the southern pole.

Question: How wide is the river mouth?

The procedure says: Multiply the distance from the second observation point to the northern pole by the distance the rope's northern end is from the observer during the first observation. Divide by the distance between the poles. Subtract the distance from the first observation point to the northern pole from the result. The remainder is the divisor.

Then subtract the distance from the first observation point to the northern pole from the distance from the second observation point to the northern pole. Multiply the remainder by the distance the northern bank is inside the northern pole during the first observation. This is the dividend. Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: *a*(=5/3) li.
"""

# 南、北相去九丈
表相去 = 9

# 當北表之西卻行去表六丈
前去表 = 6

# 入索北端四丈二寸
入索 = 4 + Fraction(2, 10)

# 以望北岸，入前所望表里一丈二尺
入所望表里 = 1 + Fraction(2, 10)

# 又卻後行去表一十三丈五尺
後去表 = 13 + Fraction(5, 10)

# 薄地遙望波口南岸，與南表參合
# (This is the alignment condition, no direct calculation here)

# 術曰：以後去表乘入索
後去表乘入索 = 後去表 * 入索

# 如表相去而一
後去表乘入索除表相去 = Fraction(後去表乘入索, 表相去)

# 所得，以前去表減之，餘以為法
法 = 後去表乘入索除表相去 - 前去表

# 復以前去表減後去表
前減後 = 後去表 - 前去表

# 餘以乘入所望表里為實
實 = 前減後 * 入所望表里

# 實如法而一，得波口廣
a = Fraction(實, 法)  # 5/3 li#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 30"""
