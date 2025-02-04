"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

"""
Suppose there is a distribution of millet for officials: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi, in total 5 people, receiving 15 dou of millet.
Now, an additional Daifu arrives and is also supposed to receive 5 dou. However, the granary has no millet left.
It is desired to distribute the required millet proportionally according to their ranks.
Question: how much does each contribute?

The procedure says: Place the millet amounts (in hu and dou) that each person originally receives, and distribute them evenly according to their ranks, forming a decreasing sequence.
Add the auxiliary amounts and include the 5 dou for the newly arrived Daifu, obtaining 20 as the divisor.
Multiply the 5 dou by the uncombined amounts, forming the dividend for each.
Divide the dividend by the divisor to obtain the amount each contributes.

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

# Original millet distribution (in dou)
大夫 = 5
不更 = 4
簪裹 = 3
上造 = 2
公士 = 1

# Add the new Daifu's 5 dou
新增大夫 = 5

# Combine all contributions to form the divisor (法)
法 = 大夫 + 不更 + 簪裹 + 上造 + 公士 + 新增大夫

# Calculate the dividend (實) for each rank
大夫實 = 新增大夫 * 大夫
不更實 = 新增大夫 * 不更
簪裹實 = 新增大夫 * 簪裹
上造實 = 新增大夫 * 上造
公士實 = 新增大夫 * 公士

# Divide each dividend by the divisor to get the contribution
a = Fraction(大夫實, 法)
b = Fraction(不更實, 法)
c = Fraction(簪裹實, 法)
d = Fraction(上造實, 法)
e = Fraction(公士實, 法)
"""
"""
