#今有大夫、不更、簪裹、上造、公士，凡五人，共獵得五鹿。欲以爵次分之，問︰各得幾何？

#荅曰：大夫得 a鹿 。不更得 b鹿 。簪裹得 c鹿 。上造得 d鹿 。公士得 e鹿 。

"""
Suppose there is Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi [official titles of varying ranks], in total 5 people.
They hunted together and caught 5 deer.
Dividing them according to their ranks, how much does each get?

The answer says: the Daifu gets *a* deer, the Bugeng gets *b* deer, the Zanniao gets *c* deer, the Shangzao gets *d* deer, the Gongshi gets *e* deer.
"""

# Place the shares
shares = [5, 4, 3, 2, 1]

# Take the sum of shares as divisor
divisor = sum(shares)

# Multiply the individual shares by the number of deer and divide by total to get the result
a, b, c, d, e = [Fraction(5 * i, divisor) for i in shares]
