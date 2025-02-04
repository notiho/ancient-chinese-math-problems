"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

#----- content starts here -----
"""
Suppose there is a golden rod, 5 chi long.
When cutting the base (first chi), it weighs 4 jin.
When cutting the tip (last chi), it weighs 2 jin.
Question: how much does each intermediate chi weigh?

The procedure says:
Let the weight of the tip be subtracted from the weight of the base; the remainder is the rate of difference.
Place the base weight, and multiply it by 4 intervals, obtaining the first decreasing value.
Place it again, subtracting the rate of difference each time, so that each chi has its own decreasing value.
Place the first decreasing value as the divisor.
Multiply the base weight (4 jin) by all the decreasing values, obtaining the dividend for each chi.
Divide the dividend by the divisor, obtaining the weight of each chi.

Answer: the tip weighs *a* jin, the next chi weighs *b* jin, the next chi weighs *c* jin, the next chi weighs *d* jin, and the base weighs *e* jin.
"""

from fractions import Fraction

# 長五尺
長 = 5

# 斬本一尺，重四斤
本重 = 4

# 斬末一尺，重二斤
末重 = 2

# 令末重減本重，餘即差率也
差率 = 本重 - 末重

# 置本重，以四間乘之，為下第一衰
下第一衰 = 本重 * (長 - 1)

# 副置，以差率減之，每尺各自為衰
列衰 = [本重 - i * 差率 for i in range(長)]

# 副置下第一衰以為法
法 = 下第一衰

# 以本重四斤遍乘列衰，各自為實
實 = [本重 * 衰 for 衰 in 列衰]

# 實如法得一斤
weights = [Fraction(實[i], 法) for i in range(長)]

# Assign weights to each chi
e, d, c, b, a = weights  # From base to tip#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: -1
Variable 'b' has wrong value. Expected: 5/2, Actual: -1/2
Variable 'c' has wrong value. Expected: 3, Actual: 0
Variable 'd' has wrong value. Expected: 7/2, Actual: 1/2
Variable 'e' has wrong value. Expected: 4, Actual: 1"""
