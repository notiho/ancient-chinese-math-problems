"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

#----- content starts here -----
"""
Suppose there is a golden rod, 5 chi in length. 
The weight of the first chi (base) is 4 jin, and the weight of the last chi (tip) is 2 jin.
Question: What is the weight of each intermediate chi?

The procedure says: Subtract the weight of the tip from the weight of the base, and the remainder is the rate of difference.
Then, take the base weight and multiply it by 4 intervals (the number of chi minus 1), obtaining the first decreasing value.
Place the base weight and subtract the rate of difference repeatedly, obtaining the weight for each chi.
Finally, take the first decreasing value as the divisor, and multiply the base weight (4 jin) by each decreasing value to obtain the dividend.
Divide the dividend by the divisor to get the weight of each chi.

Answer: The last chi weighs *a* jin, the next chi weighs *b* jin, the next chi weighs *c* jin, the next chi weighs *d* jin, and the first chi weighs *e* jin.
"""

from fractions import Fraction

# 金箠長五尺
長度 = 5

# 本一尺重四斤
本重 = 4

# 末一尺重二斤
末重 = 2

# 差率 = 本重 - 末重
差率 = 本重 - 末重

# 第一衰 = 本重 * (長度 - 1)
第一衰 = 本重 * (長度 - 1)

# 計算每尺的權重
權重 = []
當前重 = 本重
for i in range(長度):
    權重.append(當前重)
    當前重 -= 差率 / (長度 - 1)

# 計算每尺的實際重量
法 = 第一衰
實 = [本重 * w for w in 權重]
結果 = [Fraction(s, 法) for s in 實]

# Assign results
e, d, c, b, a = 結果  # Assign weights from base to tip

# Output results
a, b, c, d, e#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
