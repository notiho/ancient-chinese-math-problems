"""
今有生絲一斤練之折五兩練絲一斤染之出三兩今有生絲五十六斤八兩七分兩之四問染得㡬何
術曰置一斤兩數以折兩數減之餘乗今有絲斤兩之數又以出兩數併一斤兩數乗之為實一斤兩數自乗為法實如法得一兩數
答曰 a斤
"""

#----- content starts here -----
"""
Suppose there is 1 jin of raw silk. When refined, it loses 5 liang. 
When 1 jin of refined silk is dyed, it produces 3 liang of dyed silk.
Now suppose there are 56 jin, 8 liang, and 7/10 liang of raw silk. 
Question: how much dyed silk is obtained?

The procedure says: Place the number of liang in 1 jin, subtract the number of liang lost in refining. 
Multiply the remainder by the total number of jin and liang of raw silk, obtaining the refined silk.
Then, add the number of liang produced when dyeing to the number of liang in 1 jin, and multiply this by the refined silk, obtaining the dividend.
Square the number of liang in 1 jin, obtaining the divisor.
Divide the dividend by the divisor, obtaining the number of jin of dyed silk.

Answer: *a* jin.
"""

from fractions import Fraction

# Constants
一斤兩數 = 16  # 1 jin = 16 liang
折兩數 = 5     # Loss during refining
出兩數 = 3     # Output during dyeing

# 生絲五十六斤八兩七分兩之四
生絲 = 56 + Fraction(8, 16) + Fraction(7, 10 * 16)

# 置一斤兩數，以折兩數減之
餘 = 一斤兩數 - 折兩數

# 餘乘今有絲斤兩之數
練絲 = 餘 * 生絲

# 又以出兩數併一斤兩數
染法 = 出兩數 + 一斤兩數

# 染法乘練絲，為實
實 = 染法 * 練絲

# 一斤兩數自乘，為法
法 = 一斤兩數 ** 2

# 實如法得一兩數
a = Fraction(實, 法)  # Result in jin of dyed silk#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 330847/7168, Actual: 1890823/40960"""
