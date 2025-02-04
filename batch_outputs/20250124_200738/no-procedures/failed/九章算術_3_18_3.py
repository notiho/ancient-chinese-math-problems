"""
今有取保一歲，價錢二千五百。今先取一千二百，問︰當作日幾何？
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose there is a contract for one year (365 days) with a total value of 2500 coins.
Now, 1200 coins are taken in advance.
Question: how many days does this advance payment cover?

Answer: it covers *a* days.
"""

# Total contract value for one year
total_value = 2500

# Total days in a year
total_days = 365

# Daily rate (value per day)
daily_rate = Fraction(total_value, total_days)

# Advance payment
advance_payment = 1200

# Days covered by the advance payment
a = Fraction(advance_payment, daily_rate)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4248/25, Actual: 876/5"""
