"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a(=307/25)丈 ；山去表 b(=23/21)里 。
"""

#----- content starts here -----
"""
Suppose there is a pine tree growing on a mountain, and its height is unknown. Two poles of equal height, 2 zhang each, are erected, with a distance of 50 bu between them. The rear pole is aligned with the front pole and the top of the pine tree. From the front pole, one retreats 7 bu and 4 chi, and from there, looking at the top of the pine tree aligns with the top of the front pole. Then, looking at the base of the pine tree, the line of sight enters the front pole by 2 chi and 8 cun. Similarly, from the rear pole, one retreats 8 bu and 5 chi, and from there, looking at the top of the pine tree aligns with the top of the rear pole. 

Question: What are the height of the pine tree and the distance from the mountain to the poles?

The procedure says: To find the height of the pine tree, multiply the amount the line of sight enters the pole by the distance between the poles. Use the difference between the retreat distances as the divisor. Divide the product by the divisor and add the height of the pole to obtain the height of the pine tree. 

To find the distance from the mountain to the poles: Take the distance between the poles and multiply it by the retreat distance from the front pole. Use the difference between the retreat distances as the divisor. Divide the product by the divisor to obtain the distance from the mountain to the poles.

Answer: The height of the pine tree is *a*(=307/25) zhang, and the distance from the mountain to the poles is *b*(=23/21) li.
"""

# 表高
表高 = 2  # 丈

# 表間
表間 = 50  # 步

# 前表卻行
前表卻行 = 7 + Fraction(4, 10)  # 7步4尺 = 7.4步

# 入表
入表 = Fraction(2, 10) + Fraction(8, 100)  # 2尺8寸 = 0.28步

# 後表卻行
後表卻行 = 8 + Fraction(5, 10)  # 8步5尺 = 8.5步

# 相多為法
相多 = 後表卻行 - 前表卻行

# 以入表乘表間為實
實_松高 = 入表 * 表間

# 松高
松高 = Fraction(實_松高, 相多) + 表高
a = 松高  # 307/25 丈

# 置表間，以前表卻行乘之為實
實_山去表 = 表間 * 前表卻行

# 山去表
山去表 = Fraction(實_山去表, 相多)
b = 山去表  # 23/21 里#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 162/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 3700/11"""
