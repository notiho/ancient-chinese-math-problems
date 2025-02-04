"""
今有兔先走一百步，犬追之二百五十步，不及三十步而止。問︰犬不止，復行幾何步及之？
術曰：置兔先走一百步，以犬走不及三十步減之，餘為法。以不及三十步乘犬追步數為實，實如法得一步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose a rabbit starts by running 100 steps, and a dog chases it for 250 steps but is still 30 steps short of catching it.
Question: if the dog does not stop, how many more steps must it run to catch the rabbit?

The procedure says: Place the 100 steps the rabbit initially ran, and subtract the 30 steps by which the dog falls short. The remainder is the divisor.
Multiply the 30 steps by which the dog falls short by the 250 steps the dog ran, giving the dividend.
Divide the dividend by the divisor to obtain the additional steps the dog must run.

Answer: *a* steps.
"""

# Initial data
兔先走 = 100  # Rabbit's initial steps
犬追步數 = 250  # Dog's chasing steps
不及 = 30  # Steps by which the dog falls short

# 法: 置兔先走一百步，以犬走不及三十步減之
法 = 兔先走 - 不及

# 實: 以不及三十步乘犬追步數
實 = 不及 * 犬追步數

# 實如法得一步
a = Fraction(實, 法)

a  # The additional steps the dog must run to catch the rabbit#----- content ends here -----

"""
"""
