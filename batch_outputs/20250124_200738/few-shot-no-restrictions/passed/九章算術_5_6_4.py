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

Question 1: What is the volume of the ditch?
Answer: 4375 cubic chi.

Additionally, the labor capacity of one person is 766 cubic chi, but with 1/5 of the effort spent on removing the soil, the effective capacity is reduced to 612 4/5 cubic chi.
Question 2: How many workers are required to dig the ditch?

The procedure says: Place the labor capacity of one person, subtract 1/5 of it, and the remainder becomes the divisor. Use the volume of the ditch as the dividend. Divide the dividend by the divisor to determine the number of workers.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the ditch
上廣 = 15  # Top width in chi
下廣 = 10  # Bottom width in chi
深 = 5     # Depth in chi
袤 = 70    # Length in chi

# Calculate the volume of the ditch
# Formula: Volume = (Top width + Bottom width) / 2 * Depth * Length
積 = Fraction((上廣 + 下廣), 2) * 深 * 袤

# Verify the calculated volume
assert 積 == 4375  # The volume should match the given answer

# Labor capacity of one person
本人功 = Fraction(766)  # Total capacity in cubic chi

# Subtract 1/5 for soil removal
有效功 = 本人功 - 本人功 * Fraction(1, 5)

# Use the ditch volume as the dividend and effective capacity as the divisor
a = Fraction(積, 有效功)

# Convert the result to a mixed number for clarity
a_整數部分 = a.numerator // a.denominator
a_分數部分 = Fraction(a.numerator % a.denominator, a.denominator)

# Final answer
a_人數 = f"{a_整數部分}人 {a_分數部分}人"
a_人數#----- content ends here -----

"""
"""
