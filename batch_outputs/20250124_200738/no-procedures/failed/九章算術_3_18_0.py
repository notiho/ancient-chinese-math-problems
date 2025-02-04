"""
今有取保一歲，價錢二千五百。今先取一千二百，問︰當作日幾何？
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose there is a contract for one year (365 days) with a total payment of 2500 qian.
Now, 1200 qian has already been paid in advance.
Question: how many days does the advance payment cover?

Answer: it covers *a* days.
"""

# Total payment for one year (365 days)
total_payment = 2500

# Total days in a year
total_days = 365

# Payment already made
advance_payment = 1200

# Calculate the number of days covered by the advance payment
a = Fraction(advance_payment * total_days, total_payment)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4248/25, Actual: 876/5"""
