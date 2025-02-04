"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a人 。
"""

#----- content starts here -----
"""
Suppose there is a dike with the following dimensions:
- Bottom width: 2 zhang
- Top width: 8 chi
- Height: 4 chi
- Length: 12 zhang 7 chi

Question 1: What is the total volume of the dike?
Answer: 7112 cubic chi.

Question 2: If one worker can handle 444 cubic chi of work, how many workers are needed?
Procedure: Use the total volume as the dividend and the worker's capacity as the divisor. Divide the total volume by the worker's capacity to find the number of workers.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the dike
底廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
頂廣 = 8  # chi
高 = 4  # chi
袤 = 12 * 10 + 7  # Convert 12 zhang 7 chi to chi

# Calculate the volume of the dike
# Volume formula for a trapezoidal prism: V = (1/2) * (底廣 + 頂廣) * 高 * 袤
積 = Fraction(1, 2) * (底廣 + 頂廣) * 高 * 袤

# Given total volume in the problem
assert 積 == 7112  # Verify the calculated volume matches the given value

# Worker capacity
程功 = 444  # cubic chi per worker

# Calculate the number of workers needed
a = Fraction(積, 程功)

# Convert to an integer (since we can't have fractional workers, round up)
a = int(a) if a == int(a) else int(a) + 1  # Round up if there's a remainder

a  # Output the number of workers needed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1778/111, Actual: 17"""
