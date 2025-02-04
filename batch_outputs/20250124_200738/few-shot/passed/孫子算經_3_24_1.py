"""
今有物，不知其數。三三數之，賸二；五五數之，賸三；七七數之，賸二。問：物幾何？
術曰：三三數之，賸二，置一百四十；五五數之，賸三，置六十三；七七數之，賸二，置三十。并之，得二百三十三，以二百一十減之，即得。凡三三數之，賸一，則置七十；五五數之，賸一，則置二十一；七七數之，賸一，則置十五。一百六以上，以一百五減之，即得。
答曰： a 。
"""

#----- content starts here -----
"""
Suppose there is an unknown number of objects. 
When divided by 3, the remainder is 2. 
When divided by 5, the remainder is 3. 
When divided by 7, the remainder is 2. 
Question: how many objects are there?

The procedure says:
- For "divided by 3, remainder 2," place 140.
- For "divided by 5, remainder 3," place 63.
- For "divided by 7, remainder 2," place 30.
- Add these, obtaining 233. Subtract 210 from it, and the result is the answer.

If the remainders were all 1:
- For "divided by 3, remainder 1," place 70.
- For "divided by 5, remainder 1," place 21.
- For "divided by 7, remainder 1," place 15.
- If the sum exceeds 150, subtract 150, and the result is the answer.

Answer: *a*.
"""

# 三三數之，賸二，置一百四十
三餘二 = 140

# 五五數之，賸三，置六十三
五餘三 = 63

# 七七數之，賸二，置三十
七餘二 = 30

# 并之，得二百三十三
總和 = 三餘二 + 五餘三 + 七餘二

# 以二百一十減之，即得
a = 總和 - 210#----- content ends here -----

"""
"""
