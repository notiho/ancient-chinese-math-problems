"""
今有兔先走一百步，犬追之二百五十步，不及三十步而止。問︰犬不止，復行幾何步及之？
術曰：置兔先走一百步，以犬走不及三十步減之，餘為法。以不及三十步乘犬追步數為實，實如法得一步。
荅曰： a(=750/7)步 。
"""

#----- content starts here -----
"""
Suppose a rabbit first runs 100 steps, and a dog chases it for 250 steps but falls short by 30 steps and stops.
Question: if the dog does not stop, how many more steps must it run to catch the rabbit?

The procedure says: Place the 100 steps the rabbit first ran, and subtract the 30 steps by which the dog falls short. The remainder is the divisor.
Multiply the 30 steps by which the dog falls short by the 250 steps the dog has already run, giving the dividend.
Divide the dividend by the divisor to obtain the additional steps.

Answer: *a*(=750/7) steps.
"""

# 兔先走一百步
兔先走 = 100

# 犬追之二百五十步
犬追步數 = 250

# 不及三十步
不及步數 = 30

# 置兔先走一百步，以犬走不及三十步減之，餘為法
法 = 兔先走 - 不及步數

# 以不及三十步乘犬追步數為實
實 = 不及步數 * 犬追步數

# 實如法得一步
a = Fraction(實, 法) # 750/7#----- content ends here -----

"""
"""
