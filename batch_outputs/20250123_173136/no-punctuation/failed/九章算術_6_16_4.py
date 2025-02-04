"""
今有金箠長五尺斬本一尺重四斤斬末一尺重二斤問次一尺各重幾何
術曰令末重減本重餘即差率也又置本重以四間乘之為下第一衰副置以差率減之每尺各自為衰副置下第一衰以為法以本重四斤遍乘列衰各自為實實如法得一斤
荅曰末一尺重 a斤 次一尺 重 b斤 次一尺 重 c斤 次一尺 重 d斤 次一尺 重 e斤
"""

"""
Suppose there is a golden rod 5 chi long. 
The base (first chi) weighs 4 jin, and the tip (last chi) weighs 2 jin.
Question: how much does each intermediate chi weigh?

The procedure says:
Let the weight of the tip be subtracted from the weight of the base, and the remainder is the rate of difference.
Also, place the base weight, multiply it by 4 intervals (the number of chi between the base and the tip), and this becomes the first divisor.
For each chi, subtract the rate of difference from the previous weight, and each chi becomes its own term in the sequence.
Place the first divisor as the denominator.
Multiply the base weight (4 jin) by the entire sequence of terms, and each becomes its own dividend.
Perform the division, and obtain the weight of each chi.

The answer says: the last chi weighs *a* jin, the next chi weighs *b* jin, the next chi weighs *c* jin, the next chi weighs *d* jin, and the first chi weighs *e* jin.
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
下第一衰 = 本重 * (長度 - 1)

# 計算每尺重量
weights = []
for i in range(長度):
    # 每尺重量 = 本重 - 差率 * i
    weight = 本重 - 差率 * i
    weights.append(weight)

# 以本重遍乘列衰，並以下第一衰為法
實 = [Fraction(weight * 本重, 下第一衰) for weight in weights]

# 提取每尺重量
e, d, c, b, a = 實  # 按順序對應末到本

# 結果
a, b, c, d, e  # 末一尺重 a斤，次一尺重 b斤，次一尺重 c斤，次一尺重 d斤，次一尺重 e斤
"""
Variable 'a' has wrong value. Expected: 2, Actual: -1
Variable 'b' has wrong value. Expected: 5/2, Actual: -1/2
Variable 'c' has wrong value. Expected: 3, Actual: 0
Variable 'd' has wrong value. Expected: 7/2, Actual: 1/2
Variable 'e' has wrong value. Expected: 4, Actual: 1"""
