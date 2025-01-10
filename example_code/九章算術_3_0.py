#今有大夫、不更、簪裹、上造、公士，凡五人，共獵得五鹿。欲以爵次分之，問︰各得幾何？
#術曰：列置爵數，各自為衰，副并為法。以五鹿乘未并者，各自為實。實如法得一鹿。
#荅曰：大夫得 a鹿 。不更得 b鹿 。簪裹得 c鹿 。上造得 d鹿 。公士得 e鹿 。

"""
Suppose there is Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi [official titles of varying ranks], in total 5 people.
They hunted together and caught 5 deer.
Dividing them according to their ranks, how much does each get?

The procedure says: Place the numbers [corresponding to the] ranks in a line.
Each of them becomes on its own an [element in the] decreasing sequence.
In auxilliary, add them, giving the divisor.
Multiply the [numbers] that have not been added together by the 5 deer.
Each of them becomes on its own a dividend.
Do the division, obtaining the number of single deer [for each person].

The answer says: the Daifu gets *a* deer, the Bugeng gets *b* deer, the Zanniao gets *c* deer, the Shangzao gets *d* deer, the Gongshi gets *e* deer.
"""

# 列置爵數，各自為衰
爵數 = [5, 4, 3, 2, 1]

# 副并為法
法 = sum(爵數)

# 以五鹿乘未并者
爵數 = [5 * i for i in 爵數]

# 各自為實
實 = 爵數

# 實如法得一鹿
a, b, c, d, e = [Fraction(i, 法) for i in 實]
