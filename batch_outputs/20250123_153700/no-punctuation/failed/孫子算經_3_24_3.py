"""
今有物不知其數三三數之賸二五五數之賸三七七數之賸二問物幾何
術曰三三數之賸二置一百四十五五數之賸三置六十三七七數之賸二置三十并之得二百三十三以二百一十減之即得凡三三數之賸一則置七十五五數之賸一則置二十一七七數之賸一則置十五一百六以上以一百五減之即得
答曰 a 
"""

"""
Suppose there is an unknown number of objects.
When counted in groups of 3, there is a remainder of 2.
When counted in groups of 5, there is a remainder of 3.
When counted in groups of 7, there is a remainder of 2.
Question: how many objects are there?

The procedure says:
- For the condition "counted in groups of 3, remainder 2," place 145.
- For the condition "counted in groups of 5, remainder 3," place 63.
- For the condition "counted in groups of 7, remainder 2," place 30.
- Add these together, obtaining 233.
- Subtract 210 from it, and the result is the answer.

If the remainders are all 1:
- For "counted in groups of 3, remainder 1," place 75.
- For "counted in groups of 5, remainder 1," place 21.
- For "counted in groups of 7, remainder 1," place 15.
- Add these together, obtaining a number greater than 100.
- Subtract 105 from it, and the result is the answer.

Answer: *a*.
"""

# 三三數之賸二置一百四十五
條件1 = 145

# 五五數之賸三置六十三
條件2 = 63

# 七七數之賸二置三十
條件3 = 30

# 并之得二百三十三
總和 = 條件1 + 條件2 + 條件3

# 以二百一十減之即得
a = 總和 - 210
"""
Variable 'a' has wrong value. Expected: 23, Actual: 28"""
