"""
今有稟粟大夫不更簪裹上造公士凡五人一十五斗今有大夫一人後來亦當稟五斗倉無粟欲以衰出之問各幾何
術曰各置所稟粟斛斗數爵次均之以為列衰副并而加後來大夫亦五斗得二十以為法以五斗乘未并者各自為實實如法得一斗
荅曰大夫出 a斗 不更出 b斗 簪褭出 c斗 上造出 d斗 公士出 e斗 
"""

"""
Suppose there is a distribution of millet for five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. 
In total, they have 15 dou of millet. Now, a new Daifu arrives and is also supposed to receive 5 dou. 
However, the granary is empty, so the millet must be redistributed proportionally according to their ranks.
Question: how much does each person contribute?

The procedure says: Place the millet amounts (in hu and dou) that each rank receives in a line.
Equalize them according to their ranks, forming a sequence of decreasing proportions.
Add the new Daifu's 5 dou to the total, making 20 dou the divisor.
Multiply the 5 dou by the remaining proportions, forming the dividends.
Divide each dividend by the divisor to obtain the amount each contributes.

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

# 各置所稟粟斛斗數爵次均之，以為列
爵數 = [5, 4, 3, 2, 1]  # Ranks of Daifu, Bugeng, Zanniao, Shangzao, Gongshi

# 後來大夫亦五斗
後來大夫 = 5

# 副并而加後來大夫亦五斗，得二十以為法
法 = sum(爵數) + 後來大夫

# 以五斗乘未并者，各自為實
實 = [後來大夫 * i for i in 爵數]

# 實如法得一斗
a, b, c, d, e = [Fraction(i, 法) for i in 實]
"""
"""
