"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a(=307/25)丈 ；山去表 b(=23/21)里 。
"""

#----- content starts here -----
"""
Suppose there is a pine tree growing on a mountain, and its height is unknown. Two poles are erected, both of equal height, 2 zhang. The distance between the two poles is 50 bu. The rear pole aligns with the front pole and the top of the pine tree when viewed from a specific position. 

From the front pole, one steps back 7 bu and 4 chi, and from there, the top of the pine tree aligns with the top of the pole. The base of the pine tree aligns with a point 2 chi 8 cun into the pole. 
From the rear pole, one steps back 8 bu and 5 chi, and from there, the top of the pine tree again aligns with the top of the pole.

Question: What is the height of the pine tree and the distance from the mountain to the poles?

The procedure says: Multiply the amount the pole is entered by the distance between the poles to get the dividend. Use the difference between the two step-back distances as the divisor. Divide, and add the height of the pole to get the height of the pine tree. 

To find the distance from the mountain to the poles: Take the distance between the poles, multiply it by the step-back distance from the front pole to get the dividend. Use the difference between the two step-back distances as the divisor. Divide to get the distance from the mountain to the poles.

Answer: The height of the pine tree is *a*(=307/25) zhang, and the distance from the mountain to the poles is *b*(=23/21) li.
"""

# 表高二丈
表高 = 2

# 前後相去五十步
表間 = 50

# 從前表卻行七步四尺
前表卻行 = 7 + Fraction(4, 10)

# 入表二尺八寸
入表 = Fraction(2, 10) + Fraction(8, 100)

# 從後表卻行八步五尺
後表卻行 = 8 + Fraction(5, 10)

# 相多為法
相多 = 後表卻行 - 前表卻行

# 求松高
# 以入表乘表間為實
實_松高 = 入表 * 表間

# 除之，加入表，即得松高
松高 = Fraction(實_松高, 相多) + 表高
a = 松高  # 307/25 zhang

# 求山去表
# 置表間，以前表卻行乘之為實
實_山去表 = 表間 * 前表卻行

# 除之，得山去表
山去表 = Fraction(實_山去表, 相多)
b = 山去表  # 23/21 li#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 162/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 3700/11"""
