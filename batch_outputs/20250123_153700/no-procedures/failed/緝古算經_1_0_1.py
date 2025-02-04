"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
答曰：在鬥 a度 。
"""

"""
This is a classical Chinese calendrical problem involving the calculation of the moon's position at a specific time based on the ancient Chinese system of celestial mechanics. Let's break it down step by step and solve it in Python.

---

### Problem Breakdown:
1. **Given Data**:
   - The sun is at **斗 (Dipper) 10 degrees 7/100 degrees × 480/100**.
   - The moon's movement is governed by:
     - **朔月行定分 (fixed monthly movement)** = 9000
     - **朔日定小余 (fixed daily remainder)** = 10000
     - **日法 (daily movement divisor)** = 20000
     - **章歲 (yearly divisor)** = 700 (also called 行分法).

2. **Goal**:
   - Calculate the moon's position in **斗 (Dipper)** degrees at the given time.

3. **Approach**:
   - Use the given parameters to calculate the moon's position relative to the sun.
   - Convert the result into degrees in the **斗** system.

---

### Python Code:


"""


from fractions import Fraction

# Given data
sun_position = Fraction(10) + Fraction(7, 100) * Fraction(480, 100)  # Sun's position in 斗 degrees
fixed_monthly_movement = 9000  # 朔月行定分
fixed_daily_remainder = 10000  # 朔日定小余
daily_movement_divisor = 20000  # 日法
yearly_divisor = 700  # 章歲

# Calculate the moon's position relative to the sun
# 月行 = (朔月行定分 + 朔日定小余) / 日法
moon_relative_position = Fraction(fixed_monthly_movement + fixed_daily_remainder, daily_movement_divisor)

# Add the moon's relative position to the sun's position
moon_position = sun_position + moon_relative_position

# Convert the moon's position into degrees in the 斗 system
斗_degrees = moon_position % 360  # Ensure the position is within 0-360 degrees

# Output the result
a = 斗_degrees
print(f"The moon is at {a} degrees in the Dipper (斗).")


"""


---

### Explanation of the Code:
1. **Sun's Position**:
   - The sun's position is given in degrees, and we calculate it as a fraction for precision.

2. **Moon's Relative Position**:
   - The moon's movement is calculated using the formula:
     \[
     \text{Moon's Movement} = \frac{\text{朔月行定分} + \text{朔日定小余}}{\text{日法}}
     \]

3. **Moon's Final Position**:
   - Add the moon's relative position to the sun's position to get the moon's absolute position.
   - Use modulo 360 to ensure the position is within a full circle (0-360 degrees).

4. **Result**:
   - The result is the moon's position in **斗** degrees.

---

This code provides the moon's position in the **斗** system as a fraction for precision. You can convert it to a decimal if needed.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 5643/500"""
