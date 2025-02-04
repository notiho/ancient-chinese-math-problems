"""
今有絲一斤，價直二百四十。今有錢一千三百二十八，問︰得絲幾何？
術曰：以一斤價數為法，以一斤乘今有錢數為實，實如法得絲數。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk, priced at 240 coins. 
Now, there are 1328 coins. 
Question: how much silk can be obtained?

The procedure says: Take the price of 1 jin as the divisor. 
Multiply 1 jin by the number of coins currently available to obtain the dividend. 
Divide the dividend by the divisor to get the amount of silk.

Answer: *a* jin.
"""

from fractions import Fraction

# 絲一斤，價直二百四十
絲一斤價 = 240

# 錢一千三百二十八
錢數 = 1328

# 以一斤價數為法
法 = 絲一斤價

# 以一斤乘今有錢數為實
實 = 1 * 錢數

# 實如法得絲數
a = Fraction(實, 法)

a  # Output the amount of silk in jin#----- content ends here -----

"""
"""
