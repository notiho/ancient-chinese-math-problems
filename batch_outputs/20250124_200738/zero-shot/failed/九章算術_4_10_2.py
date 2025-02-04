"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一、十分步之一、十一分步之一、十二分步之一。求田一畝，問︰從幾何？
術曰：下有一十二分，以一為八萬三千一百六十，半為四萬一千五百八十，三分之一為二萬七千七百二十，四分之一為二萬七百九十，五分之一為一萬六千六百三十二，六分之一為一萬三千八百六十，七分之一為一萬一千八百八十，八分之一為一萬三百九十五，九分之一為九千二百四十，一十分之一為八千三百一十六十一分之一為七千五百六十，十二分之一為六千九百三十，并之得二十五萬八千六十三，以為法。置田二百四十步，亦以一為八萬三千一百六十乘之，為實。實如法得從步。
荅曰： a步 。
"""

"""
To solve this problem, we need to compute the total area of the field in terms of steps (步). The problem provides a breakdown of the contributions of fractional steps to the total area. The solution involves summing these contributions and then using the given formula to calculate the number of steps.

Here is the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_area = 240  # Total area in steps (步)
unit_area = Fraction(83160)  # Area corresponding to 1 step (步)

# Fractional contributions
fractions = [
    Fraction(1, 1),  # 1
    Fraction(1, 2),  # 1/2
    Fraction(1, 3),  # 1/3
    Fraction(1, 4),  # 1/4
    Fraction(1, 5),  # 1/5
    Fraction(1, 6),  # 1/6
    Fraction(1, 7),  # 1/7
    Fraction(1, 8),  # 1/8
    Fraction(1, 9),  # 1/9
    Fraction(1, 10), # 1/10
    Fraction(1, 11), # 1/11
    Fraction(1, 12)  # 1/12
]

# Compute the total fractional contribution
total_fraction = sum(fractions)

# Compute the total area in terms of steps
a = total_area * unit_area / total_fraction

# Result
a
#----- content ends here -----


"""


The variable `a` will contain the solution in terms of steps (步).
"""


"""
Variable 'a' has wrong value. Expected: 6652800/86021, Actual: 553246848000/86021"""
