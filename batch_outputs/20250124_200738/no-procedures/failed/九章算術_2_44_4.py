"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

#----- content starts here -----
"""
Suppose there are 610 qian (units of money) used to buy 2100 hou (feathers). 
It is desired to determine the rate of expensive feathers and cheap feathers.

Answer: *a* hou at *b* hou per qian, and *c* hou at *d* hou per qian.
"""

# Total money and feathers
total_money = 610
total_feathers = 2100

# Expensive feathers: 3 hou per qian
b = 3
a = total_money // (1 / b)  # Total expensive feathers

# Cheap feathers: 5 hou per qian
d = 5
c = total_feathers - a  # Remaining feathers are cheap feathers

# Output
a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1140, Actual: 1830.0
Variable 'c' has wrong value. Expected: 960, Actual: 270.0
Variable 'd' has wrong value. Expected: 4, Actual: 5"""
