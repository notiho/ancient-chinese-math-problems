"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：置爵數各自為衰，而返衰之，副并為法。以百錢乘未并者各自為實。實如法得一錢。
荅曰：大夫出 a錢 。不更出 b錢 。簪褭出 c錢 。上造出 d錢 。公士出 e錢 。
"""

#----- content starts here -----
"""
Suppose there are five individuals: Daifu, Bugeng, Zanniao, Shangzao, and Gongshi. Together, they contribute 100 qian.
It is desired that the higher-ranked individuals contribute less, and the lower-ranked individuals contribute more, gradually increasing.

The procedure for reverse weighting says: Arrange the weights (ranks) and let them multiply with each other. The moving (changing) weight becomes the reverse of the stationary (unchanging) weight.
The procedure says: Place the rank numbers, each as its own weight, and reverse the weights. Add the reversed weights together to form the divisor. Multiply the total contribution (100 qian) by the unreversed weights, each as its own dividend. Divide the dividend by the divisor to obtain the individual contributions.

Answer: The Daifu contributes *a* qian, the Bugeng contributes *b* qian, the Zanniao contributes *c* qian, the Shangzao contributes *d* qian, and the Gongshi contributes *e* qian.
"""

from fractions import Fraction

# 列置爵數，各自為衰
爵數 = [5, 4, 3, 2, 1]

# 返衰之 (reverse the weights)
返衰 = [Fraction(1, x) for x in 爵數]

# 副并為法 (sum the reversed weights to form the divisor)
法 = sum(返衰)

# 以百錢乘未并者 (multiply the total contribution by unreversed weights)
總錢 = 100
實 = [總錢 * x for x in 返衰]

# 實如法得一錢 (divide each dividend by the divisor to get individual contributions)
a, b, c, d, e = [x / 法 for x in 實]

# Output the results
a, b, c, d, e#----- content ends here -----

"""
"""
