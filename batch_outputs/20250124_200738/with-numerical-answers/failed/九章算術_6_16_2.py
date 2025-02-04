"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a(=2)斤 。次一尺， 重 b(=5/2)斤 。次一尺， 重 c(=3)斤 。次一尺， 重 d(=7/2)斤 。次一尺， 重 e(=4)斤
"""

#----- content starts here -----
"""
Suppose there is a golden rod, 5 chi in length.
Cutting off the base (first chi) weighs 4 jin, and cutting off the tip (last chi) weighs 2 jin.
Question: how much does each intermediate chi weigh?

The procedure says: Subtract the weight of the tip from the weight of the base, and the remainder is the rate of difference.
Then place the base weight, multiply it by the 4 intervals, and this becomes the first decreasing weight.
Place it again, subtracting the rate of difference each time, and each chi becomes its own decreasing weight.
Place the first decreasing weight below as the divisor.
Multiply the base weight of 4 jin by each decreasing weight, and each becomes its own dividend.
Divide the dividend by the divisor to obtain the weight of each chi.

Answer: The last chi weighs *a*(=2) jin. The next chi weighs *b*(=5/2) jin. The next chi weighs *c*(=3) jin. The next chi weighs *d*(=7/2) jin. The next chi weighs *e*(=4) jin.
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
衰列表 = [本重 - i * 差率 for i in range(長)]

# 副置下第一衰以為法
法 = 第一衰

# 以本重四斤遍乘列衰，各自為實
實列表 = [本重 * 衰 for 衰 in 衰列表]

# 實如法得一斤
重量列表 = [Fraction(實, 法) for 実 in 實列表]

# Assign weights to each chi
a = 重量列表[4]  # 2 jin
b = 重量列表[3]  # 5/2 jin
c = 重量列表[2]  # 3 jin
d = 重量列表[1]  # 7/2 jin
e = 重量列表[0]  # 4 jin#----- content ends here -----

"""
Code error: name '實' is not defined"""
