"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
荅曰： a人 功。內少 b尺 。
"""

"""
Let's solve this step by step.

---

### Problem 1: Calculating the volume of the canal

The canal has the following dimensions:
- Top width (上廣): 1 丈 8 尺 = 18 尺
- Bottom width (下廣): 3 尺 6 寸 = 3.6 尺
- Depth (深): 1 丈 8 尺 = 18 尺
- Length (袤): 51824 尺

The formula for the volume of a trapezoidal prism is:

\[
\text{Volume} = \frac{\text{Top Width} + \text{Bottom Width}}{2} \times \text{Depth} \times \text{Length}
\]

---

### Problem 2: Calculating the number of workers needed

- Total volume: \( 174585.6 \) 尺³ (as given in the problem).
- Each worker can dig \( 300 \) 尺³ per day.

The formula for the number of workers is:

\[
\text{Workers Needed} = \frac{\text{Total Volume}}{\text{Worker Capacity}}
\]

If there is a remainder, it will represent the leftover volume.

---

### Python Code:


"""


from fractions import Fraction

# Dimensions of the canal
top_width = 18  # in 尺
bottom_width = 3.6  # in 尺
depth = 18  # in 尺
length = 51824  # in 尺

# Calculate the volume of the canal
volume = Fraction((top_width + bottom_width), 2) * depth * length

# Worker capacity
worker_capacity = 300  # in 尺³ per worker

# Calculate the number of workers needed
workers = volume // worker_capacity  # Integer division to get full workers
remainder = volume % worker_capacity  # Remaining volume

# Convert results to fractions for precision
a = workers
b = remainder

# Output results
print(f"Total volume: {volume} 尺³")
print(f"Workers needed: {a} 人功")
print(f"Remaining volume: {b} 尺³")


"""


---

### Explanation of Results:
- **Total Volume**: \( 174585.6 \) 尺³
- **Workers Needed**: \( a \) 人功 (integer part of the division)
- **Remaining Volume**: \( b \) 尺³ (remainder of the division)
"""


"""
Code error: both arguments should be Rational instances"""
