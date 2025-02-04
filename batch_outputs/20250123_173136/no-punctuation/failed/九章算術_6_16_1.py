"""
今有金箠長五尺斬本一尺重四斤斬末一尺重二斤問次一尺各重幾何
術曰令末重減本重餘即差率也又置本重以四間乘之為下第一衰副置以差率減之每尺各自為衰副置下第一衰以為法以本重四斤遍乘列衰各自為實實如法得一斤
荅曰末一尺重 a斤 次一尺 重 b斤 次一尺 重 c斤 次一尺 重 d斤 次一尺 重 e斤
"""

"""
Suppose there is a golden rod 5 chi long. 
The first chi (near the base) weighs 4 jin, and the last chi (near the tip) weighs 2 jin.
Question: how much does each intermediate chi weigh?

The procedure says:
1. Subtract the weight of the last chi from the weight of the first chi; the remainder is the rate of difference.
2. Place the weight of the first chi (4 jin), multiply it by 4 (the number of intervals between the 5 chi) to obtain the first divisor.
3. For each chi, subtract the rate of difference from the previous weight, creating a decreasing sequence.
4. Place the first divisor as the denominator (法).
5. Multiply the weight of the first chi (4 jin) by the sequence of weights, obtaining the numerators (實).
6. Divide each numerator by the divisor to obtain the weight of each chi.

Answer: The last chi weighs *a* jin, the next chi weighs *b* jin, the next chi weighs *c* jin, the next chi weighs *d* jin, and the first chi weighs *e* jin.
"""

# 斬本一尺重四斤
本重 = 4

# 斬末一尺重二斤
末重 = 2

# 差率 = 本重 - 末重
差率 = 本重 - 末重

# 置本重以四間乘之為下第一衰
間數 = 4
下第一衰 = 本重 * 間數

# 副置以差率減之，每尺各自為衰
衰 = [本重 - i * 差率 for i in range(5)]

# 置下第一衰以為法
法 = 下第一衰

# 以本重四斤遍乘列衰各自為實
實 = [本重 * i for i in 衰]

# 實如法得一斤
weights = [Fraction(i, 法) for i in 實]

# Assign weights to each chi
e, d, c, b, a = weights  # From first chi to last chi
"""
Variable 'a' has wrong value. Expected: 2, Actual: -1
Variable 'b' has wrong value. Expected: 5/2, Actual: -1/2
Variable 'c' has wrong value. Expected: 3, Actual: 0
Variable 'd' has wrong value. Expected: 7/2, Actual: 1/2
Variable 'e' has wrong value. Expected: 4, Actual: 1"""
