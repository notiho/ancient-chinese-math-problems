"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
術曰：置本人功，去其五分之一，餘為法。以溝積尺為實。實如法而一，得用徒人數。
荅曰： a人 。
"""

"""
To solve this problem, we will first calculate the volume of the ditch (溝積) and then determine the number of workers (徒人) required based on the given conditions.

### Step 1: Calculate the volume of the ditch (溝積)
The ditch has a trapezoidal cross-section, with the top width (上廣) of 1丈5尺, the bottom width (下廣) of 1丈, and the depth (深) of 5尺. The length (袤) of the ditch is 7丈. 

1丈 = 10尺.  
The formula for the area of a trapezoid is:
\[
\text{Area} = \frac{\text{Top Width} + \text{Bottom Width}}{2} \times \text{Height}
\]
The volume is then:
\[
\text{Volume} = \text{Area} \times \text{Length}
\]

### Step 2: Determine the number of workers (用徒)
Each worker's daily capacity is given as 766尺, but they can only work 4/5 of that capacity due to the additional effort required for removing soil (出土功五分之一). The effective capacity per worker is:
\[
\text{Effective Capacity} = \text{Daily Capacity} \times \frac{4}{5}
\]
The number of workers required is:
\[
\text{Number of Workers} = \frac{\text{Volume of Ditch}}{\text{Effective Capacity}}
\]

### Python Code

"""


from fractions import Fraction

# Step 1: Calculate the volume of the ditch
top_width = Fraction(1 * 10 + 5, 1)  # 1丈5尺 = 15尺
bottom_width = Fraction(1 * 10, 1)   # 1丈 = 10尺
depth = Fraction(5, 1)               # 5尺
length = Fraction(7 * 10, 1)         # 7丈 = 70尺

# Area of trapezoid cross-section
area = (top_width + bottom_width) / 2 * depth

# Volume of the ditch
volume = area * length

# Step 2: Determine the number of workers
daily_capacity = Fraction(766, 1)  # 766尺
effective_capacity = daily_capacity * Fraction(4, 5)  # 4/5 of daily capacity

# Number of workers required
a = volume / effective_capacity

# Results
volume  # Volume of the ditch in cubic 尺
a       # Number of workers required


"""


### Explanation of Variables
- `volume`: The total volume of the ditch in cubic 尺.
- `a`: The number of workers required to complete the task.

### Final Answer
The number of workers required (`a`) will be computed as a fraction or integer, depending on the exact values.
"""


"""
"""
