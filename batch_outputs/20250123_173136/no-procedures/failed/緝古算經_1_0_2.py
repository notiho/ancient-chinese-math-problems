"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
答曰：在鬥 a度 。
"""

"""
This problem involves ancient Chinese calendrical calculations, specifically determining the position of the moon at a specific time (朔夜半, the midnight of the first day of the lunar month). The calculations are based on the "Zhang Sui" (章歲) system, which uses specific constants for the motion of the moon and the sun.

Let's break this down step by step in Python:

---

### Problem Breakdown:
1. **Given Data:**
   - The sun is at 鬥 (Dipper) 10 degrees and 480/700 of a degree.
   - Constants:
     - 章歲 (Zhang Sui): 700 (also called 行分法).
     - 朔月行定分: 9000 (the moon's motion per synodic month).
     - 朔日定小余: 10000 (the moon's offset per day).
     - 日法: 20000 (the sun's motion per day).

2. **Goal:**
   - Calculate the moon's position at midnight of the first day of the lunar month (朔夜半).

3. **Approach:**
   - The moon's position is calculated relative to the sun's position.
   - Use modular arithmetic to determine the moon's position within the 360-degree circle.

---

### Python Code:


"""


from fractions import Fraction

# Given constants
sun_position = 10 + Fraction(480, 700)  # Sun's position in degrees
zhang_sui = 700  # Zhang Sui constant
moon_motion_per_month = 9000  # Moon's motion per synodic month
moon_offset_per_day = 10000  # Moon's offset per day
sun_motion_per_day = 20000  # Sun's motion per day

# Step 1: Calculate the moon's position relative to the sun
# The moon's position is determined by the difference between the moon's motion and the sun's motion
relative_motion = moon_motion_per_month - sun_motion_per_day

# Step 2: Normalize the relative motion to the Zhang Sui system
normalized_motion = relative_motion % zhang_sui

# Step 3: Add the sun's position to get the moon's position
moon_position = sun_position + Fraction(normalized_motion, zhang_sui) * 360

# Step 4: Normalize the moon's position within 360 degrees
moon_position = moon_position % 360

# Result
a = moon_position
print(f"The moon is at 鬥 {a} degrees.")


"""


---

### Explanation of the Code:
1. **Sun's Position:** The sun's position is given as 10 degrees and 480/700 of a degree. This is converted into a fractional value.
2. **Relative Motion:** The difference between the moon's motion per month and the sun's motion per day is calculated.
3. **Normalize to Zhang Sui:** The relative motion is reduced modulo 700 (the Zhang Sui constant).
4. **Moon's Position:** The moon's position is calculated by adding the normalized relative motion to the sun's position.
5. **Normalize to 360 Degrees:** Since positions are within a 360-degree circle, the result is taken modulo 360.

---

### Example Output:
If you run the code, it will calculate the moon's position in degrees relative to 鬥 (Dipper). The result will be in the form of a fractional degree.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 3974/35"""
