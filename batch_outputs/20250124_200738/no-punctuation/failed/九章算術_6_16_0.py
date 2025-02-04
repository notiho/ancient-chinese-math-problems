"""
今有金箠長五尺斬本一尺重四斤斬末一尺重二斤問次一尺各重幾何
術曰令末重減本重餘即差率也又置本重以四間乘之為下第一衰副置以差率減之每尺各自為衰副置下第一衰以為法以本重四斤遍乘列衰各自為實實如法得一斤
荅曰末一尺重 a斤 次一尺 重 b斤 次一尺 重 c斤 次一尺 重 d斤 次一尺 重 e斤
"""

#----- content starts here -----
"""
Suppose there is a golden rod 5 chi long. 
The base (first chi) weighs 4 jin, and the tip (last chi) weighs 2 jin.
Question: how much does each intermediate chi weigh?

The procedure says:
Let the weight of the tip be subtracted from the weight of the base. The remainder is the rate of difference.
Also, place the weight of the base, and multiply it by 4 intervals to get the first divisor.
For each chi, subtract the rate of difference from the previous weight, and place it as the next weight.
Use the first divisor as the denominator.
Multiply the base weight (4 jin) by the divisor for each chi, and place it as the numerator.
Divide each numerator by the denominator to get the weight of each chi.

Answer: the tip (last chi) weighs *a* jin, the next chi weighs *b* jin, the next chi weighs *c* jin, the next chi weighs *d* jin, and the base (first chi) weighs *e* jin.
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

# 每尺各自為衰副置
weights = []
for i in range(長度):
    # 每尺重 = 本重 - 差率 * i
    weight = 本重 - 差率 * i
    weights.append(weight)

# 以本重遍乘列衰各自為實
實 = [weight * 本重 for weight in weights]

# 實如法得一斤
法 = 下第一衰
results = [Fraction(weight, 法) for weight in 實]

# Assign results to variables
e, d, c, b, a = results  # From base to tip#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: -1
Variable 'b' has wrong value. Expected: 5/2, Actual: -1/2
Variable 'c' has wrong value. Expected: 3, Actual: 0
Variable 'd' has wrong value. Expected: 7/2, Actual: 1/2
Variable 'e' has wrong value. Expected: 4, Actual: 1"""
