"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
荅曰：得素 a匹 。
"""

"""
Suppose there is one bolt of silk (1 pi) that is 1 zhang in length, and its price is 625 coins.
Now, if you have 500 coins, how much silk can you buy?

Answer: You can buy *a* pi of silk.
"""

# Price of 1 pi of silk
price_per_pi = 625

# Amount of money available
money_available = 500

# Calculate how many pi of silk can be bought
a = Fraction(money_available, price_per_pi)  # Result in pi of silk

a
"""
Variable 'a' has wrong value. Expected: 1, Actual: 4/5"""
