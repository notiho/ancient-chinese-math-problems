"""
今有取保一歲，價錢二千五百。今先取一千二百，問︰當作日幾何？
術曰：以價錢為法，以一歲三百五十四日乘先取錢數為實，實如法得日數。
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose there is a contract for one year, with a total payment of 2500 coins.
Now, 1200 coins are taken in advance.
Question: how many days does this advance payment cover?

The procedure says: Take the total payment as the divisor.
Multiply the number of days in one year (354 days) by the amount of advance payment, obtaining the dividend.
Divide the dividend by the divisor, obtaining the number of days.

Answer: *a* days.
"""

from fractions import Fraction

# Total payment for one year
價錢 = 2500

# Days in one year
一年日數 = 354

# Advance payment
先取錢數 = 1200

# Multiply days in one year by the advance payment to get the dividend
實 = 一年日數 * 先取錢數

# Divide the dividend by the total payment to get the number of days
a = Fraction(實, 價錢)

a#----- content ends here -----

"""
"""
