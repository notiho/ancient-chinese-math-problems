"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a(=5/4)斗 。不更出 b(=1)斗 。簪褭出 c(=3/4)斗 。上造出 d(=1/2)斗 。公士出 e(=1/4)斗 。
"""

"""
Suppose there is grain to be distributed among five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. 
In total, they are to receive 15 dou. 
Now, an additional Daifu arrives and is also to receive 5 dou. 
The granary is empty, so it is desired to take the grain back from the original five people in proportion to their ranks.
Question: how much does each person return?

The procedure says: Place the amount of grain (in hu and dou) each person was to receive, and equalize it according to their ranks, forming a decreasing sequence. 
Add the auxiliary values and include the additional Daifu's 5 dou, obtaining 20 as the divisor. 
Multiply 5 dou by the uncombined values, forming the dividends. 
Divide the dividends by the divisor to obtain the amount of dou each person returns.

Answer: the Daifu returns *a*(=5/4) dou, the Bugeng returns *b*(=1) dou, the Zanniao returns *c*(=3/4) dou, the Shangzao returns *d*(=1/2) dou, and the Gongshi returns *e*(=1/4) dou.
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
a, b, c, d, e = [Fraction(i, 法) for i in 實]  # 5/4, 1, 3/4, 1/2, 1/4
"""
"""
