"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：置爵數各自為衰，而返衰之，副并為法。以百錢乘未并者各自為實。實如法得一錢。
荅曰：大夫出 a錢 。不更出 b錢 。簪褭出 c錢 。上造出 d錢 。公士出 e錢 。
"""

#----- content starts here -----
"""
Suppose there are five people: Daifu, Bugeng, Zanniao, Shangzao, and Gongshi. Together, they contribute 100 qian.
It is desired that the higher-ranked officials contribute less, and the lower-ranked officials contribute more, in a gradually increasing manner.
Question: how much does each contribute?

The reverse-decreasing procedure says: Arrange the ranks in decreasing order and let them multiply with each other. The moving one becomes the non-moving one’s reverse-decreasing rank.
The procedure says: Place the rank numbers, each becoming its own decreasing rank, and reverse-decrease them. Add the auxiliary values to obtain the divisor. Multiply the 100 qian by the unadded values, each becoming its own dividend. Divide the dividends by the divisor to obtain the contributions.

Answer: The Daifu contributes *a* qian, the Bugeng contributes *b* qian, the Zanniao contributes *c* qian, the Shangzao contributes *d* qian, and the Gongshi contributes *e* qian.
"""

from fractions import Fraction

# 列置爵數，各自為衰
爵數 = [5, 4, 3, 2, 1]  # Ranks in decreasing order

# 返衰術：令相乘，動者為不動者衰
返衰 = [1, 5, 20, 60, 120]  # Reverse-decreasing ranks (calculated as factorial-like)

# 副并為法
法 = sum(返衰)

# 置百錢
總錢 = 100

# 以百錢乘未并者，各自為實
實 = [總錢 * i for i in 返衰]

# 實如法得一錢
a, b, c, d, e = [Fraction(i, 法) for i in 實]

# Output the results
a, b, c, d, e  # Contributions of Daifu, Bugeng, Zanniao, Shangzao, and Gongshi respectively#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1200/137, Actual: 50/103
Variable 'b' has wrong value. Expected: 1500/137, Actual: 250/103
Variable 'c' has wrong value. Expected: 2000/137, Actual: 1000/103
Variable 'd' has wrong value. Expected: 3000/137, Actual: 3000/103
Variable 'e' has wrong value. Expected: 6000/137, Actual: 6000/103"""
