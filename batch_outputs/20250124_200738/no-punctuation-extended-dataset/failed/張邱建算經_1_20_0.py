"""
今有絲一斤八兩直絹一疋今持絲一斤禆錢五十得絹三丈今有錢一千問得絹㡬何
術曰置絲一斤兩數以一疋尺數乗之以絲一斤八兩數而一所得以減得絹尺數餘以一千錢乗之為實以五千錢為法實如法得一
答曰 a疋
"""

#----- content starts here -----
"""
Suppose there is 1 jin and 8 liang of silk, which is worth 1 bolt of silk fabric (1 pi). 
Now, 1 jin of silk is worth 50 qian, and it can produce 3 zhang of silk fabric.
Question: if you have 1000 qian, how many bolts of silk fabric can you obtain?

The procedure says: Place the number of liang in 1 jin of silk.
Multiply it by the number of chi in 1 pi (bolt).
Divide it by the number of liang in 1 jin and 8 liang.
Subtract the result from the number of chi in 1 pi to get the remaining chi of silk fabric.
Multiply this remainder by 1000 qian to get the dividend.
Take 5000 qian as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* pi.
"""

# 絲一斤兩數 (1 jin = 16 liang)
絲一斤 = 16

# 絹一疋尺數 (1 pi = 3 zhang = 30 chi)
絹一疋 = 30

# 絲一斤八兩數 (1 jin 8 liang = 16 + 8 = 24 liang)
絲一斤八兩 = 24

# 錢一千
錢 = 1000

# 以絲一斤兩數乘以一疋尺數
實 = 絲一斤 * 絹一疋

# 以絲一斤八兩數而一所得
所得 = Fraction(實, 絲一斤八兩)

# 以減得絹尺數餘
餘 = 絹一疋 - 所得

# 以一千錢乘之為實
實 = 餘 * 錢

# 以五千錢為法
法 = 5000

# 實如法得一
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 2"""
