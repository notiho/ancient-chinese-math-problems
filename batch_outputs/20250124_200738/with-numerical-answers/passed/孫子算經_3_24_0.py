"""
今有物，不知其數。三三數之，賸二；五五數之，賸三；七七數之，賸二。問：物幾何？
術曰：三三數之，賸二，置一百四十；五五數之，賸三，置六十三；七七數之，賸二，置三十。并之，得二百三十三，以二百一十減之，即得。凡三三數之，賸一，則置七十；五五數之，賸一，則置二十一；七七數之，賸一，則置十五。一百六以上，以一百五減之，即得。
答曰： a(=23) 。
"""

#----- content starts here -----
"""
Suppose there is an unknown number of objects. 
When counted in groups of 3, there is a remainder of 2.
When counted in groups of 5, there is a remainder of 3.
When counted in groups of 7, there is a remainder of 2.
Question: how many objects are there?

The procedure says:
- For groups of 3 with a remainder of 2, place 140.
- For groups of 5 with a remainder of 3, place 63.
- For groups of 7 with a remainder of 2, place 30.
Add these, obtaining 233. Subtract 210 from it, and the result is the answer.

If the remainder is 1:
- For groups of 3, place 70.
- For groups of 5, place 21.
- For groups of 7, place 15.
If the result is greater than 150, subtract 150 to obtain the answer.

Answer: *a*(=23).
"""

# 三三數之，賸二，置一百四十
三三置 = 140

# 五五數之，賸三，置六十三
五五置 = 63

# 七七數之，賸二，置三十
七七置 = 30

# 并之，得二百三十三
總和 = 三三置 + 五五置 + 七七置

# 以二百一十減之，即得
a = 總和 - 210 # 23#----- content ends here -----

"""
"""
