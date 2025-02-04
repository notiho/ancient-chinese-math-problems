"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：置爵數各自為衰，而返衰之，副并為法。以百錢乘未并者各自為實。實如法得一錢。
荅曰：大夫出 a錢 。不更出 b錢 。簪褭出 c錢 。上造出 d錢 。公士出 e錢 。
"""

#----- content starts here -----
"""
Suppose there are five individuals: Daifu, Bugeng, Zanniao, Shangzao, and Gongshi. Together, they contribute a total of 100 qian. 
It is desired that the higher-ranked individuals contribute less, and the lower-ranked individuals contribute more, in a gradually increasing manner.
Question: how much does each contribute?

The procedure says: Arrange the ranks in descending order and let them multiply with each other. The moving rank becomes the fixed rank's weight.
The procedure further says: Place the rank numbers, each becoming its own weight, and reverse the weights. Add the reversed weights to obtain the divisor.
Multiply the total amount of 100 qian by the unreversed weights for each rank, obtaining the dividend for each. Divide the dividend by the divisor to find the contribution for each rank.

Answer: The Daifu contributes *a* qian, the Bugeng contributes *b* qian, the Zanniao contributes *c* qian, the Shangzao contributes *d* qian, and the Gongshi contributes *e* qian.
"""

from fractions import Fraction

# 列置爵數，各自為衰
爵數 = [5, 4, 3, 2, 1]  # Ranks in descending order

# 返衰之 (reverse the weights)
返衰 = [1 / x for x in 爵數]

# 副并為法 (sum the reversed weights to get the divisor)
法 = sum(返衰)

# 置百錢 (total contribution is 100 qian)
總錢 = 100

# 以百錢乘未并者各自為實 (multiply total by unreversed weights to get dividends)
實 = [總錢 * x for x in 爵數]

# 實如法得一錢 (divide each dividend by the divisor to get contributions)
contributions = [Fraction(x, 法) for x in 實]

# Assign contributions to each rank
a, b, c, d, e = contributions

# Output the results
a, b, c, d, e#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
