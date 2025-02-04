"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
荅曰： a丈 。
"""

"""
Suppose there is an autumn project requiring 300 chi of work, and the total labor required is 33,582 person-chi, with 14 chi and 4 cun remaining.

If 1,000 workers arrive first, how much length (in zhang) should they complete?

Answer: *a* zhang.
"""

# Total labor required
total_labor = 33582 - (14 + Fraction(4, 10))  # Subtract the remaining 14 chi and 4 cun

# Number of workers arriving first
workers = 1000

# Calculate the length they should complete
# Each worker contributes 1 chi of work, so divide total labor by workers
length_in_chi = total_labor / workers

# Convert chi to zhang (1 zhang = 10 chi)
a = length_in_chi / 10  # Convert to zhang

a
"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 83919/25000"""
