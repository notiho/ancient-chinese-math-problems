"""
今有物，不知其數。三三數之，賸二；五五數之，賸三；七七數之，賸二。問：物幾何？
術曰：三三數之，賸二，置一百四十；五五數之，賸三，置六十三；七七數之，賸二，置三十。并之，得二百三十三，以二百一十減之，即得。凡三三數之，賸一，則置七十；五五數之，賸一，則置二十一；七七數之，賸一，則置十五。一百六以上，以一百五減之，即得。
答曰： a 。
"""

"""
Suppose there is an unknown quantity of objects. 
When divided by 3, the remainder is 2; 
when divided by 5, the remainder is 3; 
when divided by 7, the remainder is 2. 
Question: how many objects are there?

The procedure says: 
When dividing by 3 and the remainder is 2, place 140. 
When dividing by 5 and the remainder is 3, place 63. 
When dividing by 7 and the remainder is 2, place 30. 
Add these, obtaining 233. Subtract 210 from it, and the result is obtained. 
If dividing by 3 and the remainder is 1, place 70. 
If dividing by 5 and the remainder is 1, place 21. 
If dividing by 7 and the remainder is 1, place 15. 
If the result is greater than 150, subtract 105, and the result is obtained.

Answer: *a*.
"""

# 三三數之，賸二，置一百四十
三置 = 140

# 五五數之，賸三，置六十三
五置 = 63

# 七七數之，賸二，置三十
七置 = 30

# 并之，得二百三十三
總和 = 三置 + 五置 + 七置

# 以二百一十減之，即得
a = 總和 - 210

a
"""
"""
