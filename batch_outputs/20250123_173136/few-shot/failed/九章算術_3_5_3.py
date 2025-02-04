"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

"""
Suppose there is grain to be distributed among five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. 
In total, they have 15 dou of grain. Now, one additional Daifu arrives, and he is also to receive 5 dou. 
However, the granary has no more grain, so the grain must be taken back proportionally according to their ranks.
Question: how much does each person return?

The procedure says: Place the amount of grain (in hu and dou) that each person originally received.
Distribute it evenly according to their ranks, forming a sequence of proportions.
Add the additional Daifu's 5 dou to the total, making 20 dou as the divisor.
Multiply 5 dou by the uncombined values for each person, forming the dividend.
Divide the dividend by the divisor to obtain the amount each person must return.

Answer: the Daifu returns *a* dou, the Bugeng returns *b* dou, the Zanniao returns *c* dou, the Shangzao returns *d* dou, and the Gongshi returns *e* dou.
"""

# 各置所稟粟斛斗數
稟粟 = [5, 4, 3, 2, 1]  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi

# 爵次均之，以為列衰
列衰 = 稟粟

# 副并而加後來大夫亦五斗，得二十以為法
法 = sum(列衰) + 5

# 以五斗乘未并者各自為實
未并者 = 列衰
實 = [5 * i for i in 未并者]

# 實如法得一斗
a, b, c, d, e = [Fraction(i, 法) for i in 实]
"""
Code error: name '实' is not defined"""
