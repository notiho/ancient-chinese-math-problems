"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a(=2)斤 。次一尺， 重 b(=5/2)斤 。次一尺， 重 c(=3)斤 。次一尺， 重 d(=7/2)斤 。次一尺， 重 e(=4)斤
"""

"""
Suppose there is a golden rod, 5 chi in length.
Cutting off the base (first chi) weighs 4 jin, and cutting off the tip (last chi) weighs 2 jin.
Question: how much does each intermediate chi weigh?

The procedure says: Subtract the weight of the tip from the weight of the base; the remainder is the rate of difference.
Then place the base weight, and multiply it by the 4 intervals, obtaining the first decreasing value.
Place it again, and subtract the rate of difference from it, making each chi its own decreasing value.
Place the first decreasing value as the divisor.
Multiply the base weight of 4 jin by all the decreasing values, making each its own dividend.
Divide the dividend by the divisor, obtaining the weight of each chi.

Answer: The last chi weighs *a*(=2) jin. The next chi weighs *b*(=5/2) jin. The next chi weighs *c*(=3) jin. The next chi weighs *d*(=7/2) jin. The next chi weighs *e*(=4) jin.
"""

# 長五尺
長度 = 5

# 斬本一尺，重四斤
本重 = 4

# 斬末一尺，重二斤
末重 = 2

# 令末重減本重，餘即差率也
差率 = 本重 - 末重

# 又置本重，以四間乘之，為下第一衰
間數 = 長度 - 1
下第一衰 = 本重 * 間數

# 副置，以差率減之，每尺各自為衰
列衰 = [本重 - i * 差率 for i in range(間數 + 1)]

# 副置下第一衰以為法
法 = 下第一衰

# 以本重四斤遍乘列衰，各自為實
實 = [本重 * 衰 for 衰 in 列衰]

# 實如法得一斤
重量 = [Fraction(實值, 法) for 實值 in 實]

# Assign weights to each chi
a, b, c, d, e = 重量 # 2, 5/2, 3, 7/2, 4
"""
Variable 'a' has wrong value. Expected: 2, Actual: 1
Variable 'b' has wrong value. Expected: 5/2, Actual: 1/2
Variable 'c' has wrong value. Expected: 3, Actual: 0
Variable 'd' has wrong value. Expected: 7/2, Actual: -1/2
Variable 'e' has wrong value. Expected: 4, Actual: -1"""
