"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
Suppose 610 qian (coins) are spent to purchase 2100 hu (feathers). The feathers are of two types: expensive and cheap.
Question: what is the rate of each type of feather (how many hu per qian for each type)?

Answer: the expensive feathers are *a* hu per qian, and *b* hu cost 1 qian.
The cheap feathers are *c* hu per qian, and *d* hu cost 1 qian.
"""

# Total money spent
total_money = 610

# Total feathers purchased
total_feathers = 2100

# Let the expensive feathers cost 3 hu per qian
expensive_rate = 3  # a = 3

# Calculate how many expensive feathers were purchased
expensive_feathers = expensive_rate * total_money // 2  # b = 2 (3 hu per qian means 2 qian buys 6 hu)

# Calculate the remaining feathers (cheap feathers)
cheap_feathers = total_feathers - expensive_feathers

# Calculate the rate for cheap feathers
cheap_rate = cheap_feathers // (total_money // 2)  # c = 7 (7 hu per qian means 1 qian buys 7 hu)
cheap_cost = 1  # d = 1 (1 qian buys 7 hu)

# Final results
a = expensive_rate
b = 2  # 2 qian buys 6 hu
c = cheap_rate
d = cheap_cost

a, b, c, d
"""
Variable 'a' has wrong value. Expected: 1140, Actual: 3
Variable 'b' has wrong value. Expected: 3, Actual: 2
Variable 'c' has wrong value. Expected: 960, Actual: 3
Variable 'd' has wrong value. Expected: 4, Actual: 1"""
