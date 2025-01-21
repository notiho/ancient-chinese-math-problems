"""
今有取保一歲，價錢二千五百。今先取一千二百，問︰當作日幾何？
荅曰： a日 。
"""

"""
Suppose there is a contract for one year (365 days) with a total price of 2500. 
Now, 1200 has already been paid in advance. 
Question: how many days does the advance payment cover?

Answer: it covers *a* days.
"""

# Total price for one year
total_price = 2500

# Total days in a year
total_days = 365

# Price per day
price_per_day = Fraction(total_price, total_days)

# Advance payment
advance_payment = 1200

# Days covered by the advance payment
a = Fraction(advance_payment, price_per_day)

a
"""
Variable 'a' has wrong value. Expected: 4248/25, Actual: 876/5"""
