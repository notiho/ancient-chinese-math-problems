"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
術曰：置本人功，去其五分之一，餘為法。以溝積尺為實。實如法而一，得用徒人數。
荅曰： a人 。
"""

"""
To solve the problem, we need to compute the number of workers (`a`) required based on the given dimensions and the rules provided. Let's break it into steps and translate it into Python code.

### Problem Breakdown:
1. **Calculate the volume of the ditch (溝積):**
   - The ditch has a trapezoidal cross-section with:
     - Top width = 1丈5尺 = 15尺
     - Bottom width = 1丈 = 10尺
     - Depth = 5尺
   - Length (袤) = 7丈 = 70尺
   - The formula for the volume of a trapezoidal prism is:
     \[
     \text{Volume} = \frac{1}{2} \times (\text{Top Width} + \text{Bottom Width}) \times \text{Depth} \times \text{Length}
     \]

2. **Determine the number of workers (`a`):**
   - Each worker can handle 766尺 of work, but 1/5 of that is used for "出土功" (additional work for removing soil), so the effective work per worker is:
     \[
     \text{Effective Work per Worker} = 766 - \frac{766}{5}
     \]
   - The total work required is the volume of the ditch.
   - The number of workers is:
     \[
     \text{Number of Workers} = \frac{\text{Volume}}{\text{Effective Work per Worker}}
     \]

### Python Code:

"""


from fractions import Fraction

# Step 1: Calculate the volume of the ditch
top_width = 15  # in 尺
bottom_width = 10  # in 尺
depth = 5  # in 尺
length = 70  # in 尺

volume = Fraction(1, 2) * (top_width + bottom_width) * depth * length  # in cubic 尺

# Step 2: Calculate the effective work per worker
total_work_per_worker = 766  # in cubic 尺
effective_work_per_worker = total_work_per_worker - Fraction(1, 5) * total_work_per_worker  # in cubic 尺

# Step 3: Calculate the number of workers
a = volume / effective_work_per_worker

# Output the result
a


"""


### Explanation of the Code:
1. **Volume Calculation:**
   - The trapezoidal cross-section area is computed using the formula for the area of a trapezoid.
   - Multiply the area by the length to get the volume.

2. **Effective Work per Worker:**
   - Subtract 1/5 of the total work capacity from each worker's capacity to account for the additional work.

3. **Number of Workers:**
   - Divide the total volume by the effective work per worker to get the number of workers required.

### Result:
The variable `a` will contain the number of workers required, represented as a `Fraction`.
"""


"""
"""
