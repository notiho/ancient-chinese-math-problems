"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a人 。
"""

#----- content starts here -----
"""
Suppose there is a dam with the following dimensions:
- Bottom width: 2 zhang
- Top width: 8 chi
- Height: 4 chi
- Length: 12 zhang 7 chi

Question 1: What is the total volume of the dam?
Answer: 7112 cubic chi.

Question 2: If one person can complete 444 cubic chi of work, how many workers are needed?
The procedure says: Take the total volume (in cubic chi) as the dividend, and the amount of work one person can complete (in cubic chi) as the divisor. Divide the total volume by the work per person to get the number of workers.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the dam
底廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
頂廣 = 8  # chi
高 = 4  # chi
袤 = 12 * 10 + 7  # Convert zhang and chi to chi (12 zhang 7 chi)

# Calculate the cross-sectional area (trapezoid area formula: A = (a + b) * h / 2)
橫截面積 = Fraction((底廣 + 頂廣) * 高, 2)

# Calculate the total volume (Volume = cross-sectional area * length)
積 = 橫截面積 * 袤

# Verify the total volume matches the given answer
assert 積 == 7112, f"Calculated volume {積} does not match the given answer of 7112 cubic chi."

# Work per person
程功 = 444  # cubic chi

# Calculate the number of workers needed
a = Fraction(積, 程功)

# Output the number of workers
a#----- content ends here -----

"""
"""
