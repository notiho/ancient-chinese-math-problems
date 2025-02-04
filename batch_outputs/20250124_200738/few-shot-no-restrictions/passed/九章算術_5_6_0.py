"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
術曰：置本人功，去其五分之一，餘為法。以溝積尺為實。實如法而一，得用徒人數。
荅曰： a人 。
"""

#----- content starts here -----
"""
Suppose there is a ditch with the following dimensions:
- Top width: 1 zhang 5 chi (15 chi)
- Bottom width: 1 zhang (10 chi)
- Depth: 5 chi
- Length: 7 zhang (70 chi)

Question: What is the volume of the ditch?

Answer: 4375 cubic chi.

Additionally, the work rate for one person is 766 cubic chi, including 1/5 of the work for removing the dug-out soil.
The adjusted work rate is 612 and 4/5 cubic chi.

Question: How many workers are required?

The procedure says: Place the work rate of one person, subtract 1/5 of it, and the remainder becomes the divisor.
Take the volume of the ditch as the dividend.
Divide the dividend by the divisor to obtain the number of workers required.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the ditch
上廣 = 15  # Top width in chi
下廣 = 10  # Bottom width in chi
深 = 5     # Depth in chi
袤 = 70    # Length in chi

# Volume of the ditch
積 = Fraction((上廣 + 下廣) * 深 * 袤, 2)  # Trapezoidal prism formula
assert 積 == 4375  # Confirm the calculated volume matches the given answer

# Work rate for one person
本人功 = Fraction(766)  # Total work rate including 1/5 for removing soil
去土功 = Fraction(1, 5) * 本人功  # 1/5 of the work rate for removing soil
法 = 本人功 - 去土功  # Adjusted work rate (法)
assert 法 == Fraction(612, 1) + Fraction(4, 5)  # Confirm adjusted work rate matches the given value

# Number of workers required
實 = 積  # Volume of the ditch
a = 實 / 法  # Number of workers required
a = a.limit_denominator()  # Simplify the fraction

# Output the result
a#----- content ends here -----

"""
"""
