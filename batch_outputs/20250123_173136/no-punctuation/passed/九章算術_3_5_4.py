"""
今有稟粟大夫不更簪裹上造公士凡五人一十五斗今有大夫一人後來亦當稟五斗倉無粟欲以衰出之問各幾何
術曰各置所稟粟斛斗數爵次均之以為列衰副并而加後來大夫亦五斗得二十以為法以五斗乘未并者各自為實實如法得一斗
荅曰大夫出 a斗 不更出 b斗 簪褭出 c斗 上造出 d斗 公士出 e斗 
"""

"""
Suppose there is millet to be distributed among five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi.
In total, they have 15 dou of millet. Now, an additional Daifu arrives and should also receive 5 dou.
The granary is empty, so the millet must be redistributed according to rank.
Question: how much millet does each person contribute?

The procedure says: Place the millet amounts (in hu and dou) that each rank receives, and equalize them according to rank.
Use this as the sequence of decreasing weights.
Add the weights together and include the additional Daifu's 5 dou, obtaining 20 as the divisor.
Multiply the 5 dou by the unadded weights, and each becomes its own dividend.
Divide by the divisor, obtaining the amount of millet each contributes.

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

# 各置所稟粟斛斗數爵次均之以為列
爵數 = [5, 4, 3, 2, 1]  # The weights for each rank

# 副并而加後來大夫亦五斗，得二十以為法
法 = sum(爵數) + 5  # Adding the new Daifu's 5 dou

# 以五斗乘未并者
未并者 = [5 * i for i in 爵數]  # Multiply 5 dou by each weight

# 各自為實
實 = 未并者

# 實如法得一斗
a, b, c, d, e = [Fraction(i, 法) for i in 實]  # Divide each by the divisor to get the contribution

# Outputs
a, b, c, d, e
"""
"""
