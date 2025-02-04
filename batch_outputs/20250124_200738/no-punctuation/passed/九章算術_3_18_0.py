"""
今有取保一歲價錢二千五百今先取一千二百問當作日幾何
術曰以價錢為法以一歲三百五十四日乘先取錢數為實實如法得日數
荅曰 a日 
"""

#----- content starts here -----
"""
Suppose there is a contract for one year with a value of 2500 qian. 
Now, 1200 qian is taken in advance. 
Question: how many days does this correspond to?

The procedure says: Take the total value of the contract as the divisor.
Multiply the number of days in one year (354 days) by the amount of money taken in advance, obtaining the dividend.
Divide the dividend by the divisor, obtaining the number of days.

The answer says: *a* days.
"""

# 一歲價錢二千五百
價錢 = 2500

# 一歲三百五十四日
一年日數 = 354

# 先取一千二百
先取錢數 = 1200

# 以一歲三百五十四日乘先取錢數，為實
實 = 一年日數 * 先取錢數

# 以價錢為法
法 = 價錢

# 實如法得日數
a = Fraction(實, 法)#----- content ends here -----

"""
"""
