"""
今有田廣一步半、三分步之一、四分步之一。求田一畝，問︰從幾何？
術曰：下有四分，以一為一十二，半為六，三分之一為四，四分之一為三，并之得二十五，以為法。置田二百四十步，亦以一為一十二乘之，為實。實如法而一，得從步。
荅曰： a步 。
"""

"""
To solve this problem, we need to compute the value of `a` in terms of steps (步). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
田廣 = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4)  # 田廣一步半、三分步之一、四分步之一
田一畝 = 240  # 田一畝 is 240 steps

# Convert 田廣 to a common denominator
田廣_in_twelfths = Fraction(1, 2) * 12 + Fraction(1, 3) * 12 + Fraction(1, 4) * 12  # Convert to twelfths
田廣_in_twelfths = 6 + 4 + 3  # 半為六，三分之一為四，四分之一為三
田廣_total = 田廣_in_twelfths  # Total is 25 twelfths

# 法 (the divisor) is 25 twelfths
法 = 田廣_total

# Convert 田一畝 to twelfths
田一畝_in_twelfths = 田一畝 * 12  # 240 steps multiplied by 12

# Compute the result
a = 田一畝_in_twelfths / 法  # 實如法而一，得從步

# Simplify the result
a = Fraction(a)

# The result is in steps (步)
print(f"a = {a} 步")
#----- content ends here -----


"""


This code calculates the value of `a` in steps (步). The final value of `a` will be printed as a fraction.
"""


"""
Variable 'a' has wrong value. Expected: 576/5, Actual: 1948672915689157/8796093022208"""
