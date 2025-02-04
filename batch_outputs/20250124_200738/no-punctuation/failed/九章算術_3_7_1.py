"""
今有大夫不更簪褭上造公士凡五人共出百錢欲令高爵出少以次漸多問各幾何
返衰術曰列置衰而令相乘動者為不動者衰術曰置爵數各自為衰而返衰之副并為法以百錢乘未并者各自為實實如法得一錢
荅曰大夫出 a錢 不更出 b錢 簪褭出 c錢 上造出 d錢 公士出 e錢 
"""

#----- content starts here -----
"""
Suppose there are five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi.
Together, they contribute 100 qian. It is desired that the higher-ranked officials contribute less, and the lower-ranked officials contribute more, gradually increasing.

The procedure for reverse weighting says: Arrange the weights (ranks) and let them multiply such that the active ones become the inactive ones.
The procedure for weighting says: Place the rank numbers, each becoming its own weight.
Reverse the weights, and in auxiliary, add them, giving the divisor.
Multiply the 100 qian by the unadded ones, each becoming its own dividend.
Do the division, obtaining the number of qian for each person.

The answer says: the Daifu contributes *a* qian, the Bugeng contributes *b* qian, the Zanniao contributes *c* qian, the Shangzao contributes *d* qian, and the Gongshi contributes *e* qian.
"""

# 列置爵數，各自為衰
爵數 = [5, 4, 3, 2, 1]

# 返衰之
返衰 = list(reversed(爵數))

# 副并為法
法 = sum(返衰)

# 以百錢乘未并者
總錢 = 100
實 = [總錢 * i for i in 返衰]

# 各自為實，實如法得一錢
a, b, c, d, e = [Fraction(i, 法) for i in 实]#----- content ends here -----

"""
Code error: name '实' is not defined"""
