"""
秋程人功三百尺，問︰用徒幾何？
荅曰：三萬三千五百八十二人功。內少一十四尺四寸。
一千人先到，問︰當受袤幾何？
荅曰： a丈 。
"""

"""
This problem involves calculating the work done by laborers (measured in "person-work" or "人功") and determining how much length (袤) a group of 1000 workers can complete.

### Problem Breakdown:
1. **秋程人功三百尺**: The total work required is 300 chi (尺), which corresponds to **33,582 person-work** (人功).
2. **內少一十四尺四寸**: There is a leftover of **14 chi and 4 cun** (寸) that needs to be accounted for.
3. **一千人先到**: 1000 workers arrive first.
4. **問當受袤幾何**: We need to calculate how much length (袤) these 1000 workers can complete.

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total work required
total_work = 33582  # in person-work
total_length = 300  # in chi

# Convert leftover into chi
leftover_length = 14 + Fraction(4, 10)  # 14 chi and 4 cun (1 chi = 10 cun)

# Effective length to be worked on
effective_length = total_length - leftover_length

# Work per chi (尺)
work_per_chi = total_work / effective_length

# Number of workers
workers = 1000

# Calculate the length (袤) that 1000 workers can complete
a = Fraction(workers, work_per_chi)

# Convert result into zhang (丈), where 1 zhang = 10 chi
a_in_zhang = a / 10

# Output the result
a_in_zhang
#----- content ends here -----


"""


### Explanation:
1. **Work per chi**: We calculate how much person-work is required to complete 1 chi of length.
2. **Length for 1000 workers**: Using the work per chi, we calculate how much length 1000 workers can complete.
3. **Convert to zhang**: Since the answer is requested in zhang (丈), we divide the result by 10 (1 zhang = 10 chi).

---

### Final Answer:
The value of `a` (in zhang) will be the length that 1000 workers can complete.
"""


"""
Variable 'a' has wrong value. Expected: 12500/81, Actual: 47600/5597"""
