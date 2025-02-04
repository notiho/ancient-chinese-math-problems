"""
今有絲一斤八兩直絹一疋今持絲一斤禆錢五十得絹三丈今有錢一千問得絹㡬何
術曰置絲一斤兩數以一疋尺數乗之以絲一斤八兩數而一所得以減得絹尺數餘以一千錢乗之為實以五千錢為法實如法得一
答曰 a疋
"""

"""
Suppose there is 1 jin and 8 liang of silk, which is worth 1 bolt of silk fabric (1 pi). 
Now, 1 jin of silk is worth 50 qian, and it can produce 3 zhang of silk fabric.
Question: if you have 1000 qian, how many bolts of silk fabric can you obtain?

The procedure says: Place the number of liang in 1 jin of silk.
Multiply it by the number of chi in 1 pi.
Divide it by the number of liang in 1 jin and 8 liang.
Subtract the result from the number of chi in the silk fabric.
Take the remainder and multiply it by 1000 qian, giving the dividend.
Take 5000 qian as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* pi.
"""

from fractions import Fraction

# 絲一斤兩數 (1 jin = 16 liang)
絲一斤兩數 = 16

# 一疋尺數 (1 pi = 3 zhang = 30 chi)
一疋尺數 = 30

# 絲一斤八兩數 (1 jin 8 liang = 16 + 8 = 24 liang)
絲一斤八兩數 = 24

# 錢一千
錢 = 1000

# 以絲一斤兩數以一疋尺數乘之
步驟1 = 絲一斤兩數 * 一疋尺數

# 以絲一斤八兩數而一所得
步驟2 = Fraction(步驟1, 絲一斤八兩數)

# 以減得絹尺數餘
絹尺數餘 = 一疋尺數 - 步驟2

# 以一千錢乘之為實
實 = 絹尺數餘 * 錢

# 以五千錢為法
法 = 5000

# 實如法得一
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 2"""
