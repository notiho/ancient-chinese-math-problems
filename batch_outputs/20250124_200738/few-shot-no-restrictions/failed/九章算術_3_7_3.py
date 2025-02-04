"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：置爵數各自為衰，而返衰之，副并為法。以百錢乘未并者各自為實。實如法得一錢。
荅曰：大夫出 a錢 。不更出 b錢 。簪褭出 c錢 。上造出 d錢 。公士出 e錢 。
"""

#----- content starts here -----
"""
Suppose there are five individuals: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. 
Together, they contribute a total of 100 qian. 
It is desired that the higher-ranked individuals contribute less, and the lower-ranked individuals contribute more, in a gradually increasing manner.
Question: how much does each contribute?

The procedure for reverse ranking says: Arrange the ranks in decreasing order and let them multiply with each other. 
The moving rank becomes the fixed rank's reverse ranking.
The procedure says: Place the rank numbers, each as its own decreasing sequence, and reverse their ranking. 
Add the reversed ranks together to obtain the divisor.
Multiply the total amount (100 qian) by the unreversed ranks, each as its own dividend.
Divide the dividend by the divisor to obtain the contribution of each individual.

Answer: the Daifu contributes *a* qian, the Bugeng contributes *b* qian, the Zanniao contributes *c* qian, the Shangzao contributes *d* qian, and the Gongshi contributes *e* qian.
"""

from fractions import Fraction

# 列置爵數，各自為衰
爵數 = [5, 4, 3, 2, 1]  # Ranks in decreasing order

# 返衰之：令相乘，動者為不動者衰
返衰 = [1 / i for i in 爵數]

# 副并為法
法 = sum(返衰)

# 置總額百錢
總額 = 100

# 以百錢乘未并者，各自為實
實 = [總額 * i for i in 返衰]

# 實如法得一錢
a, b, c, d, e = [Fraction(i, 法) for i in 實]

# Output results
a, b, c, d, e#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
