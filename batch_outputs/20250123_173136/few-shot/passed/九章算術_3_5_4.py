"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

"""
Suppose there is a distribution of millet for officials: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi, in total 5 people, with 15 dou of millet.
Now, an additional Daifu arrives later and is also to receive 5 dou.
The granary has no millet left, so the millet must be taken proportionally from the others based on their ranks.
Question: how much does each contribute?

The procedure says: Place the millet amounts (in hu and dou) that each was originally allocated, and divide them equally according to their ranks, forming a decreasing sequence.
Add the contributions of the additional Daifu (5 dou), obtaining 20 as the divisor.
Multiply 5 dou by the uncombined values for each person, forming the dividend.
Divide the dividend by the divisor to obtain the contribution of each person.

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

# Original millet allocation in dou
大夫稟 = 5
不更稟 = 4
簪裹稟 = 3
上造稟 = 2
公士稟 = 1

# Combine the original allocations into a list
稟粟 = [大夫稟, 不更稟, 簪裹稟, 上造稟, 公士稟]

# Add the additional Daifu's allocation (5 dou) to the total
法 = sum(稟粟) + 5

# Multiply 5 dou by each person's original allocation
實 = [5 * i for i in 稟粟]

# Divide each person's contribution by the total divisor
a, b, c, d, e = [Fraction(i, 法) for i in 實]
"""
"""
