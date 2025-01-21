"""
今有取保一歲，價錢二千五百。今先取一千二百，問︰當作日幾何？
荅曰： a日 。
"""

"""
Suppose there is a contract for one year (365 days) with a total payment of 2500 coins.
Now, 1200 coins are paid in advance.
Question: how many days does this advance payment cover?

Answer: it covers *a* days.
"""

# Total contract duration and payment
total_days = 365
total_payment = 2500

# Advance payment
advance_payment = 1200

# Calculate the number of days covered by the advance payment
a = Fraction(advance_payment * total_days, total_payment)
"""
Variable 'a' has wrong value. Expected: 4248/25, Actual: 876/5"""
