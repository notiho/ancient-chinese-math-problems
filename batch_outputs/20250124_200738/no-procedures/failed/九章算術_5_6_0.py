"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
荅曰： a人 。
"""

"""
### Problem Breakdown:

1. **Volume of the Trapezoidal Ditch**:
   - Top width: 1丈5尺 = 15尺
   - Bottom width: 1丈 = 10尺
   - Depth: 5尺
   - Length: 7丈 = 70尺
   - Formula for the volume of a trapezoidal prism:  
     \[
     V = \frac{(上廣 + 下廣) \times 深 \times 袤}{2}
     \]

2. **Work Calculation**:
   - Total volume: 4375尺 (as given in the problem).
   - Work per person: 766尺 (春程人功).
   - Additional work for removing soil: 1/5 of the total volume.
   - Total work:  
     \[
     定功 = 春程人功 - \frac{出土功}{5}
     \]

3. **Number of Workers**:
   - Divide the total work by the work per person to find the number of workers.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the ditch
top_width = 15  # in chi
bottom_width = 10  # in chi
depth = 5  # in chi
length = 70  # in chi

# Calculate the volume of the ditch
volume = Fraction((top_width + bottom_width) * depth * length, 2)

# Verify the volume matches the given value
assert volume == 4375, "Calculated volume does not match the given value."

# Work per person
work_per_person = Fraction(766)

# Additional work for removing soil (1/5 of the total volume)
additional_work = Fraction(volume, 5)

# Total work required
total_work = volume + additional_work

# Number of workers required
number_of_workers = total_work / work_per_person

# Simplify the result
number_of_workers = number_of_workers.limit_denominator()

# Output the result
a = number_of_workers
a
#----- content ends here -----


"""


---

### Explanation of the Code:

1. **Volume Calculation**:
   - The trapezoidal prism formula is used to calculate the volume of the ditch.
   - The result is verified against the given value of 4375 chi³.

2. **Work Calculation**:
   - The additional work for removing soil is calculated as 1/5 of the total volume.
   - The total work is the sum of the volume and the additional work.

3. **Number of Workers**:
   - The total work is divided by the work per person to calculate the number of workers required.
   - The result is simplified using `limit_denominator()` to ensure it is expressed as a fraction.

---

### Final Answer:
The number of workers required is \( a \) people, where \( a \) is the result of the calculation.
"""


"""
Variable 'a' has wrong value. Expected: 21875/3064, Actual: 2625/383"""
