"""
今有生絲一斤練之折五兩練絲一斤染之出三兩今有生絲五十六斤八兩七分兩之四問染得㡬何
術曰置一斤兩數以折兩數減之餘乗今有絲斤兩之數又以出兩數併一斤兩數乗之為實一斤兩數自乗為法實如法得一兩數
答曰 a斤
"""

"""
Suppose there is 1 jin of raw silk. When refined, it loses 5 liang. 
When 1 jin of refined silk is dyed, it produces 3 liang.
Now suppose there are 56 jin, 8 liang, and 7/10 of a liang of raw silk.
Question: how much dyed silk is obtained?

The procedure says: Place the liang count of 1 jin and subtract the loss liang count from it. 
Take the remainder and multiply it by the total jin and liang count of the raw silk.
Then, take the output liang count and add it to the liang count of 1 jin, and multiply them together to form the dividend.
Square the liang count of 1 jin to form the divisor.
Divide the dividend by the divisor to obtain the result in jin.

Answer: *a* jin.
"""

from fractions import Fraction

# 生絲一斤
一斤兩數 = 16  # 1 jin = 16 liang

# 練之折五兩
折兩數 = 5

# 練絲一斤染之出三兩
出兩數 = 3

# 生絲五十六斤八兩七分兩之四
生絲 = 56 + Fraction(8, 16) + Fraction(7, 10 * 16)

# 置一斤兩數，以折兩數減之
餘 = 一斤兩數 - 折兩數

# 餘乘今有絲斤兩之數
實 = 餘 * 生絲

# 又以出兩數併一斤兩數，乘之為實
實 = 實 * (出兩數 + 一斤兩數)

# 一斤兩數自乘為法
法 = 一斤兩數 ** 2

# 實如法得一兩數
a = Fraction(實, 法)

"""
Variable 'a' has wrong value. Expected: 330847/7168, Actual: 1890823/40960"""
