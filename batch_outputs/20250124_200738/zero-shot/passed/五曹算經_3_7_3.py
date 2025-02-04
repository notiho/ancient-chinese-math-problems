"""
今有米一千五百七十七斛，斛别加八斗三升。問：計㡬何？
術曰：列米一千五百七十七斛，以加米一斛八斗三升乘之即得。
答曰： a斛 。
"""

"""
To solve the problem, let's translate it into Python code. The problem states that there are 1577 "斛" of rice, and each "斛" is increased by 8 "斗" and 3 "升". We need to calculate the total amount of rice.

1 "斛" = 10 "斗", and 1 "斗" = 10 "升". Therefore, we need to convert the additional amount (8 "斗" and 3 "升") into "斛" and then multiply it by 1577.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_hu = 1577  # Total "斛"
additional_dou = 8  # Additional "斗"
additional_sheng = 3  # Additional "升"

# Convert additional amount to "斛"
additional_hu = Fraction(additional_dou, 10) + Fraction(additional_sheng, 100)

# Calculate total rice in "斛"
a = total_hu * (1 + additional_hu)

# Result
a  # Total amount of rice in "斛"
#----- content ends here -----


"""


The variable `a` will contain the total amount of rice in "斛".
"""


"""
"""
