"""
今有取保一歲，價錢二千五百。今先取一千二百，問︰當作日幾何？
荅曰： a日 。
"""

"""
Suppose there is a contract for one year (365 days) with a total payment of 2500 coins.
Now, 1200 coins have been paid in advance.
Question: how many days does this advance payment cover?

Answer: it covers *a* days.
"""

# Total payment for one year
total_payment = 2500

# Total days in one year
total_days = 365

# Payment already made
advance_payment = 1200

# Calculate how many days the advance payment covers
a = Fraction(advance_payment * total_days, total_payment)
"""
Variable 'a' has wrong value. Expected: 4248/25, Actual: 876/5"""
