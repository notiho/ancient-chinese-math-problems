"""
今有池，五渠注之。其一渠開之，少半日一滿；次，一日一滿；次，二日半一滿；次，三日一滿；次，五日一滿。今皆決之，問︰幾何日滿池？
術曰：各置渠一日滿池之數，并以為法。以一日為實。實如法得一日。
荅曰： a日 。
"""

"""
To solve this problem, we need to calculate how many days it will take to fill the pool when all five channels are opened simultaneously. Each channel fills the pool at a different rate. Let's translate this into Python code:


"""


from fractions import Fraction

# Rates of each channel (pool filled per day)
rate1 = Fraction(2, 1)  # Half a day to fill, so 2 pools per day
rate2 = Fraction(1, 1)  # 1 day to fill, so 1 pool per day
rate3 = Fraction(2, 5)  # 2.5 days to fill, so 2/5 pools per day
rate4 = Fraction(1, 3)  # 3 days to fill, so 1/3 pools per day
rate5 = Fraction(1, 5)  # 5 days to fill, so 1/5 pools per day

# Total rate when all channels are opened
total_rate = rate1 + rate2 + rate3 + rate4 + rate5

# Time to fill the pool when all channels are opened
a = Fraction(1, total_rate)

# Result
a  # This is the number of days it takes to fill the pool


"""


The variable `a` will contain the number of days it takes to fill the pool when all five channels are opened simultaneously.
"""


"""
Variable 'a' has wrong value. Expected: 15/74, Actual: 15/59"""
