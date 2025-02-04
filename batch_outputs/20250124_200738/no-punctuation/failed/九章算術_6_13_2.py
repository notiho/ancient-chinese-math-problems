"""
今有兔先走一百步犬追之二百五十步不及三十步而止問犬不止復行幾何步及之
術曰置兔先走一百步以犬走不及三十步減之餘為法以不及三十步乘犬追步數為實實如法得一步
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose a rabbit starts by running 100 steps, and a dog chases it by running 250 steps but is still 30 steps behind when it stops.
Question: if the dog does not stop and continues running, how many more steps does it need to catch the rabbit?

The procedure says: Place the 100 steps the rabbit initially runs.
Subtract the 30 steps the dog is behind from the 250 steps the dog runs; the remainder is the divisor.
Multiply the 30 steps the dog is behind by the 250 steps the dog runs; this is the dividend.
Divide the dividend by the divisor to obtain the number of steps.

The answer says: *a* steps.
"""

# 兔先走一百步
兔先走 = 100

# 犬追之二百五十步
犬追步數 = 250

# 不及三十步
不及步數 = 30

# 以犬走不及三十步減之，餘為法
法 = 犬追步數 - 不及步數

# 以不及三十步乘犬追步數，為實
實 = 不及步數 * 犬追步數

# 實如法得一步
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 750/7, Actual: 375/11"""
