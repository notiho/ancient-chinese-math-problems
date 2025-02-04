"""
今有稟粟大夫不更簪裹上造公士凡五人一十五斗今有大夫一人後來亦當稟五斗倉無粟欲以衰出之問各幾何
術曰各置所稟粟斛斗數爵次均之以為列衰副并而加後來大夫亦五斗得二十以為法以五斗乘未并者各自為實實如法得一斗
荅曰大夫出 a斗 不更出 b斗 簪褭出 c斗 上造出 d斗 公士出 e斗 
"""

"""
Suppose there is grain to be distributed among five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi.
They are to receive a total of 15 dou of grain.
Now, an additional Daifu arrives and is also to receive 5 dou of grain.
The granary is empty, so the grain must be redistributed proportionally according to their ranks.
Question: how much grain should each person contribute?

The procedure says: Place the amount of grain each person originally receives (in hu and dou) and the rank numbers in a line.
Equalize them and treat them as a sequence.
Add the new Daifu's 5 dou to the total, making 20 dou the divisor.
Multiply the 5 dou by the uncombined numbers, treating each as a dividend.
Perform the division to obtain the amount of grain each person contributes.

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

# 各置所稟粟斛斗數爵次均之以為列
爵數 = [5, 4, 3, 2, 1]  # 爵次 (ranks)
稟粟 = [5, 4, 3, 2, 1]  # 每人原本稟粟數 (in dou)

# 後來大夫亦五斗
後來大夫稟粟 = 5

# 副并而加後來大夫亦五斗，得二十以為法
法 = sum(稟粟) + 後來大夫稟粟

# 以五斗乘未并者，各自為實
實 = [後來大夫稟粟 * i for i in 稟粟]

# 實如法得一斗
a, b, c, d, e = [Fraction(i, 法) for i in 實]
"""
"""
