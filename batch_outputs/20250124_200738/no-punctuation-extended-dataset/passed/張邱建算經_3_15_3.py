"""
今有車五乘行道三十里僱錢一百四十五今有車二十六乘僱錢三千九百五十四四十五分錢之十四問行道幾何
術曰置今有僱錢數以行道里數乘之以本車乘數乘之為實以本僱錢數乘今有車數為法實如法得一
答曰 a里
"""

#----- content starts here -----
"""
Suppose there are 5 carts traveling 30 li, and the hiring cost is 145 qian.
Now, there are 26 carts, and the hiring cost is 3954 qian and 14/45 qian.
Question: how far do they travel?

The procedure says: Place the current hiring cost and multiply it by the distance in li.
Multiply it by the original number of carts, obtaining the dividend.
Multiply the original hiring cost by the current number of carts, obtaining the divisor.
Divide the dividend by the divisor, obtaining the distance.

Answer: *a* li.
"""

from fractions import Fraction

# 車五乘
本車數 = 5

# 行道三十里
本行道里數 = 30

# 僱錢一百四十五
本僱錢數 = 145

# 車二十六乘
今車數 = 26

# 僱錢三千九百五十四四十五分錢之十四
今僱錢數 = 3954 + Fraction(14, 45)

# 置今有僱錢數，以行道里數乘之
實 = 今僱錢數 * 本行道里數

# 以本車乘數乘之，為實
實 *= 本車數

# 以本僱錢數乘今有車數，為法
法 = 本僱錢數 * 今車數

# 實如法得一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
