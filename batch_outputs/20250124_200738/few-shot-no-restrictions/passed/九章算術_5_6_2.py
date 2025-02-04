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
- Top width: 1 zhang 5 chi (15 chi),
- Bottom width: 1 zhang (10 chi),
- Depth: 5 chi,
- Length: 7 zhang (70 chi).

Question 1: What is the total volume of the ditch?
Answer: 4375 cubic chi.

Additionally, the work rate for one person is 766 cubic chi, including 1/5 of the effort for removing the excavated soil. The adjusted work rate is 612 4/5 cubic chi.
Question 2: How many workers are needed to complete the task?

The procedure says: Place the work rate for one person, remove 1/5 of it, and the remainder becomes the divisor. Use the volume of the ditch as the dividend. Divide the dividend by the divisor to obtain the number of workers.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the ditch
上廣 = 15  # Top width in chi
下廣 = 10  # Bottom width in chi
深 = 5     # Depth in chi
袤 = 70    # Length in chi

# Calculate the volume of the ditch
積 = Fraction((上廣 + 下廣), 2) * 深 * 袤  # Trapezoidal prism formula
積 = int(積)  # Convert to integer since the problem specifies an exact value

# Work rate for one person
本人功 = Fraction(766)  # Total work rate including soil removal
去土功 = 本人功 * Fraction(1, 5)  # 1/5 of the work is for soil removal
法 = 本人功 - 去土功  # Adjusted work rate

# Calculate the number of workers needed
實 = 積  # The volume of the ditch
a = Fraction(實, 法)  # Number of workers

# Convert to mixed fraction for clarity
a_mixed = divmod(a.numerator, a.denominator)
a_result = f"{a_mixed[0]}人 {a_mixed[1]}/{a.denominator}人" if a_mixed[1] != 0 else f"{a_mixed[0]}人"

# Outputs
print(f"溝積: {積} cubic chi")
print(f"用徒: {a_result}")#----- content ends here -----

"""
"""
