"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
荅曰： a人 ，犬價 b 。
"""

"""
Suppose a group of people want to buy a dog. If each person contributes 5 coins, they are 90 coins short. 
If each person contributes 50 coins, they have just enough to buy the dog.

Question: How many people are there, and what is the price of the dog?

Answer: There are *a* people, and the price of the dog is *b* coins.
"""

# Let the number of people be a and the price of the dog be b.
# From the problem:
# 1. If each person contributes 5 coins, the total is 5a, and they are 90 coins short: 5a + 90 = b
# 2. If each person contributes 50 coins, the total is 50a, and it is exactly enough: 50a = b

# Solve the equations:
# From the second equation, b = 50a
# Substitute b = 50a into the first equation:
# 5a + 90 = 50a
# 90 = 50a - 5a
# 90 = 45a
# a = 90 / 45 = 2

# Substitute a = 2 into b = 50a:
# b = 50 * 2 = 100

a = 2  # Number of people
b = 100  # Price of the dog in coins
"""
"""
