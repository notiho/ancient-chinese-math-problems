"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a(=5/3)里 。
"""

"""
Suppose there is a view of the mouth of a river to the southeast. Two poles are erected, one to the south and one to the north, with a distance of 9 zhang between them. A rope is stretched across the ground connecting them. 
Standing west of the northern pole, 6 zhang away from it, the observer looks across the ground to the southern bank of the river mouth. The rope enters the northern end by 4 zhang and 2 cun. 
Looking at the northern bank, the rope enters the previous pole by 1 zhang and 2 chi. 
The observer then steps back further, 13 zhang and 5 chi away from the pole. Looking across the ground to the southern bank of the river mouth, the rope aligns with the southern pole. 
Question: how wide is the river mouth?

The procedure says: Multiply the distance from the second position to the pole by the rope's entry at the northern end. Divide by the distance between the poles. Subtract the first position's distance from the pole from the result, and take the remainder as the divisor. 
Then subtract the second position's distance from the first position's distance, and multiply the result by the rope's entry at the previous pole to get the dividend. Divide the dividend by the divisor to obtain the width of the river mouth.

Answer: *a*(=5/3) li.
"""

# 立兩表南、北相去九丈
表相去 = 9

# 當北表之西卻行去表六丈
前去表 = 6

# 薄地遙望波口南岸，入索北端四丈二寸
入索北端 = 4 + Fraction(2, 10)

# 以望北岸，入前所望表里一丈二尺
入所望表里 = 1 + Fraction(2, 10)

# 又卻後行去表一十三丈五尺
後去表 = 13 + Fraction(5, 10)

# 薄地遙望波口南岸，與南表參合
# 求波口廣

# 術曰：以後去表乘入索
後去表乘入索 = 後去表 * 入索北端

# 如表相去而一
後去表乘入索除表相去 = Fraction(後去表乘入索, 表相去)

# 所得，以前去表減之，餘以為法
法 = 後去表乘入索除表相去 - 前去表

# 復以前去表減後去表
前減後 = 前去表 - 後去表

# 餘以乘入所望表里為實
實 = 前減後 * 入所望表里

# 實如法而一，得波口廣
波口廣 = Fraction(實, 法)

a = 波口廣 # 5/3 里
"""
Variable 'a' has wrong value. Expected: 5/3, Actual: -30"""
