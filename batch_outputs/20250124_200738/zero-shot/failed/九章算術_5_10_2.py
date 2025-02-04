"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a trapezoidal prism (the canal) and determining the number of workers required to complete the task.

### Problem Breakdown:
1. **Canal Dimensions**:
   - Top width = 1丈8尺 = 18尺
   - Bottom width = 3尺6寸 = 3.6尺
   - Depth = 1丈8尺 = 18尺
   - Length = 51824尺

2. **Volume Calculation**:
   - The cross-sectional area of the trapezoid is calculated as:
     \[
     \text{Area} = \frac{\text{Top Width} + \text{Bottom Width}}{2} \times \text{Depth}
     \]
   - The volume is then:
     \[
     \text{Volume} = \text{Area} \times \text{Length}
     \]

3. **Worker Calculation**:
   - Each worker can dig 300尺³ per day.
   - The number of workers required is:
     \[
     \text{Workers} = \frac{\text{Volume}}{\text{Worker Capacity}}
     \]
   - If the division is not exact, the remainder (in 尺³) is also calculated.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
top_width = Fraction(18)  # in 尺
bottom_width = Fraction(3.6)  # in 尺
depth = Fraction(18)  # in 尺
length = Fraction(51824)  # in 尺
worker_capacity = Fraction(300)  # in 尺³ per worker

# Step 1: Calculate the cross-sectional area of the trapezoid
cross_sectional_area = (top_width + bottom_width) / 2 * depth  # in 尺²

# Step 2: Calculate the total volume of the canal
volume = cross_sectional_area * length  # in 尺³

# Step 3: Calculate the number of workers required and the remainder
a = volume // worker_capacity  # Number of workers (integer division)
b = volume % worker_capacity  # Remaining volume in 尺³

# Results
a  # Number of workers
b  # Remaining volume in 尺³
#----- content ends here -----


"""


### Explanation of the Code:
1. **Cross-sectional Area**:
   - The trapezoidal area is calculated using the formula for the area of a trapezoid.
2. **Volume**:
   - The volume is obtained by multiplying the cross-sectional area by the length of the canal.
3. **Workers and Remainder**:
   - The number of workers is calculated using integer division (`//`), and the remainder is calculated using the modulus operator (`%`).

### Final Results:
- `a`: The number of workers required.
- `b`: The remaining volume in 尺³ that is not covered by the workers.

This code directly translates the ancient problem into a modern computational approach using Python.
"""


"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 40194626674287507/140737488355328"""
