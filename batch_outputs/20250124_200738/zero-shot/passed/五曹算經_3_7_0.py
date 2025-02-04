"""
今有米一千五百七十七斛，斛别加八斗三升。問：計㡬何？
術曰：列米一千五百七十七斛，以加米一斛八斗三升乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will calculate the total amount of rice when 1,577 "斛" (a unit of volume) is increased by 8 "斗" and 3 "升" per "斛". First, we need to convert the additional amount into a fraction of a "斛". Since 1 "斛" = 10 "斗" and 1 "斗" = 10 "升", the additional amount per "斛" is:

8 "斗" = 8/10 "斛"  
3 "升" = 3/(10 * 10) "斛" = 3/100 "斛"  

Thus, the total additional amount per "斛" is:  
(8/10) + (3/100) = 80/100 + 3/100 = 83/100 "斛".

Now, we multiply this additional amount by the total number of "斛" (1,577) to find the total increase, and then add it to the original amount.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
original_amount = 1577  # in 斛
additional_per_hu = Fraction(83, 100)  # 8斗3升 converted to 斛

# Total calculation
a = original_amount * (1 + additional_per_hu)

# Result
a  # in 斛
#----- content ends here -----


"""


The variable `a` will contain the total amount of rice in "斛".
"""


"""
"""
