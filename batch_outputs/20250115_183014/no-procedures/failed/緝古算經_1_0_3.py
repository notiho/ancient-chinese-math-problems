"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
答曰：在鬥 a度 。
"""

"""
This problem involves ancient Chinese calendrical calculations, specifically determining the position of the moon at a specific time. The problem uses the concept of "章歲" (Zhang Sui), "朔月行定分" (fixed monthly motion), and other calendrical parameters. Let's break it down step by step and solve it.

---

### Problem Breakdown:
1. **Given Data:**
   - The sun is at **斗 (Dipper) 10 degrees and 480/700 parts**.
   - **朔月行定分 (fixed monthly motion)** = 9000.
   - **朔日定小余 (fixed daily remainder)** = 10000.
   - **日法 (solar divisor)** = 20000.
   - **章歲 (Zhang Sui)** = 700 (also called 行分法, or motion divisor).
   - We are calculating the moon's position at **天正十一月朔夜半** (midnight on the first day of the 11th month).

2. **Goal:**
   - Find the moon's position in degrees (a) in the **斗** (Dipper) at the specified time.

3. **Key Formula:**
   - The moon's position is determined by the difference between the sun's position and the moon's motion since the last conjunction (朔).
   - Use the given parameters to calculate the moon's motion and add it to the sun's position.

---

### Solution:


"""


from fractions import Fraction

# Given data
sun_position = Fraction(10) + Fraction(480, 700)  # Sun's position in degrees
fixed_monthly_motion = 9000  # 朔月行定分
fixed_daily_remainder = 10000  # 朔日定小余
solar_divisor = 20000  # 日法
zhang_sui = 700  # 章歲 (motion divisor)

# Step 1: Calculate the moon's motion since the last conjunction
# The moon's motion is determined by the fixed monthly motion divided by the Zhang Sui
moon_motion = Fraction(fixed_monthly_motion, zhang_sui)

# Step 2: Add the moon's motion to the sun's position to find the moon's position
moon_position = sun_position + moon_motion

# Step 3: Normalize the moon's position to within 0-360 degrees
# Since the degrees are in the Dipper (斗), we only care about the fractional part
a = moon_position % 360

# Output the result
a


"""


---

### Explanation of the Code:
1. **Sun's Position:** The sun's position is given as 10 degrees and 480/700 parts. This is converted into a fraction for precise calculations.
2. **Moon's Motion:** The moon's motion since the last conjunction is calculated using the fixed monthly motion divided by the Zhang Sui (motion divisor).
3. **Moon's Position:** The moon's position is the sum of the sun's position and the moon's motion.
4. **Normalization:** The result is normalized to ensure it falls within 0-360 degrees.

---

### Final Answer:
The moon's position at **天正十一月朔夜半** is:

**在鬥 a度**, where `a` is the calculated value in degrees.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 824/35"""
