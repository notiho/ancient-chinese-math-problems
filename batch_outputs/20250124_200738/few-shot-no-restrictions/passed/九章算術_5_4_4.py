"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a人 。
"""

#----- content starts here -----
"""
Suppose there is a dike with a bottom width of 2 zhang, a top width of 8 chi, a height of 4 chi, and a length of 12 zhang 7 chi.
Question: what is the total volume?

The answer says: 7112 cubic chi.

If one worker can handle 444 cubic chi of earthwork in a day, how many workers are needed?

The procedure says: Take the total volume as the dividend and the worker's daily capacity as the divisor. Divide the volume by the capacity to get the number of workers.

The answer says: *a* workers.
"""

from fractions import Fraction

# Dimensions of the dike
底廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
頂廣 = 8  # chi
高 = 4  # chi
袤 = 12 * 10 + 7  # Convert zhang and chi to total chi

# Calculate the volume of the trapezoidal prism
# Formula: V = (1/2) * (底廣 + 頂廣) * 高 * 袤
積 = Fraction(1, 2) * (底廣 + 頂廣) * 高 * 袤

# Verify the volume matches the given answer
assert 積 == 7112, f"Calculated volume {積} does not match the given answer."

# Worker capacity
程功 = 444  # cubic chi per worker per day

# Calculate the number of workers needed
a = Fraction(積, 程功)

# Output the result
a#----- content ends here -----

"""
"""
