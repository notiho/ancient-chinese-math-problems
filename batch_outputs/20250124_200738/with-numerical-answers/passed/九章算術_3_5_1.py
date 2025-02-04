"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a(=5/4)斗 。不更出 b(=1)斗 。簪褭出 c(=3/4)斗 。上造出 d(=1/2)斗 。公士出 e(=1/4)斗 。
"""

#----- content starts here -----
"""
Suppose there is grain to be distributed among five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. 
In total, there are 15 dou of grain. 
Now, an additional Daifu arrives and is also to receive 5 dou of grain. 
The granary has no more grain, so it is desired to take it back from the others proportionally to their ranks.
Question: how much does each person contribute?

The procedure says: Place the amount of grain (in hu and dou) each person is to receive, and equalize it according to their ranks, forming the decreasing sequence.
Add the auxiliary values and include the additional Daifu's 5 dou, obtaining 20 as the divisor.
Multiply the 5 dou by the uncombined values, forming the dividends.
Divide the dividends by the divisor, obtaining the amount of dou each person contributes.

Answer: the Daifu contributes *a*(=5/4) dou, the Bugeng contributes *b*(=1) dou, the Zanniao contributes *c*(=3/4) dou, the Shangzao contributes *d*(=1/2) dou, and the Gongshi contributes *e*(=1/4) dou.
"""

# 各置所稟粟斛斗數 (initial grain distribution in dou)
稟粟 = [5, 4, 3, 2, 1]

# 爵次均之，以為列衰 (proportional ranks)
爵次 = 稟粟

# 副并而加後來大夫亦五斗，得二十以為法
法 = sum(爵次) + 5

# 以五斗乘未并者各自為實
未并者 = [5 * i for i in 爵次]

# 實如法得一斗
a, b, c, d, e = [Fraction(i, 法) for i in 未并者] # 5/4, 1, 3/4, 1/2, 1/4#----- content ends here -----

"""
"""
