"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

"""
Suppose there is a golden rod, 5 chi long.
Cutting off the base (first chi) weighs 4 jin, and cutting off the tip (last chi) weighs 2 jin.
Question: how much does each intermediate chi weigh?

The procedure says: Subtract the weight of the tip from the weight of the base; the remainder is the rate of difference.
Then place the base weight, multiply it by the 4 intervals, and this becomes the first weight in the decreasing sequence.
Place it again, subtract the rate of difference from it, and each chi becomes its own weight in the sequence.
Place the first weight in the sequence as the divisor.
Multiply the base weight of 4 jin by the sequence of weights, and each becomes its own dividend.
Divide the dividend by the divisor to obtain the weight of each chi.

Answer: The last chi weighs *a* jin, the next chi weighs *b* jin, the next chi weighs *c* jin, the next chi weighs *d* jin, and the first chi weighs *e* jin.
"""

# 長五尺
長 = 5

# 斬本一尺，重四斤
本重 = 4

# 斬末一尺，重二斤
末重 = 2

# 令末重減本重，餘即差率也
差率 = 本重 - 末重

# 又置本重，以四間乘之，為下第一衰
第一衰 = 本重 * (長 - 1)

# 副置，以差率減之，每尺各自為衰
衰列 = [本重 - i * 差率 for i in range(長)]

# 副置下第一衰以為法
法 = 第一衰

# 以本重四斤遍乘列衰，各自為實
實列 = [本重 * 衰 for 衰 in 衰列]

# 實如法得一斤
結果 = [Fraction(實, 法) for 実 in 實列]

# Assign results to variables
e, d, c, b, a = 結果
"""
Code error: name '實' is not defined"""
