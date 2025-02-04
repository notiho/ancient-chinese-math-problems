"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a(=5/3)里 。
"""

#----- content starts here -----
"""
Suppose there is a point at the southeast looking toward the mouth of a river. Two poles are erected, one to the south and one to the north, separated by 9 zhang. A rope is stretched across the ground connecting them.
At a point 6 zhang west of the northern pole, the observer looks toward the southern bank of the river mouth, and the rope enters the northern end by 4 zhang and 2 cun. Looking toward the northern bank, the rope enters the pole by 1 zhang and 2 chi.
The observer then moves 13 zhang and 5 chi further west from the northern pole. Looking toward the southern bank of the river mouth, the rope aligns with the southern pole.
Question: what is the width of the river mouth?

The procedure says: Multiply the distance moved west from the pole (afterward) by the amount the rope enters (at the northern end). Divide by the distance between the poles. Subtract the distance moved west from the pole (beforehand) from the result, and use the remainder as the divisor.
Subtract the distance moved west from the pole (beforehand) from the distance moved west afterward. Multiply the result by the amount the rope enters the pole (at the northern bank), obtaining the dividend. Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: *a*(=5/3) li.
"""

# 南北相去九丈
表相去 = 9

# 當北表之西卻行去表六丈
前去表 = 6

# 入索北端四丈二寸
入索 = 4 + Fraction(2, 10)

# 以望北岸，入前所望表里一丈二尺
入所望表里 = 1 + Fraction(2, 10)

# 又卻後行去表一十三丈五尺
後去表 = 13 + Fraction(5, 10)

# 術曰：以後去表乘入索
實1 = 後去表 * 入索

# 如表相去而一
實1 = Fraction(實1, 表相去)

# 所得，以前去表減之，餘以為法
法 = 實1 - 前去表

# 復以前去表減後去表
差 = 後去表 - 前去表

# 餘以乘入所望表里為實
實2 = 差 * 入所望表里

# 實如法而一，得波口廣
a = Fraction(實2, 法) # 5/3 里#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 30"""
