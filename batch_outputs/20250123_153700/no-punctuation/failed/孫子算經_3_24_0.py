"""
今有物不知其數三三數之賸二五五數之賸三七七數之賸二問物幾何
術曰三三數之賸二置一百四十五五數之賸三置六十三七七數之賸二置三十并之得二百三十三以二百一十減之即得凡三三數之賸一則置七十五五數之賸一則置二十一七七數之賸一則置十五一百六以上以一百五減之即得
答曰 a 
"""

"""
Suppose there is an unknown number of objects. When counted in groups of 3, the remainder is 2. 
When counted in groups of 5, the remainder is 3. 
When counted in groups of 7, the remainder is 2.
Question: what is the number of objects?

The procedure says: 
For "counted in groups of 3, remainder 2," place 145.
For "counted in groups of 5, remainder 3," place 63.
For "counted in groups of 7, remainder 2," place 30.
Add these, obtaining 233. Subtract 210 from it, and the result is the answer.

If "counted in groups of 3, remainder 1," place 75.
If "counted in groups of 5, remainder 1," place 21.
If "counted in groups of 7, remainder 1," place 15.
For numbers above 100, subtract 105, and the result is the answer.

Answer: *a*.
"""

# 三三數之賸二置一百四十五
置_3 = 145

# 五五數之賸三置六十三
置_5 = 63

# 七七數之賸二置三十
置_7 = 30

# 并之得二百三十三
總和 = 置_3 + 置_5 + 置_7

# 以二百一十減之即得
a = 總和 - 210
"""
Variable 'a' has wrong value. Expected: 23, Actual: 28"""
