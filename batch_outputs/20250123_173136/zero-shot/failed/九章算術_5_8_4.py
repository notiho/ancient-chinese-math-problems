"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
荅曰：一萬九百四十三尺八寸。
夏程人功八百七十一尺。并出土功五分之一，沙礫水石之功作太半，定功二百三十二尺、一十五分尺之四。問︰用徒幾何？
術曰：置本人功，去其出土功五分之一，又去沙礫水石之功太半，餘為法。以塹積尺為實。實如法而一，即用徒人數。
荅曰： a人 。
"""

"""
To solve this problem, we will first compute the volume of the trench (塹積) in cubic feet (尺). Then, we will calculate the number of workers (徒人數) required based on the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Step 1: Compute the volume of the trench (塹積)
# Dimensions of the trench:
top_width = Fraction(1, 1) + Fraction(6, 10) + Fraction(3, 100)  # 1丈6尺3寸
bottom_width = Fraction(1, 1)  # 1丈
depth = Fraction(6, 10) + Fraction(3, 100)  # 6尺3寸
length = Fraction(13, 1) + Fraction(2, 10) + Fraction(1, 100)  # 13丈2尺1寸

# Volume formula for a trapezoidal prism: V = (1/2) * (top_width + bottom_width) * depth * length
volume = Fraction(1, 2) * (top_width + bottom_width) * depth * length

# Convert volume to cubic feet (尺)
volume_in_cubic_feet = volume

# Step 2: Compute the number of workers (徒人數)
# Given data:
worker_capacity = Fraction(871, 1)  # 871 cubic feet per worker
soil_removal_fraction = Fraction(1, 5)  # 1/5 of the work is for soil removal
sand_gravel_fraction = Fraction(1, 2)  # 1/2 of the remaining work is for sand, gravel, water, and stones
fixed_work = Fraction(232, 1) + Fraction(4, 15)  # 232尺 and 4/15尺

# Adjust worker capacity:
adjusted_worker_capacity = worker_capacity - (worker_capacity * soil_removal_fraction) - (worker_capacity * sand_gravel_fraction)

# Compute the number of workers:
a = volume_in_cubic_feet / adjusted_worker_capacity

# Output the result
a


"""


### Explanation of the Code:
1. **Volume Calculation**:
   - The trench is a trapezoidal prism. Its volume is calculated using the formula for the volume of a trapezoidal prism: \( V = \frac{1}{2} \times (\text{top width} + \text{bottom width}) \times \text{depth} \times \text{length} \).
   - All dimensions are converted into fractions to ensure precision.

2. **Worker Capacity Adjustment**:
   - The worker's capacity is reduced by the fraction of work for soil removal (\( \frac{1}{5} \)).
   - The remaining work is further reduced by the fraction for sand, gravel, water, and stones (\( \frac{1}{2} \)).
   - The fixed work (\( 232 \) and \( \frac{4}{15} \)) is added to the adjusted capacity.

3. **Number of Workers**:
   - The total volume of the trench is divided by the adjusted worker capacity to compute the number of workers required.

### Final Answer:
The variable `a` contains the number of workers required.
"""


"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: 7295883/174200000"""
