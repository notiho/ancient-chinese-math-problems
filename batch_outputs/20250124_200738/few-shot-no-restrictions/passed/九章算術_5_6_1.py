"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
術曰：置本人功，去其五分之一，餘為法。以溝積尺為實。實如法而一，得用徒人數。
荅曰： a人 。
"""

#----- content starts here -----
"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 5 chi (15 chi)
- Bottom width: 1 zhang (10 chi)
- Depth: 5 chi
- Length: 7 zhang (70 chi)

Question 1: What is the volume of the trench?
Answer: 4375 cubic chi.

Additionally:
- A single worker can dig 766 cubic chi of earth, including 1/5 for removing excess soil.
- The effective work rate per worker is 766 - (1/5 of 766) = 612.8 cubic chi.

Question 2: How many workers are needed to dig the trench?

Procedure:
1. Place the work rate per worker, subtracting 1/5, to get the divisor.
2. Use the trench volume as the dividend.
3. Divide the dividend by the divisor to get the number of workers.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the trench
上廣 = 15  # Top width in chi
下廣 = 10  # Bottom width in chi
深 = 5     # Depth in chi
袤 = 70    # Length in chi

# Calculate the volume of the trench
積 = Fraction((上廣 + 下廣), 2) * 深 * 袤  # Trapezoidal prism formula
積 = int(積)  # Convert to integer since the answer is given in whole cubic chi
print(f"Trench volume: {積} cubic chi")

# Worker productivity
本人功 = 766  # Total work rate per worker in cubic chi
去土功 = Fraction(1, 5) * 本人功  # Excess soil removal (1/5 of total work rate)
定功 = 本人功 - 去土功  # Effective work rate per worker

# Calculate the number of workers needed
用徒 = Fraction(積, 定功)  # Divide trench volume by effective work rate
用徒 = 用徒.limit_denominator()  # Simplify the fraction

a = 用徒
print(f"Number of workers needed: {a} workers")#----- content ends here -----

"""
"""
