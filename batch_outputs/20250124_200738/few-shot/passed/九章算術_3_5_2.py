"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

#----- content starts here -----
"""
Suppose there is a distribution of millet for officials: Daifu, Bugeng, Zanniao, Shangzao, and Gongshi, in total 5 people, with 15 dou of millet.
Now, one additional Daifu arrives, and he should also receive 5 dou.
The granary has no millet left, so it is desired to take millet from the others proportionally to their ranks.
Question: how much does each contribute?

The procedure says: Place the millet amounts (in hu and dou) that each originally receives, and distribute them evenly according to their ranks, forming a decreasing sequence.
Add the auxiliary amounts and include the 5 dou for the newly arrived Daifu, obtaining 20 as the divisor.
Multiply the 5 dou by the remaining amounts (not yet added), forming the dividend for each.
Perform the division to obtain the amount of dou each contributes.

The answer says: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

# 各置所稟粟斛斗數
稟粟 = [5, 4, 3, 2, 1]  # Original distribution in dou for Daifu, Bugeng, Zanniao, Shangzao, Gongshi

# 爵次均之，以為列衰
爵次 = 稟粟

# 副并而加後來大夫亦五斗，得二十以為法
法 = sum(爵次) + 5

# 以五斗乘未并者各自為實
實 = [5 * i for i in 爵次]

# 實如法得一斗
a, b, c, d, e = [Fraction(i, 法) for i in 實]#----- content ends here -----

"""
"""
