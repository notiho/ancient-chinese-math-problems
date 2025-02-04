"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

#----- content starts here -----
"""
Suppose there is a pine tree growing on a mountain, and its height is unknown.
Two poles of equal height, 2 zhang each, are erected. The distance between the two poles is 50 bu.
The rear pole is aligned with the front pole and the pine tree.
From the front pole, one walks backward 7 bu and 4 chi, and looks at the top of the pine tree, aligning it with the top of the pole.
Then, looking at the base of the pine tree, the line of sight enters the pole by 2 chi and 8 cun.
From the rear pole, one walks backward 8 bu and 5 chi, and again looks at the top of the pine tree, aligning it with the top of the pole.
Question: What are the height of the pine tree and the distance from the mountain to the poles?

The procedure says: Multiply the amount the line of sight enters the pole by the distance between the poles to get the dividend.
The difference between the backward walking distances is the divisor. Divide the dividend by the divisor, and add the height of the pole to get the height of the pine tree.
To find the distance from the mountain to the poles: Take the distance between the poles, and multiply it by the backward walking distance from the front pole to get the dividend.
The difference between the backward walking distances is the divisor. Divide the dividend by the divisor to get the distance from the mountain to the poles.

Answer: The height of the pine tree is *a* zhang, and the distance from the mountain to the poles is *b* li.
"""

# 表高二丈
表高 = 2

# 前後表相去五十步
表間 = 50

# 前表卻行七步四尺
前表卻行 = 7 + Fraction(4, 10)

# 入表二尺八寸
入表 = 2 + Fraction(8, 10)

# 後表卻行八步五尺
後表卻行 = 8 + Fraction(5, 10)

# 相多為法 (difference between backward walking distances)
法 = 後表卻行 - 前表卻行

# 以入表乘表間為實 (calculate dividend for pine tree height)
實_松高 = 入表 * 表間

# 松高 = 實 / 法 + 表高
松高 = Fraction(實_松高, 法) + 表高
a = 松高

# 以表間乘前表卻行為實 (calculate dividend for mountain distance)
實_山距 = 表間 * 前表卻行

# 山去表 = 實 / 法
山去表 = Fraction(實_山距, 法)
b = 山去表#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 1422/11
Variable 'b' has wrong value. Expected: 23/21, Actual: 3700/11"""
