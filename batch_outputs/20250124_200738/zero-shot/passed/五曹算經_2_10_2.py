"""
今有馬六千二百四十三匹，匹給粟五升三合。問：計㡬何？
術曰：列馬六千二百四十三匹，以五升三合乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount of grain (in "斛") required for 6,243 horses, where each horse is given 5升 (sheng) and 3合 (he) of grain. 

### Conversion:
1 斛 = 10 斗 (dou)  
1 斗 = 10 升 (sheng)  
1 升 = 10 合 (he)

Thus, the total grain per horse in terms of 合 is:  
5升 3合 = (5 × 10) + 3 = 53合.

Now, the total grain for 6,243 horses in 合 is:  
6,243 × 53 合.

Finally, we convert the total 合 into 斛:  
1 斛 = 10 × 10 × 10 = 1,000 合.

Here is the Python code to compute the answer:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
horses = 6243
grain_per_horse_in_he = 5 * 10 + 3  # 5升 3合 = 53合
grain_per_horse_in_he = Fraction(grain_per_horse_in_he)

# Total grain in 合
total_grain_in_he = horses * grain_per_horse_in_he

# Convert 合 to 斛
a = total_grain_in_he / 1000  # 1斛 = 1000合

# Result
a  # Total grain in 斛
#----- content ends here -----


"""


The variable `a` will contain the total amount of grain in 斛.
"""


"""
"""
