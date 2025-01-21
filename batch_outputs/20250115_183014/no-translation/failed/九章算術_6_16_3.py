"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

"""

"""


from fractions import Fraction

# 金箠長五尺
總長 = 5

# 本一尺重四斤
本重 = 4

# 末一尺重二斤
末重 = 2

# 令末重減本重，餘即差率也
差率 = 本重 - 末重

# 置本重，以四間乘之，為下第一衰
間數 = 總長 - 1  # 四間
下第一衰 = 本重 * 間數

# 副置，以差率減之，每尺各自為衰
列衰 = [本重 - i * Fraction(差率, 間數) for i in range(間數 + 1)]

# 副置下第一衰以為法
法 = 下第一衰

# 以本重四斤遍乘列衰，各自為實
實 = [本重 * 衰 for 衰 in 列衰]

# 實如法得一斤
結果 = [Fraction(實[i], 法) for i in range(len(實))]

# 各尺重
a = 結果[4]  # 末一尺
b = 結果[3]  # 次一尺
c = 結果[2]  # 次一尺
d = 結果[1]  # 次一尺
e = 結果[0]  # 次一尺


"""

"""


"""
Variable 'a' has wrong value. Expected: 2, Actual: 1/2
Variable 'b' has wrong value. Expected: 5/2, Actual: 5/8
Variable 'c' has wrong value. Expected: 3, Actual: 3/4
Variable 'd' has wrong value. Expected: 7/2, Actual: 7/8
Variable 'e' has wrong value. Expected: 4, Actual: 1"""
