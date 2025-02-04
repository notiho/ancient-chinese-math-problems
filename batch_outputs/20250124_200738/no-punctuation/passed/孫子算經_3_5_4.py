"""
今有租九萬八千七百六十二斛欲以一車載五十斛問用車幾何
術曰置租九萬八千七百六十二斛為實以一車所載五十斛為法實如法即得
答曰 a乘 奇 b斛 
"""

#----- content starts here -----
"""
Suppose there is a rent of 98,762 hu, and it is desired to transport it using carts, each carrying 50 hu.
Question: how many carts are needed, and how much is left over?

The procedure says: Place the rent of 98,762 hu as the dividend.
Take the amount one cart can carry, 50 hu, as the divisor.
Divide the dividend by the divisor, obtaining the number of carts.
The remainder is the leftover hu.

Answer: *a* carts, with *b* hu remaining.
"""

# 置租九萬八千七百六十二斛為實
實 = 98762

# 以一車所載五十斛為法
法 = 50

# 實如法即得
a = 實 // 法  # Number of carts
b = 實 % 法   # Remaining hu#----- content ends here -----

"""
"""
