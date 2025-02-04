"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一、十分步之一、十一分步之一、十二分步之一。求田一畝，問︰從幾何？
術曰：下有一十二分，以一為八萬三千一百六十，半為四萬一千五百八十，三分之一為二萬七千七百二十，四分之一為二萬七百九十，五分之一為一萬六千六百三十二，六分之一為一萬三千八百六十，七分之一為一萬一千八百八十，八分之一為一萬三百九十五，九分之一為九千二百四十，一十分之一為八千三百一十六十一分之一為七千五百六十，十二分之一為六千九百三十，并之得二十五萬八千六十三，以為法。置田二百四十步，亦以一為八萬三千一百六十乘之，為實。實如法得從步。
荅曰： a步 。
"""

"""
To solve the problem, we need to compute the total area of the field in terms of steps (`步`) based on the given fractions and their corresponding values. The solution involves summing up the contributions of each fraction and then using the total area to calculate the number of steps (`a`).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values for each fraction of a step
one = 83160
half = 41580
third = 27720
quarter = 20790
fifth = 16632
sixth = 13860
seventh = 11880
eighth = 10395
ninth = 9240
tenth = 8316
eleventh = 7560
twelfth = 6930

# Total area (法)
total_area = one + half + third + quarter + fifth + sixth + seventh + eighth + ninth + tenth + eleventh + twelfth

# Given field size in steps
field_size = 240

# Calculate the number of steps (a)
a = Fraction(field_size * one, total_area)

# Result
a
#----- content ends here -----


"""


The variable `a` will contain the number of steps (`步`) as a `Fraction`.
"""


"""
"""
