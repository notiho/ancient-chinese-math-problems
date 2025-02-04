"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

"""
Suppose there is a golden rod, 5 chi in length.
Cutting off the base (first chi) weighs 4 jin.
Cutting off the tip (last chi) weighs 2 jin.
Question: how much does each of the intermediate chi weigh?

The procedure says: Subtract the weight of the tip from the weight of the base; the remainder is the rate of difference.
Next, place the base weight, and multiply it by 4 intervals, obtaining the first decreasing weight.
Place it again, subtracting the rate of difference each time, so that each chi has its own decreasing weight.
Place the first decreasing weight as the divisor.
Multiply the base weight (4 jin) by all the decreasing weights, obtaining the dividend for each chi.
Divide the dividend by the divisor, obtaining the weight of each chi.

Answer: The last chi weighs *a* jin. The next chi weighs *b* jin. The next chi weighs *c* jin. The next chi weighs *d* jin. The next chi weighs *e* jin.
"""

# 長五尺
總長 = 5

# 斬本一尺，重四斤
本重 = 4

# 斬末一尺，重二斤
末重 = 2

# 令末重減本重，餘即差率也
差率 = 本重 - 末重

# 又置本重，以四間乘之，為下第一衰
間數 = 總長 - 1  # 4 intervals between 5 chi
第一衰 = 本重 * 間數

# 副置，以差率減之，每尺各自為衰
列衰 = [本重 - 差率 * i for i in range(間數 + 1)]

# 副置下第一衰以為法
法 = 第一衰

# 以本重四斤遍乘列衰，各自為實
實 = [本重 * 衰 for 衰 in 列衰]

# 實如法得一斤
結果 = [Fraction(實值, 法) for 實值 in 實]

# Assign results to variables
a, b, c, d, e = 結果
"""
Variable 'a' has wrong value. Expected: 2, Actual: 1
Variable 'b' has wrong value. Expected: 5/2, Actual: 1/2
Variable 'c' has wrong value. Expected: 3, Actual: 0
Variable 'd' has wrong value. Expected: 7/2, Actual: -1/2
Variable 'e' has wrong value. Expected: 4, Actual: -1"""
