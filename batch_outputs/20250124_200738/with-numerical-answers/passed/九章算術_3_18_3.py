"""
今有取保一歲，價錢二千五百。今先取一千二百，問︰當作日幾何？
術曰：以價錢為法，以一歲三百五十四日乘先取錢數為實，實如法得日數。
荅曰： a(=4248/25)日 。
"""

#----- content starts here -----
"""
Suppose there is a contract for one year, with a value of 2500 coins.
Now, 1200 coins are taken in advance.
Question: how many days does this correspond to?

The procedure says: Take the total value of the contract as the divisor.
Multiply the number of days in one year (354 days) by the amount of coins taken in advance, obtaining the dividend.
Divide the dividend by the divisor to get the number of days.

Answer: *a*(=4248/25) days.
"""

# 價錢二千五百
價錢 = 2500

# 一歲三百五十四日
一年日數 = 354

# 先取一千二百
先取錢數 = 1200

# 以一歲三百五十四日乘先取錢數為實
實 = 一年日數 * 先取錢數

# 實如法得日數
a = Fraction(實, 價錢) # 4248/25 days#----- content ends here -----

"""
"""
