"""
今有車五乘行道三十里僱錢一百四十五今有車二十六乘僱錢三千九百五十四四十五分錢之十四問行道幾何
術曰置今有僱錢數以行道里數乘之以本車乘數乘之為實以本僱錢數乘今有車數為法實如法得一
答曰 a里
"""

"""
Suppose there are 5 carts traveling 30 li, and the hiring cost is 145 qian.
Now there are 26 carts, and the hiring cost is 3954 and 14/45 qian.
Question: how far do they travel?

The procedure says: Place the current hiring cost and multiply it by the distance in li. 
Then multiply it by the original number of carts, obtaining the dividend.
Multiply the original hiring cost by the current number of carts, obtaining the divisor.
Divide the dividend by the divisor to obtain the distance.

Answer: *a* li.
"""

from fractions import Fraction

# 本車乘數 (original number of carts)
本車乘數 = 5

# 行道里數 (original distance in li)
本行道里數 = 30

# 本僱錢數 (original hiring cost)
本僱錢數 = 145

# 今有車數 (current number of carts)
今車數 = 26

# 今有僱錢數 (current hiring cost)
今僱錢數 = 3954 + Fraction(14, 45)

# 置今有僱錢數，以行道里數乘之
實 = 今僱錢數 * 本行道里數

# 以本車乘數乘之
實 *= 本車乘數

# 以本僱錢數乘今有車數，為法
法 = 本僱錢數 * 今車數

# 實如法得一
a = Fraction(實, 法)
"""
"""
