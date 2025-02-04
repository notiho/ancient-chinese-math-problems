"""
今有金箠長五尺斬本一尺重四斤斬末一尺重二斤問次一尺各重幾何
術曰令末重減本重餘即差率也又置本重以四間乘之為下第一衰副置以差率減之每尺各自為衰副置下第一衰以為法以本重四斤遍乘列衰各自為實實如法得一斤
荅曰末一尺重 a斤 次一尺 重 b斤 次一尺 重 c斤 次一尺 重 d斤 次一尺 重 e斤
"""

"""
Suppose there is a golden rod 5 chi long. 
The base (first chi) weighs 4 jin, and the tip (last chi) weighs 2 jin.
Question: how much does each intermediate chi weigh?

The procedure says: Subtract the weight of the tip from the weight of the base. The remainder is the rate of difference.
Then place the weight of the base, multiply it by 4 intervals, and this becomes the first divisor.
For each chi, subtract the rate of difference from the previous weight. Each chi becomes its own decreasing sequence.
Place the first divisor as the overall divisor.
Multiply the base weight (4 jin) by the total number of chi, and distribute it across the sequence. Each chi becomes its own dividend.
Divide each dividend by the divisor to obtain the weight of each chi.

The answer says: the last chi weighs *a* jin, the second-to-last chi weighs *b* jin, the third-to-last chi weighs *c* jin, the fourth-to-last chi weighs *d* jin, and the first chi weighs *e* jin.
"""

# 金箠長五尺
長度 = 5

# 本一尺重四斤
本重 = 4

# 末一尺重二斤
末重 = 2

# 差率 = 本重 - 末重
差率 = 本重 - 末重

# 下第一衰副置 = 本重 * (長度 - 1)
下第一衰副置 = 本重 * (長度 - 1)

# 每尺各自為衰副置
衰副置 = [本重 - i * 差率 for i in range(長度)]

# 下第一衰以為法
法 = 下第一衰副置

# 以本重遍乘列衰各自為實
實 = [本重 * 長度 * i for i in 衰副置]

# 實如法得一斤
weights = [Fraction(i, 法) for i in 實]

# Assign weights to each chi
e, d, c, b, a = weights  # From base to tip
"""
Variable 'a' has wrong value. Expected: 2, Actual: -5
Variable 'b' has wrong value. Expected: 5/2, Actual: -5/2
Variable 'c' has wrong value. Expected: 3, Actual: 0
Variable 'd' has wrong value. Expected: 7/2, Actual: 5/2
Variable 'e' has wrong value. Expected: 4, Actual: 5"""
