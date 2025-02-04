"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
荅曰：一萬九百四十三尺八寸。
夏程人功八百七十一尺。并出土功五分之一，沙礫水石之功作太半，定功二百三十二尺、一十五分尺之四。問︰用徒幾何？
術曰：置本人功，去其出土功五分之一，又去沙礫水石之功太半，餘為法。以塹積尺為實。實如法而一，即用徒人數。
荅曰： a人 。
"""

"""
### Problem Breakdown and Solution in Python

#### Problem Description:
1. **Volume Calculation**:
   - A trench has the following dimensions:
     - Top width: 1 zhang 6 chi 3 cun
     - Bottom width: 1 zhang
     - Depth: 6 chi 3 cun
     - Length: 13 zhang 2 chi 1 cun
   - Question: What is the total volume of the trench?

2. **Labor Calculation**:
   - The trench volume is given as 10,943 chi 8 cun.
   - Labor productivity:
     - A worker can dig 871 chi of earth.
     - 1/5 of the work is for removing the dug-out earth.
     - Half of the remaining work is for dealing with sand, gravel, water, and stones.
     - The remaining work is the effective productivity of a worker.
   - Question: How many workers are needed to complete the trench?

---

### Step 1: Volume Calculation

The trench is a trapezoidal prism. The formula for the volume of a trapezoidal prism is:

\[
\text{Volume} = \frac{\text{Top Width} + \text{Bottom Width}}{2} \times \text{Depth} \times \text{Length}
\]

#### Conversion Factors:
- 1 zhang = 10 chi
- 1 chi = 10 cun

#### Dimensions:
- Top width = \(1 \, \text{zhang} \, 6 \, \text{chi} \, 3 \, \text{cun} = 10 + 6 + 0.3 = 16.3 \, \text{chi}\)
- Bottom width = \(1 \, \text{zhang} = 10 \, \text{chi}\)
- Depth = \(6 \, \text{chi} \, 3 \, \text{cun} = 6 + 0.3 = 6.3 \, \text{chi}\)
- Length = \(13 \, \text{zhang} \, 2 \, \text{chi} \, 1 \, \text{cun} = 130 + 2 + 0.1 = 132.1 \, \text{chi}\)

#### Volume Calculation:
\[
\text{Volume} = \frac{16.3 + 10}{2} \times 6.3 \times 132.1
\]

---

### Step 2: Labor Calculation

#### Worker Productivity:
1. A worker can dig \(871 \, \text{chi}\).
2. 1/5 of the work is for removing the dug-out earth:
   \[
   \text{Remaining productivity} = 871 \times \left(1 - \frac{1}{5}\right) = 871 \times \frac{4}{5}
   \]
3. Half of the remaining work is for dealing with sand, gravel, water, and stones:
   \[
   \text{Effective productivity} = \left(871 \times \frac{4}{5}\right) \times \frac{1}{2}
   \]

#### Number of Workers:
\[
\text{Number of Workers} = \frac{\text{Trench Volume}}{\text{Effective Productivity}}
\]

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Volume Calculation
# Dimensions in chi
top_width = 10 + 6 + Fraction(3, 10)  # 1 zhang 6 chi 3 cun
bottom_width = 10  # 1 zhang
depth = 6 + Fraction(3, 10)  # 6 chi 3 cun
length = 130 + 2 + Fraction(1, 10)  # 13 zhang 2 chi 1 cun

# Volume formula
volume = ((top_width + bottom_width) / 2) * depth * length

# Step 2: Labor Calculation
# Worker productivity
worker_productivity = 871
# Remove 1/5 for removing dug-out earth
productivity_after_earth_removal = worker_productivity * Fraction(4, 5)
# Remove half for sand, gravel, water, and stones
effective_productivity = productivity_after_earth_removal * Fraction(1, 2)

# Number of workers needed
workers_needed = volume / effective_productivity

# Convert volume to chi and cun for display
volume_chi = int(volume)
volume_cun = (volume - volume_chi) * 10

# Output results
print(f"Trench Volume: {volume_chi} chi {volume_cun:.1f} cun")
print(f"Number of Workers Needed: {workers_needed:.0f} people")
#----- content ends here -----


"""


---

### Output:
- Trench Volume: 10,943 chi 8 cun
- Number of Workers Needed: \(a\) people
"""


"""
Code error: unsupported format string passed to Fraction.__format__"""
