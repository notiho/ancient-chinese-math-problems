"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
Suppose there is a total of 610 qian spent to buy 2100 feathers (翭). The feathers are of two types: expensive and cheap. 
The question asks for the rate of each type of feather (how many feathers per qian for each type).

Answer: The expensive feathers are *a* feathers per qian, and the cheap feathers are *b* feathers per qian.
"""

# Total money spent
total_money = 610

# Total feathers bought
total_feathers = 2100

# Let the expensive feathers be x feathers per qian, and the cheap feathers be y feathers per qian.
# Assume the expensive feathers are 3 feathers per qian, and the cheap feathers are 5 feathers per qian.

# Expensive feathers rate
a = 3  # feathers per qian

# Cheap feathers rate
b = 5  # feathers per qian

# Total expensive feathers bought
expensive_feathers = total_money // (1 + 2)

# Total cheap feathers bought
cheap_feathers = total_feathers
"""
Variable 'a' has wrong value. Expected: 1140, Actual: 3
Variable 'b' has wrong value. Expected: 3, Actual: 5
Missing variable in output: 'c'
Missing variable in output: 'd'"""
