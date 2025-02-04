"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
荅曰：得素 a匹 。
"""

#----- content starts here -----
"""
Suppose there is 1 pi (bolt) of silk, 1 zhang in length, worth 625 coins.
Now, if you have 500 coins, how much silk can you get?

Answer: you can get *a* pi of silk.
"""

# Silk price for 1 pi (1 zhang) is 625 coins
price_per_pi = 625

# Available money
money = 500

# Calculate the amount of silk you can get
a = Fraction(money, price_per_pi)  # Fraction of a pi of silk#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 4/5"""
