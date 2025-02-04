"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

#----- content starts here -----
"""
Suppose there is millet to be distributed among five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi.
In total, they are to receive 15 dou. Now, an additional Daifu arrives and is also to receive 5 dou.
The granary has no millet, so it is desired to take millet from the original shares proportionally according to their ranks.
Question: how much does each contribute?

The procedure says: Place the millet each person is to receive (in hu and dou) and balance it according to their ranks, forming a decreasing sequence.
Add the auxiliary amounts, including the 5 dou for the newly arrived Daifu, obtaining 20 as the divisor.
Multiply the 5 dou by the uncombined amounts, forming the dividend for each.
Divide the dividend by the divisor to obtain the amount each person contributes.

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

# 各置所稟粟斛斗數
稟粟 = [5, 4, 3, 2, 1]  # The original shares in dou for Daifu, Bugeng, Zanniao, Shangzao, and Gongshi

# 爵次均之，以為列衰
列衰 = 稟粟

# 副并而加後來大夫亦五斗，得二十以為法
法 = sum(列衰) + 5

# 以五斗乘未并者各自為實
後來大夫稟粟 = 5
實 = [後來大夫稟粟 * i for i in 列衰]

# 實如法得一斗
a, b, c, d, e = [Fraction(i, 法) for i in 實]#----- content ends here -----

"""
"""
