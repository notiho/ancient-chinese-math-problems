"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
荅曰： a人 。
"""

"""
### Problem Breakdown:

1. **First Part: Calculate the Volume of the Trapezoidal Ditch**
   - Top width = 1 丈 5 尺 = 15 尺
   - Bottom width = 1 丈 = 10 尺
   - Depth = 5 尺
   - Length = 7 丈 = 70 尺
   - Formula for the volume of a trapezoidal prism:
     \[
     V = \frac{(上廣 + 下廣) \times 深}{2} \times 袤
     \]

2. **Second Part: Determine the Number of Workers Needed**
   - Total volume = 4375 尺
   - Each worker's daily capacity = 612 尺 \( \frac{4}{5} \) (including 1/5 extra for soil removal)
   - Formula for the number of workers:
     \[
     人數 = \frac{\text{Total Volume}}{\text{Daily Capacity per Worker}}
     \]

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
上廣 = 15  # in 尺
下廣 = 10  # in 尺
深 = 5     # in 尺
袤 = 70    # in 尺

# Calculate the volume of the ditch
積 = Fraction((上廣 + 下廣) * 深, 2) * 袤

# Verify the calculated volume matches the given value
assert 積 == 4375, "Calculated volume does not match the given value!"

# Worker capacity (including 1/5 extra for soil removal)
每日功 = Fraction(612) + Fraction(4, 5)

# Calculate the number of workers needed
a = 積 / 每日功

# Simplify the result
a = a.limit_denominator()

# Output the number of workers
a
#----- content ends here -----


"""


---

### Explanation of the Code:

1. **Volume Calculation**:
   - The trapezoidal prism formula is used to calculate the volume of the ditch in cubic 尺.
   - The result is verified to match the given value of 4375 尺.

2. **Worker Capacity**:
   - Each worker's daily capacity is given as 612 尺 plus an additional 1/5 for soil removal. This is calculated as \( 612 + \frac{4}{5} \).

3. **Number of Workers**:
   - The total volume is divided by the daily capacity of one worker to determine the number of workers required.
   - The result is simplified using `limit_denominator()` to ensure it is expressed as a proper fraction.

---

### Final Answer:
The number of workers required is \( a \) people.
"""


"""
"""
