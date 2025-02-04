"""
今有兔先走一百步犬追之二百五十步不及三十步而止問犬不止復行幾何步及之
術曰置兔先走一百步以犬走不及三十步減之餘為法以不及三十步乘犬追步數為實實如法得一步
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose a rabbit first runs 100 bu, and a dog chases it for 250 bu but is still 30 bu short of catching it.
Question: if the dog does not stop and continues running, how many more bu does it need to catch the rabbit?

The procedure says: Place the 100 bu that the rabbit first runs.
Subtract the 30 bu that the dog is short of catching it, and the remainder becomes the divisor.
Multiply the 30 bu by the 250 bu that the dog has already run, and this becomes the dividend.
Divide the dividend by the divisor to obtain the additional bu the dog needs to run.

The answer says: *a* bu.
"""

# 兔先走一百步
兔先走 = 100

# 犬追之二百五十步
犬追步數 = 250

# 不及三十步
不及 = 30

# 以犬走不及三十步減之，餘為法
法 = 兔先走 - 不及

# 以不及三十步乘犬追步數，為實
實 = 不及 * 犬追步數

# 實如法得一步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
